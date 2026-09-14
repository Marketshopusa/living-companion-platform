"""In-memory Companion identity repository."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from core.identity.canonicalize import canonicalize, dumps_canonical, loads_canonical
from core.identity.errors import IdentityError
from core.identity.schema import validate_identity


class InMemoryIdentityRepository:
    def __init__(self) -> None:
        self._documents: dict[str, str] = {}

    def get(self, companion_id: str) -> dict[str, Any] | None:
        raw = self._documents.get(companion_id.lower())
        if raw is None:
            return None
        return loads_canonical(raw)

    def create(self, document: dict[str, Any]) -> dict[str, Any]:
        canonical = self._prepare(document)
        companion_id = canonical["companion_id"]
        if companion_id in self._documents:
            raise IdentityError("conflict", "companion_id already exists")
        self._documents[companion_id] = dumps_canonical(canonical)
        return loads_canonical(self._documents[companion_id])

    def save(self, document: dict[str, Any], expected_config_revision: int) -> dict[str, Any]:
        canonical = self._prepare(document)
        companion_id = canonical["companion_id"]
        existing_raw = self._documents.get(companion_id)
        if existing_raw is None:
            raise IdentityError("not_found", "companion identity not found")
        existing = loads_canonical(existing_raw)
        if existing["config_revision"] != expected_config_revision:
            raise IdentityError("conflict", "config_revision does not match stored identity")
        if canonical["config_revision"] != expected_config_revision + 1:
            raise IdentityError("validation_error", "config_revision must increment by 1")
        self._documents[companion_id] = dumps_canonical(canonical)
        return loads_canonical(self._documents[companion_id])

    def _prepare(self, document: dict[str, Any]) -> dict[str, Any]:
        canonical = canonicalize(deepcopy(document))
        validate_identity(canonical)
        return canonical
