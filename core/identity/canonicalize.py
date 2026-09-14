"""Deterministic canonical JSON for identity documents."""

from __future__ import annotations

import json
import math
import re
from typing import Any

from core.identity.errors import IdentityError

_UUID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
)
_RFC3339_Z_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$"
)


def _normalize(value: Any, key: str | None = None) -> Any:
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            raise IdentityError("validation_error", "non-finite number is not allowed")
        return value
    if isinstance(value, dict):
        return {k: _normalize(value[k], k) for k in sorted(value)}
    if isinstance(value, list):
        return [_normalize(item) for item in value]
    if isinstance(value, str):
        if key in {"companion_id", "tenant_id", "owner_user_id"}:
            lowered = value.lower()
            if not _UUID_RE.match(lowered):
                raise IdentityError("validation_error", f"invalid uuid for {key}")
            return lowered
        if key in {"created_at", "updated_at"}:
            text = value.strip()
            if text.endswith("+00:00"):
                text = text[:-6] + "Z"
            if not _RFC3339_Z_RE.match(text):
                raise IdentityError("validation_error", f"invalid RFC 3339 UTC timestamp for {key}")
            return text
        return value
    return value


def canonicalize(document: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(document, dict):
        raise IdentityError("validation_error", "identity document must be an object")
    return _normalize(document)


def dumps_canonical(document: dict[str, Any]) -> str:
    canonical = canonicalize(document)
    return json.dumps(canonical, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def loads_canonical(text: str) -> dict[str, Any]:
    data = json.loads(text)
    if not isinstance(data, dict):
        raise IdentityError("validation_error", "identity document must be an object")
    return canonicalize(data)
