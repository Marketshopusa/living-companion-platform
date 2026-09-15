"""Local identity persistence. No database, no cloud."""

from backend.identity.file_store import JsonFileIdentityRepository
from backend.identity.memory_store import InMemoryIdentityRepository

__all__ = ["InMemoryIdentityRepository", "JsonFileIdentityRepository"]
