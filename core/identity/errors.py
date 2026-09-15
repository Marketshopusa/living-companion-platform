"""Identity error codes matching contracts/identity/v1/errors.schema.json."""

from __future__ import annotations

from typing import Any


class IdentityError(Exception):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message

    def to_document(self) -> dict[str, Any]:
        return {"code": self.code, "message": self.message}
