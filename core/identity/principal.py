"""Simulated principal for Gate 1. Not production authentication (Point 39)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Principal:
    tenant_id: str
    user_id: str
    actor_id: str
    role: str = "owner"

    def is_tenant_admin(self) -> bool:
        return self.role == "tenant_admin"
