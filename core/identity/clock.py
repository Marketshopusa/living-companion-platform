"""Injectable clock and id generator."""

from __future__ import annotations

import uuid
from datetime import datetime, timezone


class SystemClock:
    def now_rfc3339(self) -> str:
        now = datetime.now(timezone.utc).replace(microsecond=0)
        return now.strftime("%Y-%m-%dT%H:%M:%SZ")


class FrozenClock:
    def __init__(self, timestamp: str) -> None:
        self._timestamp = timestamp

    def now_rfc3339(self) -> str:
        return self._timestamp


class Uuid4Generator:
    def new_uuid(self) -> str:
        return str(uuid.uuid4())


class SequenceIdGenerator:
    def __init__(self, values: list[str]) -> None:
        self._values = list(values)

    def new_uuid(self) -> str:
        if not self._values:
            raise RuntimeError("id generator exhausted")
        return self._values.pop(0)
