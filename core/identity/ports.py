"""Ports for Companion identity. No vendor SDKs."""

from __future__ import annotations

from typing import Any, Protocol


class CompanionIdentityRepository(Protocol):
    def get(self, companion_id: str) -> dict[str, Any] | None:
        ...

    def create(self, document: dict[str, Any]) -> dict[str, Any]:
        ...

    def save(self, document: dict[str, Any], expected_config_revision: int) -> dict[str, Any]:
        ...


class Clock(Protocol):
    def now_rfc3339(self) -> str:
        ...


class IdGenerator(Protocol):
    def new_uuid(self) -> str:
        ...
