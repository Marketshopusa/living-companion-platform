"""Identity command service: the only mutation API for canonical Companion identity."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from core.identity.canonicalize import canonicalize, dumps_canonical
from core.identity.clock import SystemClock, Uuid4Generator
from core.identity.errors import IdentityError
from core.identity.policy import IdentityAccessPolicy
from core.identity.ports import Clock, CompanionIdentityRepository, IdGenerator
from core.identity.principal import Principal
from core.identity.schema import validate_command, validate_error, validate_identity

IMMUTABLE_FIELDS = ("companion_id", "tenant_id", "owner_user_id", "created_at")


class IdentityCommandService:
    def __init__(
        self,
        repository: CompanionIdentityRepository,
        *,
        policy: IdentityAccessPolicy | None = None,
        clock: Clock | None = None,
        ids: IdGenerator | None = None,
    ) -> None:
        self._repository = repository
        self._policy = policy or IdentityAccessPolicy()
        self._clock = clock or SystemClock()
        self._ids = ids or Uuid4Generator()

    def handle(self, principal: Principal, command: dict[str, Any]) -> dict[str, Any]:
        validate_command(command)
        name = command["command"]
        if name == "CreateCompanion":
            return self.create_companion(principal, command)
        if name == "GetCompanion":
            return self.get_companion(principal, command["companion_id"])
        if name == "UpdateCompanionConfiguration":
            return self.update_companion_configuration(principal, command)
        if name == "SetCompanionStatus":
            return self.set_companion_status(principal, command)
        raise IdentityError("validation_error", "unknown command")

    def create_companion(self, principal: Principal, command: dict[str, Any]) -> dict[str, Any]:
        owner_user_id = command["owner_user_id"].lower()
        self._policy.assert_same_tenant_owner(principal, owner_user_id)
        self._policy.assert_create_owner(principal, owner_user_id)
        now = self._clock.now_rfc3339()
        document: dict[str, Any] = {
            "companion_id": self._ids.new_uuid().lower(),
            "tenant_id": principal.tenant_id.lower(),
            "owner_user_id": owner_user_id,
            "created_at": now,
            "updated_at": now,
            "identity_schema_version": 1,
            "config_revision": 1,
            "created_by_actor": principal.actor_id,
            "updated_by_actor": principal.actor_id,
            "display_name": command["display_name"],
            "age_presentation": command.get("age_presentation"),
            "gender_presentation": command.get("gender_presentation"),
            "status": "active",
            "personality": deepcopy(command["personality"]),
            "configuration": deepcopy(command["configuration"]),
            "metadata": deepcopy(command.get("metadata") or {}),
        }
        canonical = self._validated(document)
        stored = self._repository.create(canonical)
        return self._validated(stored)

    def get_companion(self, principal: Principal, companion_id: str) -> dict[str, Any]:
        document = self._load_for_principal(principal, companion_id)
        self._policy.assert_can_read(principal, document)
        return self._validated(document)

    def update_companion_configuration(
        self, principal: Principal, command: dict[str, Any]
    ) -> dict[str, Any]:
        current = self._load_for_principal(principal, command["companion_id"])
        self._policy.assert_can_write(principal, current)
        self._assert_revision(current, command["expected_config_revision"])
        updated = deepcopy(current)
        for key in (
            "display_name",
            "age_presentation",
            "gender_presentation",
            "personality",
            "configuration",
            "metadata",
        ):
            if key in command:
                updated[key] = deepcopy(command[key])
        self._reject_immutable_tamper(current, updated)
        updated["updated_at"] = self._clock.now_rfc3339()
        updated["updated_by_actor"] = principal.actor_id
        updated["config_revision"] = current["config_revision"] + 1
        canonical = self._validated(updated)
        stored = self._repository.save(canonical, command["expected_config_revision"])
        return self._validated(stored)

    def set_companion_status(self, principal: Principal, command: dict[str, Any]) -> dict[str, Any]:
        current = self._load_for_principal(principal, command["companion_id"])
        self._policy.assert_can_write(principal, current)
        self._assert_revision(current, command["expected_config_revision"])
        updated = deepcopy(current)
        updated["status"] = command["status"]
        self._reject_immutable_tamper(current, updated)
        updated["updated_at"] = self._clock.now_rfc3339()
        updated["updated_by_actor"] = principal.actor_id
        updated["config_revision"] = current["config_revision"] + 1
        canonical = self._validated(updated)
        stored = self._repository.save(canonical, command["expected_config_revision"])
        return self._validated(stored)

    def dumps(self, document: dict[str, Any]) -> str:
        return dumps_canonical(self._validated(document))

    def _load_for_principal(self, principal: Principal, companion_id: str) -> dict[str, Any]:
        document = self._repository.get(companion_id.lower())
        if document is None:
            raise IdentityError("not_found", "companion identity not found")
        canonical = canonicalize(document)
        if canonical["tenant_id"] != principal.tenant_id.lower():
            raise IdentityError("forbidden", "cross-tenant identity access is denied")
        return canonical

    def _validated(self, document: dict[str, Any]) -> dict[str, Any]:
        canonical = canonicalize(document)
        validate_identity(canonical)
        return canonical

    def _assert_revision(self, current: dict[str, Any], expected: int) -> None:
        if current["config_revision"] != expected:
            raise IdentityError("conflict", "config_revision does not match stored identity")

    def _reject_immutable_tamper(self, before: dict[str, Any], after: dict[str, Any]) -> None:
        for field in IMMUTABLE_FIELDS:
            if before[field] != after[field]:
                raise IdentityError("validation_error", f"{field} is immutable")
        if before["identity_schema_version"] != after["identity_schema_version"]:
            raise IdentityError("validation_error", "identity_schema_version is immutable")


class ClientIdentityGateway:
    """Simulated client facade. Holds no competing identity store."""

    def __init__(self, service: IdentityCommandService, principal: Principal) -> None:
        self._service = service
        self._principal = principal

    def create(self, command: dict[str, Any]) -> dict[str, Any]:
        payload = {"command": "CreateCompanion", **command}
        return self._service.handle(self._principal, payload)

    def get(self, companion_id: str) -> dict[str, Any]:
        return self._service.handle(
            self._principal,
            {"command": "GetCompanion", "companion_id": companion_id},
        )

    def update(self, command: dict[str, Any]) -> dict[str, Any]:
        payload = {"command": "UpdateCompanionConfiguration", **command}
        return self._service.handle(self._principal, payload)

    def set_status(self, command: dict[str, Any]) -> dict[str, Any]:
        payload = {"command": "SetCompanionStatus", **command}
        return self._service.handle(self._principal, payload)

    def canonical_json(self, document: dict[str, Any]) -> str:
        return self._service.dumps(document)


def error_document(exc: IdentityError) -> dict[str, Any]:
    doc = exc.to_document()
    validate_error(doc)
    return doc
