from __future__ import annotations

import json
from pathlib import Path

import pytest

from backend.identity.memory_store import InMemoryIdentityRepository
from core.identity.clock import FrozenClock, SequenceIdGenerator
from core.identity.principal import Principal
from core.identity.service import ClientIdentityGateway, IdentityCommandService

FIXTURES = Path(__file__).resolve().parent / "fixtures"

TENANT_A = "11111111-1111-4111-8111-111111111111"
USER_A = "22222222-2222-4222-8222-222222222222"
TENANT_B = "33333333-3333-4333-8333-333333333333"
USER_B = "44444444-4444-4444-8444-444444444444"
COMPANION_A = "55555555-5555-4555-8555-555555555555"
COMPANION_B = "66666666-6666-4666-8666-666666666666"
NOW = "2026-01-15T12:00:00Z"


def load_json(name: str) -> dict:
    path = FIXTURES / name
    return json.loads(path.read_text(encoding="utf-8"))


def personality() -> dict:
    return {
        "personality_config_version": 1,
        "humor": 0.72,
        "empathy": 0.88,
        "curiosity": 0.91,
        "assertiveness": 0.63,
        "playfulness": 0.77,
        "formality": 0.21,
        "values": ["honesty", "kindness"],
        "interests": ["music", "walking"],
        "speech_style": "warm and concise",
        "boundaries": ["no medical advice", "no impersonation of real people"],
        "temperament": "calm",
    }


def configuration() -> dict:
    return {"configuration_version": 1, "declared_locale": "en-US"}


def create_payload(**overrides) -> dict:
    body = {
        "owner_user_id": USER_A,
        "display_name": "Mira Solenne",
        "age_presentation": "adult",
        "gender_presentation": "feminine",
        "personality": personality(),
        "configuration": configuration(),
        "metadata": {"source": "test", "notes": "Fictional Gate 1 reference Companion."},
    }
    body.update(overrides)
    return body


@pytest.fixture
def principal_a() -> Principal:
    return Principal(tenant_id=TENANT_A, user_id=USER_A, actor_id="actor-owner-a")


@pytest.fixture
def principal_b() -> Principal:
    return Principal(tenant_id=TENANT_B, user_id=USER_B, actor_id="actor-owner-b")


@pytest.fixture
def same_tenant_other_user() -> Principal:
    return Principal(
        tenant_id=TENANT_A,
        user_id="77777777-7777-4777-8777-777777777777",
        actor_id="actor-other",
    )


def make_service(ids: list[str] | None = None) -> tuple[IdentityCommandService, InMemoryIdentityRepository]:
    repo = InMemoryIdentityRepository()
    service = IdentityCommandService(
        repo,
        clock=FrozenClock(NOW),
        ids=SequenceIdGenerator(ids or [COMPANION_A, COMPANION_B]),
    )
    return service, repo


@pytest.fixture
def service() -> IdentityCommandService:
    svc, _ = make_service()
    return svc


@pytest.fixture
def client_a(service: IdentityCommandService, principal_a: Principal) -> ClientIdentityGateway:
    return ClientIdentityGateway(service, principal_a)


@pytest.fixture
def client_b_same_core(service: IdentityCommandService, principal_a: Principal) -> ClientIdentityGateway:
    return ClientIdentityGateway(service, principal_a)
