"""Server-side identity access policy. Clients cannot grant themselves access."""

from __future__ import annotations

from typing import Any

from core.identity.errors import IdentityError
from core.identity.principal import Principal


class IdentityAccessPolicy:
    def assert_can_read(self, principal: Principal, document: dict[str, Any]) -> None:
        self._assert_tenant(principal, document["tenant_id"])
        self._assert_role(principal, document)

    def assert_can_write(self, principal: Principal, document: dict[str, Any]) -> None:
        self._assert_tenant(principal, document["tenant_id"])
        self._assert_role(principal, document)

    def assert_create_owner(self, principal: Principal, owner_user_id: str) -> None:
        if owner_user_id == principal.user_id:
            return
        if principal.is_tenant_admin():
            return
        raise IdentityError("forbidden", "principal cannot create a Companion for another owner")

    def assert_same_tenant_owner(self, principal: Principal, owner_user_id: str) -> None:
        del owner_user_id
        # Owner records have no separate tenant table in Gate 1; tenant is the principal's tenant.
        if not principal.tenant_id:
            raise IdentityError("validation_error", "tenant_id is required")

    def _assert_tenant(self, principal: Principal, tenant_id: str) -> None:
        if principal.tenant_id != tenant_id:
            raise IdentityError("forbidden", "cross-tenant identity access is denied")

    def _assert_role(self, principal: Principal, document: dict[str, Any]) -> None:
        if principal.is_tenant_admin():
            return
        if principal.user_id == document["owner_user_id"]:
            return
        raise IdentityError("forbidden", "principal is not the Companion owner")
