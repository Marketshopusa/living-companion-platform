"""Companion Core identity domain (Gate 1)."""

from core.identity.errors import IdentityError
from core.identity.principal import Principal
from core.identity.service import IdentityCommandService

__all__ = ["IdentityError", "IdentityCommandService", "Principal"]
