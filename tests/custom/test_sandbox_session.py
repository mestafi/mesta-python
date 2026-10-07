"""client.sandbox.get parses a complete sandbox as round 14 of the API sends it: fixtures.magicValues is a list
of {key, value, appliesTo, outcome, description} (contract sandbox-api-responses.md). Synthetic values only; the
response comes from an in-process transport, so nothing leaves the machine."""

import typing

import httpx

from mesta import Mesta, SandboxFixturesMagicValuesItem

SANDBOX_ID = "sbx_01EXAMPLE00000000000000000"

ROUND_14_SESSION: typing.Dict[str, typing.Any] = {
    "data": {
        "sandboxId": "sbx_01EXAMPLE00000000000000000",
        "merchantId": "00000000-0000-4000-8000-000000000001",
        "status": "unclaimed",
        "plane": "sandbox",
        "apiBaseUrl": "https://api.sandbox.mesta.xyz",
        "portalUrl": "https://ohana.sandbox.mesta.xyz",
        "createdAt": "2026-10-07T14:14:16.999Z",
        "expiresAt": "2026-10-14T14:14:16.999Z",
        "emailVerified": False,
        "executionPaused": False,
        "pauseMessage": None,
        "counts": {
            "accounts": 13,
            "senders": 4,
            "beneficiaries": 13,
            "orders": 17,
            "deposits": 11,
            "wallets": 0,
            "webhooks": 1,
        },
        "keys": [
            {
                "id": "00000000-0000-4000-8000-000000000002",
                "kind": "standard",
                "expiresAt": "2026-10-14T14:14:16.999Z",
                "lastUsedAt": "2026-10-07T14:14:17.477Z",
            }
        ],
        "seed": {
            "status": "complete",
            "step": None,
            "steps": [
                {"name": "merchant", "status": "done"},
                {"name": "keys", "status": "done"},
                {"name": "terms", "status": "done"},
                {"name": "merchant_setup", "status": "done"},
                {"name": "webhook", "status": "done"},
                {"name": "wallets", "status": "skipped"},
                {"name": "senders", "status": "done"},
                {"name": "deposits", "status": "done"},
                {"name": "beneficiaries", "status": "done"},
                {"name": "orders", "status": "done"},
                {"name": "fixtures", "status": "done"},
            ],
            "completedAt": "2026-10-07T14:14:38.463Z",
            "error": None,
        },
        "wallets": {
            "senders": {"used": 0, "cap": 5, "items": []},
            "status": "unavailable",
            "reason": "not_offered_on_plane",
        },
        "productionRequest": None,
        "fixtures": {
            "orders": [
                {"id": "00000000-0000-4000-8000-000000000010", "status": "created"},
                {"id": "00000000-0000-4000-8000-000000000011", "status": "success"},
            ],
            "senders": [{"id": "00000000-0000-4000-8000-000000000020", "label": "Example Sender"}],
            "version": "2026.10.1",
            "wallets": [],
            "webhook": {
                "id": "00000000-0000-4000-8000-000000000030",
                "url": "https://api.sandbox.mesta.xyz/v1/sandbox/sink/sbx_01EXAMPLE00000000000000000",
                "signingKey": "example-signing-key",
            },
            "balances": [{"owner": "00000000-0000-4000-8000-000000000020", "amount": "100000.00", "currency": "USD"}],
            "magicValues": [
                {
                    "key": "quote_source_amount_cents_99",
                    "value": ".99",
                    "outcome": ["order:failed"],
                    "appliesTo": "the cents of sourceAmount in POST /v1/quotes",
                    "description": "An order placed on a quote whose sourceAmount ends in .99 fails its payout.",
                },
                {
                    "key": "quote_source_amount_cents_77",
                    "value": ".77",
                    "outcome": ["order:success", "order:returned"],
                    "appliesTo": "the cents of sourceAmount in POST /v1/quotes",
                    "description": "An order placed on a quote whose sourceAmount ends in .77 is paid and then returned.",
                },
            ],
            "beneficiaries": [
                {
                    "id": "00000000-0000-4000-8000-000000000040",
                    "label": "Example Beneficiary",
                    "paymentMethodId": "00000000-0000-4000-8000-000000000041",
                }
            ],
            "depositSource": "sender",
        },
    },
    "requestId": 1,
}


def test_sandbox_get_parses_magic_values_list() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "GET"
        assert request.url.path == f"/v1/sandbox/sessions/{SANDBOX_ID}"
        return httpx.Response(200, json=ROUND_14_SESSION)

    client = Mesta(
        api_key="example",
        api_secret="example",
        base_url="https://example.invalid",
        httpx_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )
    response = client.sandbox.get(SANDBOX_ID)

    assert response.data.fixtures is not None
    magic_values = response.data.fixtures.magic_values
    assert all(isinstance(item, SandboxFixturesMagicValuesItem) for item in magic_values)
    assert [item.key for item in magic_values] == ["quote_source_amount_cents_99", "quote_source_amount_cents_77"]
    assert magic_values[0].applies_to == "the cents of sourceAmount in POST /v1/quotes"
    assert magic_values[1].outcome == ["order:success", "order:returned"]
    assert response.data.seed.steps[5].status == "skipped"
    assert response.data.wallets.status == "unavailable"
