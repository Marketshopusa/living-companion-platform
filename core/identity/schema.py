"""JSON Schema validation for identity contracts v1 (Draft 2020-12)."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError
from referencing import Registry, Resource

from core.identity.errors import IdentityError

CONTRACTS_V1 = Path(__file__).resolve().parents[1] / "contracts" / "identity" / "v1"
FORMAT_CHECKER = FormatChecker()

_SCHEMA_FILES = {
    "https://living-companion.local/contracts/identity/v1/personality-configuration": "personality-configuration.schema.json",
    "https://living-companion.local/contracts/identity/v1/companion-configuration": "companion-configuration.schema.json",
    "https://living-companion.local/contracts/identity/v1/companion-identity": "companion-identity.schema.json",
    "https://living-companion.local/contracts/identity/v1/commands": "commands.schema.json",
    "https://living-companion.local/contracts/identity/v1/errors": "errors.schema.json",
}


@lru_cache(maxsize=1)
def _registry() -> Registry:
    resources = []
    for uri, filename in _SCHEMA_FILES.items():
        raw = json.loads((CONTRACTS_V1 / filename).read_text(encoding="utf-8"))
        resources.append((uri, Resource.from_contents(raw)))
    registry: Registry = Registry()
    for uri, resource in resources:
        registry = registry.with_resource(uri, resource)
    return registry


def _validator(schema_uri: str) -> Draft202012Validator:
    resource = _registry()[schema_uri]
    return Draft202012Validator(
        resource.contents,
        registry=_registry(),
        format_checker=FORMAT_CHECKER,
    )


def validate_document(schema_uri: str, document: dict[str, Any]) -> None:
    try:
        _validator(schema_uri).validate(document)
    except ValidationError as exc:
        raise IdentityError("validation_error", exc.message) from exc


def validate_identity(document: dict[str, Any]) -> None:
    validate_document(
        "https://living-companion.local/contracts/identity/v1/companion-identity",
        document,
    )


def validate_command(document: dict[str, Any]) -> None:
    validate_document(
        "https://living-companion.local/contracts/identity/v1/commands",
        document,
    )


def validate_error(document: dict[str, Any]) -> None:
    validate_document(
        "https://living-companion.local/contracts/identity/v1/errors",
        document,
    )
