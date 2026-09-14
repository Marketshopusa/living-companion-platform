"""JSON-file Companion identity repository. One document per companion_id."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

from core.identity.canonicalize import canonicalize, dumps_canonical, loads_canonical
from core.identity.errors import IdentityError
from core.identity.schema import validate_identity


class JsonFileIdentityRepository:
    def __init__(self, root: str | Path) -> None:
        self._root = Path(root)
        self._root.mkdir(parents=True, exist_ok=True)

    def get(self, companion_id: str) -> dict[str, Any] | None:
        path = self._path(companion_id)
        if not path.is_file():
            return None
        return loads_canonical(path.read_text(encoding="utf-8"))

    def create(self, document: dict[str, Any]) -> dict[str, Any]:
        canonical = self._prepare(document)
        path = self._path(canonical["companion_id"])
        if path.exists():
            raise IdentityError("conflict", "companion_id already exists")
        self._atomic_write(path, dumps_canonical(canonical))
        return loads_canonical(path.read_text(encoding="utf-8"))

    def save(self, document: dict[str, Any], expected_config_revision: int) -> dict[str, Any]:
        canonical = self._prepare(document)
        path = self._path(canonical["companion_id"])
        if not path.is_file():
            raise IdentityError("not_found", "companion identity not found")
        existing = loads_canonical(path.read_text(encoding="utf-8"))
        if existing["config_revision"] != expected_config_revision:
            raise IdentityError("conflict", "config_revision does not match stored identity")
        if canonical["config_revision"] != expected_config_revision + 1:
            raise IdentityError("validation_error", "config_revision must increment by 1")
        self._atomic_write(path, dumps_canonical(canonical))
        return loads_canonical(path.read_text(encoding="utf-8"))

    def _path(self, companion_id: str) -> Path:
        return self._root / f"{companion_id.lower()}.json"

    def _prepare(self, document: dict[str, Any]) -> dict[str, Any]:
        canonical = canonicalize(deepcopy(document))
        validate_identity(canonical)
        return canonical

    def _atomic_write(self, path: Path, text: str) -> None:
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(text, encoding="utf-8")
        tmp.replace(path)


class FailingIdentityRepository:
    """Test double: persist operations fail without writing."""

    def __init__(self, inner: Any, *, fail_on: str = "save", code: str = "timeout") -> None:
        self._inner = inner
        self._fail_on = fail_on
        self._code = code

    def get(self, companion_id: str) -> dict[str, Any] | None:
        return self._inner.get(companion_id)

    def create(self, document: dict[str, Any]) -> dict[str, Any]:
        if self._fail_on == "create":
            raise IdentityError(self._code, "forced persistence failure")
        return self._inner.create(document)

    def save(self, document: dict[str, Any], expected_config_revision: int) -> dict[str, Any]:
        if self._fail_on == "save":
            raise IdentityError(self._code, "forced persistence failure")
        return self._inner.save(document, expected_config_revision)
