# Reference
## Merchants
<details><summary><code>client.merchants.<a href="src/mesta/merchants/client.py">get</a>(...) -> GetMerchantsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves detailed information about a specific merchant, including account details and UBO (Ultimate Beneficial Owner) information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.get(
    merchant_id="merchantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` — Unique identifier of the merchant
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.<a href="src/mesta/merchants/client.py">accept_terms</a>(...) -> AcceptTermsMerchantsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Records the merchant's acceptance of Terms of Service. Captures acceptance timestamp, user identity, and IP address.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.accept_terms(
    merchant_id="merchantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` — ID of the merchant
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.<a href="src/mesta/merchants/client.py">get_balances</a>(...) -> GetBalancesMerchantsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the current balances for a merchant across all currencies and stablecoins.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.get_balances(
    merchant_id="merchantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` — Unique identifier of the merchant
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## WalletAddresses
<details><summary><code>client.wallet_addresses.<a href="src/mesta/wallet_addresses/client.py">get</a>(...) -> GetWalletAddressesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a single source wallet address by its unique identifier.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.wallet_addresses.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the source wallet address
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Senders
<details><summary><code>client.senders.<a href="src/mesta/senders/client.py">list</a>(...) -> ListSendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of all senders associated with a merchant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — Filter senders by specific ID
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListSendersRequestStatus]` — Filter senders by their verification status
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Records per page
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListSendersRequestSortBy]` — Sort column
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListSendersRequestSortOrder]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/mesta/senders/client.py">create_v1</a>(...) -> CreateV1SendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

## Overview
* Creates a new sender
* Supports both individual and business senders
* Requirements vary by country and ownerType

## Validation Rules
* **Important**: Always check validation rules before creating a sender
* Validation rules endpoint: `GET /v1/validation-rules/senders`
* Required query parameters:
   * `ownerType=[individual|business]`
  * `country=[ISO 3166-1 alpha-2 code]`
* Example request:
```
GET /v1/validation-rules/senders?ownerType=individual&country=MX
```
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta, Address, IndividualSenderIdentity
from mesta.environment import MestaEnvironment
from mesta.senders import CreateV1SendersRequest_Individual
import datetime

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.create_v1(
    request=CreateV1SendersRequest_Individual(
        first_name="firstName",
        last_name="lastName",
        birth_date=datetime.date.fromisoformat("2023-01-15"),
        email="email",
        phone="phone",
        addresses=[
            Address(
                street="street",
                city="city",
                postal_code="12345 or 00000",
                country="country",
            )
        ],
        identity=IndividualSenderIdentity(
            document_type="PASSPORT",
            country_code="countryCode",
            document_number="documentNumber",
        ),
        gender="male",
        occupation="accountant",
        type="individual",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateV1SendersRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/mesta/senders/client.py">create_v2</a>(...) -> CreateV2SendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

## Overview
* Creates a new sender
* Supports both individual and business senders
* Includes additional onboarding fields used for compliance review
* Requirements vary by country and ownerType

## Validation Rules
* **Important**: Always check validation rules before creating a sender
* Validation rules endpoint: `GET /v2/validation-rules/senders`
* Required query parameters:
   * `ownerType=[individual|business]`
  * `country=[ISO 3166-1 alpha-2 code]`
* Example request:
```
GET /v2/validation-rules/senders?ownerType=individual&country=MX
```

## Additional v2 Notes
* `expectedMonthlyVolumeEstimate`, `averageTransactionSize`, `primaryCounterpartyJurisdictions`, `natureOfPayments`, and `sourceOfFunds` are required for both sender types
* Each value in `primaryCounterpartyJurisdictions` must be an ISO 3166-1 alpha-2 country code (for example: `US`, `IN`, `GB`)
* `isFinancialInstitution` and `numberOfEmployees` are required for business senders
* `websiteAbsenceReason` is required for business senders when `websiteUrl` is not provided
* If `isFinancialInstitution` is `true`, upload the FI registration proof using `POST /v1/senders/{senderId}/documents` with document type `fi_registration_proof` before calling `POST /v1/senders/{senderId}/verify`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta, IndividualSenderV2, Address, IndividualSenderIdentity
from mesta.environment import MestaEnvironment
import datetime

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.create_v2(
    request=IndividualSenderV2(
        type="individual",
        first_name="firstName",
        last_name="lastName",
        birth_date=datetime.date.fromisoformat("2023-01-15"),
        email="email",
        phone="phone",
        addresses=[
            Address(
                street="street",
                city="city",
                postal_code="12345 or 00000",
                country="country",
            )
        ],
        identity=IndividualSenderIdentity(
            document_type="PASSPORT",
            country_code="countryCode",
            document_number="documentNumber",
        ),
        gender="male",
        occupation="accountant",
        expected_monthly_volume_estimate=1.1,
        average_transaction_size=1.1,
        primary_counterparty_jurisdictions=[
            "primaryCounterpartyJurisdictions"
        ],
        nature_of_payments=[
            "payroll"
        ],
        source_of_funds="advance_from_director",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateV2SendersRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/mesta/senders/client.py">get</a>(...) -> GetSendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves detailed information about a specific sender account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.get(
    sender_id="senderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` — Unique identifier for the sender.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/mesta/senders/client.py">delete</a>(...) -> DeleteSendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a sender account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.delete(
    sender_id="senderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` — Unique identifier for the sender.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/mesta/senders/client.py">update</a>(...) -> UpdateSendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing sender's information. Note that certain fields cannot be modified after initial creation:

- type (individual/business)
- identificationNumber (for business senders)
- taxIdentificationNumber (for business senders)

Before updating a sender, always check the validation rules using:
GET /v2/validation-rules/senders?ownerType=[individual|business]&country=[ISO 3166-1 alpha-2 code]
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta, PatchIndividualSender
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.update(
    sender_id="senderId",
    request=PatchIndividualSender(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` — Unique identifier for the sender.
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateSendersRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/mesta/senders/client.py">simulate_verification_result</a>(...) -> SimulateVerificationResultSendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Settles a pending sender verification with a simulated provider decision so you can drive onboarding end to end without waiting on the identity provider. Available in test environments only — disabled in production.

Verification must already have been started via the corresponding `/verify` call; otherwise the request is rejected with `MOCK_VERIFICATION_NOT_INITIATED`. For a business sender the same result is applied to the sender's KYB and to every UBO and unlinked associate on it, matching how the provider settles them individually.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.simulate_verification_result(
    sender_id="senderId",
    result="APPROVED",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` — Unique identifier for the sender.
    
</dd>
</dl>

<dl>
<dd>

**result:** `SimulateVerificationResultSendersRequestResult` — The verification outcome to simulate.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/mesta/senders/client.py">verify</a>(...) -> VerifySendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs the authoritative union of base sender, country-specific, accepted-capability, and persisted UBO/associate requirements, minus canonical data already stored. If no blockers remain, it initiates the existing verification process. If requirements are incomplete, verification does not start and the API returns actionable `CAPABILITY_REQUIREMENTS_MISSING` blockers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.verify(
    sender_id="senderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` — Unique identifier for the sender.
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `typing.Optional[int]` — Unique identifier for the Verify Sender request
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/mesta/senders/client.py">get_balances</a>(...) -> GetBalancesSendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the account balances for a specific sender across all supported currencies. Returns an array of currency-balance pairs for all currencies where the sender has an account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.get_balances(
    sender_id="senderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` — Unique identifier for the sender
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/mesta/senders/client.py">simulate_deposit</a>(...) -> SimulateDepositSendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Credits a sender's deposit account with simulated funds so you can test order flows end to end without moving real money.

**Available in test environments only.** This endpoint is disabled in production and returns `403 FORBIDDEN` there.

The credit is applied asynchronously: a successful call only confirms that the simulated deposit was accepted. The funds land once the banking provider's webhook is processed, which normally takes a few seconds. Poll `GET /v1/senders/{senderId}/balances` to confirm the balance has moved.

**Limits**

- `amount` must be greater than `0` and no more than `200` per request. Repeat the call to fund larger balances.
- Rate limited to 10 requests per 2 hours for this endpoint, counted per source IP address. Every rejected request also consumes quota, including `401`, `403`, `400` and `404` responses.
- Simulated deposits are only supported for deposit accounts held with a banking provider that offers a deposit simulator. Accounts on other providers return `MOCK_DEPOSIT_NOT_SUPPORTED_FOR_ACCOUNT`.

**Permissions**

The API key must carry the `merchant:sender:write` permission (`merchant:*:*` also matches). Without it the request is rejected with `403 FORBIDDEN`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.simulate_deposit(
    sender_id="senderId",
    amount=1.1,
    currency="USD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` — Unique identifier for the sender
    
</dd>
</dl>

<dl>
<dd>

**amount:** `float` — Amount to credit, in the deposit currency. Must be greater than 0 and no more than 200 per request.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Currency of the deposit account to credit, for example `USD`, `EUR`, `GBP` or `MXN`. The sender must already have a deposit account in this currency. Optional in the contract but effectively required in practice: always pass it explicitly, because omitting it can resolve a different deposit account than you intend and fail with `NO_DEPOSIT_BANK_ACCOUNT_FOUND`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.<a href="src/mesta/senders/client.py">generate_ledger_accounts</a>(...) -> GenerateLedgerAccountsSendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates ledger accounts and virtual bank accounts for a sender. These accounts are used for tracking balances and transactions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.generate_ledger_accounts(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the sender
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Beneficiaries
<details><summary><code>client.beneficiaries.<a href="src/mesta/beneficiaries/client.py">list_v1</a>(...) -> ListV1BeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of all beneficiaries associated with a merchant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.list_v1(
    merchant_id="xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — Filter beneficiaries by ID
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `typing.Optional[str]` — Identifier of the associated merchant
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListV1BeneficiariesRequestStatus]` — Filter beneficiaries by verification status
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — Field to sort the beneficiaries by
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListV1BeneficiariesRequestSortOrder]` — Sort order (ascending or descending)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.<a href="src/mesta/beneficiaries/client.py">create_v1</a>(...) -> CreateV1BeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

## Overview
* Creates a new beneficiary.
* Supports both individual and business beneficiaries
* Requirements vary by country and ownerType

## Validation Rules
* **Important**: Always check validation rules before creating a beneficiary
* Validation rules endpoint: `GET /v1/validation-rules/beneficiaries`
* Required query parameters:
  * `ownerType=[individual|business]`
  * `country=[ISO 3166-1 alpha-2 code]`
* Example request:
```
GET /v1/validation-rules/beneficiaries?ownerType=individual&country=PH
```

## Bank Information
* For US beneficiaries with paymentType=bank_account:
  * Routing number is required
  * Bank ID is not needed
* For non-US beneficiaries with paymentType=bank_account:
  * Bank ID is required
  * Fetch bank list using: `GET /v1/beneficiaries/banks`
  * Required query parameter: `countryCode=[ISO 3166-1 alpha-2 code]`
* Example request:
```
GET /v1/beneficiaries/banks?countryCode=PH
```
* Response includes bank ID and name:
```json
{
  "data": [
    {
      "id": "123",
      "name": "Sample Bank"
    }
  ]
}
```
* Use the `bankId` in the paymentInfo object when creating non-US beneficiaries with bank_account payment type
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta, IndividualBeneficiaryAddress, BankAccount
from mesta.environment import MestaEnvironment
from mesta.beneficiaries import CreateV1BeneficiariesRequest_Individual

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.create_v1(
    request=CreateV1BeneficiariesRequest_Individual(
        first_name="firstName",
        last_name="lastName",
        address=IndividualBeneficiaryAddress(
            street="street",
            city="city",
            postal_code="12345 or 00000",
            country="country",
        ),
        payment_type="bank_account",
        payment_info=BankAccount(
            account_number="accountNumber",
        ),
        type="individual",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateV1BeneficiariesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.<a href="src/mesta/beneficiaries/client.py">get_v1</a>(...) -> GetV1BeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves detailed information about a specific beneficiary account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.get_v1(
    beneficiary_id="beneficiaryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**beneficiary_id:** `str` — Unique identifier for the beneficiary.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.<a href="src/mesta/beneficiaries/client.py">delete</a>(...) -> DeleteBeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a beneficiary account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.delete(
    beneficiary_id="beneficiaryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**beneficiary_id:** `str` — Unique identifier for the beneficiary.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.<a href="src/mesta/beneficiaries/client.py">update_v1</a>(...) -> UpdateV1BeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing beneficiary's information. Note that certain fields cannot be modified after initial creation.

Non-updatable fields:
- type (individual/business)
- identificationNumber (for business beneficiaries)
- taxIdentificationNumber (for business beneficiaries)
- bankAccountType
- bankAccountNumber
- bankCode

Before updating a beneficiary, always check the validation rules using:
GET /v1/validation-rules/beneficiaries?ownerType=[individual|business]&country=[ISO 3166-1 alpha-2 code]
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta, IndividualBeneficiaryAddress, BankAccount
from mesta.environment import MestaEnvironment
from mesta.beneficiaries import UpdateV1BeneficiariesRequestBody_Individual

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.update_v1(
    beneficiary_id="beneficiaryId",
    request=UpdateV1BeneficiariesRequestBody_Individual(
        first_name="firstName",
        last_name="lastName",
        address=IndividualBeneficiaryAddress(
            street="street",
            city="city",
            postal_code="12345 or 00000",
            country="country",
        ),
        payment_type="bank_account",
        payment_info=BankAccount(
            account_number="accountNumber",
        ),
        type="individual",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**beneficiary_id:** `str` — Unique identifier for the beneficiary
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateV1BeneficiariesRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.<a href="src/mesta/beneficiaries/client.py">simulate_verification_result</a>(...) -> SimulateVerificationResultBeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Settles a pending beneficiary verification with a simulated provider decision so you can drive onboarding end to end without waiting on the identity provider. Available in test environments only — disabled in production.

Verification must already have been started via the corresponding `/verify` call; otherwise the request is rejected with `MOCK_VERIFICATION_NOT_INITIATED`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.simulate_verification_result(
    beneficiary_id="beneficiaryId",
    result="APPROVED",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**beneficiary_id:** `str` — Unique identifier for the beneficiary.
    
</dd>
</dl>

<dl>
<dd>

**result:** `SimulateVerificationResultBeneficiariesRequestResult` — The verification outcome to simulate.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.<a href="src/mesta/beneficiaries/client.py">verify</a>(...) -> VerifyBeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verifies a specific beneficiary account by initiating sanction/watchlist screenings.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.verify(
    beneficiary_id="beneficiaryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**beneficiary_id:** `str` — Unique identifier for the beneficiary.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.<a href="src/mesta/beneficiaries/client.py">lookup_bank</a>(...) -> LookupBankBeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of bank Ids for a specific country.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.lookup_bank(
    country_code="countryCode",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**country_code:** `str` — ISO 3166-1 alpha-2 country code
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.<a href="src/mesta/beneficiaries/client.py">list_v2</a>(...) -> ListV2BeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a paginated list of beneficiaries using the V2 API. Unlike v1, the v2 API separates payment methods from beneficiary data. Payment methods are available on the detail endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.list_v2()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number (zero-based)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListV2BeneficiariesRequestSortBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListV2BeneficiariesRequestSortOrder]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.<a href="src/mesta/beneficiaries/client.py">create_v2</a>(...) -> CreateV2BeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new beneficiary with payment methods in a single request. This v2 endpoint allows you to create a beneficiary and attach payment methods simultaneously.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment
from mesta.beneficiaries import CreateV2BeneficiariesRequestAddress, CreateV2BeneficiariesRequestPaymentMethodsItem

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.create_v2(
    type="individual",
    address=CreateV2BeneficiariesRequestAddress(
        street="123 Main St",
        city="Manila",
        postal_code="1000",
        country="PH",
    ),
    payment_methods=[
        CreateV2BeneficiariesRequestPaymentMethodsItem(
            type="bank_account",
            data={
                "key": "value"
            },
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `CreateV2BeneficiariesRequestType` — Type of beneficiary
    
</dd>
</dl>

<dl>
<dd>

**address:** `CreateV2BeneficiariesRequestAddress` — Beneficiary address
    
</dd>
</dl>

<dl>
<dd>

**payment_methods:** `typing.List[CreateV2BeneficiariesRequestPaymentMethodsItem]` — At least one payment method must be provided
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — First name (required for individual type)
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — Last name (required for individual type)
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[str]` — Middle name (optional, individual type only)
    
</dd>
</dl>

<dl>
<dd>

**full_name:** `typing.Optional[str]` — Full business name (required for business type)
    
</dd>
</dl>

<dl>
<dd>

**business_registration_number:** `typing.Optional[str]` — Business registration number (required for business type)
    
</dd>
</dl>

<dl>
<dd>

**business_type:** `typing.Optional[CreateV2BeneficiariesRequestBusinessType]` — Type of business (optional)
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Beneficiary email
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — Beneficiary phone number
    
</dd>
</dl>

<dl>
<dd>

**birth_date:** `typing.Optional[datetime.date]` — Date of birth (YYYY-MM-DD, individual type)
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `typing.Optional[str]` — Merchant ID (optional, auto-assigned from API key)
    
</dd>
</dl>

<dl>
<dd>

**identity:** `typing.Optional[CreateV2BeneficiariesRequestIdentity]` — Identity document details
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Custom metadata
    
</dd>
</dl>

<dl>
<dd>

**beneficiary_relationship:** `typing.Optional[BeneficiaryRelationship]` 
    
</dd>
</dl>

<dl>
<dd>

**purpose_of_payment:** `typing.Optional[PurposeOfPayment]` 
    
</dd>
</dl>

<dl>
<dd>

**purpose_of_payment_document:** `typing.Optional[PurposeOfPaymentDocumentRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.<a href="src/mesta/beneficiaries/client.py">get_v2</a>(...) -> GetV2BeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a single beneficiary by ID with their associated payment methods.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.get_v2(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Beneficiary ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.<a href="src/mesta/beneficiaries/client.py">update_v2</a>(...) -> UpdateV2BeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update a beneficiary. Only the provided fields will be updated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.update_v2(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Beneficiary ID
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[UpdateV2BeneficiariesRequestType]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**full_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**birth_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[UpdateV2BeneficiariesRequestAddress]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**beneficiary_relationship:** `typing.Optional[BeneficiaryRelationship]` 
    
</dd>
</dl>

<dl>
<dd>

**purpose_of_payment:** `typing.Optional[PurposeOfPayment]` 
    
</dd>
</dl>

<dl>
<dd>

**purpose_of_payment_document:** `typing.Optional[PurposeOfPaymentDocumentRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.<a href="src/mesta/beneficiaries/client.py">validate</a>(...) -> ValidateBeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates a beneficiary's information, checking that all required fields are present and correct for the beneficiary's country and payment method configuration.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.validate(
    beneficiary_id="beneficiaryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**beneficiary_id:** `str` — Unique identifier of the beneficiary
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.<a href="src/mesta/beneficiaries/client.py">update_verification</a>(...) -> UpdateVerificationBeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the verification status of a beneficiary. Used to mark a beneficiary as verified, pending, or declined after completing identity checks.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.update_verification(
    beneficiary_id="beneficiaryId",
    status="unverified",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**beneficiary_id:** `str` — Unique identifier of the beneficiary
    
</dd>
</dl>

<dl>
<dd>

**status:** `UpdateVerificationBeneficiariesRequestStatus` — New verification status for the beneficiary
    
</dd>
</dl>

<dl>
<dd>

**external_ref_id:** `typing.Optional[str]` — External reference ID for the verification
    
</dd>
</dl>

<dl>
<dd>

**verification_result:** `typing.Optional[typing.Dict[str, typing.Any]]` — Arbitrary JSON object containing verification result details
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.<a href="src/mesta/beneficiaries/client.py">create_v3</a>(...) -> CreateV3BeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new beneficiary with mandatory compliance fields. Same as V2 but `beneficiaryRelationship` and `purposeOfPayment` are required.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment
from mesta.beneficiaries import CreateV3BeneficiariesRequestAddress, CreateV3BeneficiariesRequestPaymentMethodsItem

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.create_v3(
    type="individual",
    address=CreateV3BeneficiariesRequestAddress(
        street="123 Main St",
        city="Manila",
        postal_code="1000",
        country="PH",
    ),
    payment_methods=[
        CreateV3BeneficiariesRequestPaymentMethodsItem(
            type="bank_account",
            data={
                "key": "value"
            },
        )
    ],
    beneficiary_relationship="business_partner",
    purpose_of_payment="payroll",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `CreateV3BeneficiariesRequestType` — Type of beneficiary
    
</dd>
</dl>

<dl>
<dd>

**address:** `CreateV3BeneficiariesRequestAddress` — Beneficiary address
    
</dd>
</dl>

<dl>
<dd>

**payment_methods:** `typing.List[CreateV3BeneficiariesRequestPaymentMethodsItem]` — At least one payment method must be provided
    
</dd>
</dl>

<dl>
<dd>

**beneficiary_relationship:** `BeneficiaryRelationship` 
    
</dd>
</dl>

<dl>
<dd>

**purpose_of_payment:** `PurposeOfPayment` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — First name (required for individual type)
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — Last name (required for individual type)
    
</dd>
</dl>

<dl>
<dd>

**middle_name:** `typing.Optional[str]` — Middle name (optional, individual type only)
    
</dd>
</dl>

<dl>
<dd>

**full_name:** `typing.Optional[str]` — Full business name (required for business type)
    
</dd>
</dl>

<dl>
<dd>

**business_registration_number:** `typing.Optional[str]` — Business registration number (required for business type)
    
</dd>
</dl>

<dl>
<dd>

**business_type:** `typing.Optional[CreateV3BeneficiariesRequestBusinessType]` — Type of business (optional)
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Beneficiary email
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — Beneficiary phone number
    
</dd>
</dl>

<dl>
<dd>

**birth_date:** `typing.Optional[datetime.date]` — Date of birth (YYYY-MM-DD, individual type)
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `typing.Optional[str]` — Merchant ID (optional, auto-assigned from API key)
    
</dd>
</dl>

<dl>
<dd>

**identity:** `typing.Optional[CreateV3BeneficiariesRequestIdentity]` — Identity document details
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Custom metadata
    
</dd>
</dl>

<dl>
<dd>

**purpose_of_payment_document:** `typing.Optional[PurposeOfPaymentDocumentRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Quotes
<details><summary><code>client.quotes.<a href="src/mesta/quotes/client.py">get</a>(...) -> GetQuotesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the details of a specific quote by its unique identifier (quoteId).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.quotes.get(
    quote_id="quoteId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**quote_id:** `str` — Unique identifier for the quote.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/mesta/quotes/client.py">list</a>(...) -> ListQuotesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a paginated list of quotes with optional filtering.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.quotes.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Records per page
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListQuotesRequestSortBy]` — Sort column
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListQuotesRequestSortOrder]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/mesta/quotes/client.py">create</a>(...) -> CreateQuotesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Obtain a quote for converting USD or USDC to another specified currency. For web3 merchants, sourceCurrency is required and must be a stable coin. For web2 merchants, sourceCurrency is optional and defaults to USD if omitted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.quotes.create(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CreateQuotesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Orders
<details><summary><code>client.orders.<a href="src/mesta/orders/client.py">list</a>(...) -> ListOrdersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of orders for the authenticated user, with optional filters to narrow down results based on status, date range, target currency, or other relevant criteria.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.orders.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `typing.Optional[str]` — Filter by order ID
    
</dd>
</dl>

<dl>
<dd>

**source_currency:** `typing.Optional[str]` — Filter by source currency
    
</dd>
</dl>

<dl>
<dd>

**accepted_gross_source_amount:** `typing.Optional[str]` — Filter by accepted gross source amount
    
</dd>
</dl>

<dl>
<dd>

**sender_id:** `typing.Optional[str]` — Filter by sender ID
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListOrdersRequestStatus]` — Filter by order status.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — Filter orders starting from this date (ISO8601 format).
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — Filter orders up to this date (ISO8601 format).
    
</dd>
</dl>

<dl>
<dd>

**target_currency:** `typing.Optional[str]` — Filter by target currency ISO code (e.g., "EUR", "GBP").
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Pagination page number.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of orders per page.
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — Field to sort the orders by (e.g., "creationDate", "amount").
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListOrdersRequestSortOrder]` — Sort order (ascending or descending).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/mesta/orders/client.py">create_v1</a>(...) -> CreateV1OrdersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates a order for converting and transferring USD or USDC to a specified target currency, using a previously obtained quote.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.orders.create_v1(
    accepted_quote_id="acceptedQuoteId",
    sender_id="senderId",
    beneficiary_id="beneficiaryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**accepted_quote_id:** `str` — Unique ID for the quote to use for this order.
    
</dd>
</dl>

<dl>
<dd>

**sender_id:** `str` — Unique identifier for the sender.
    
</dd>
</dl>

<dl>
<dd>

**beneficiary_id:** `str` — Unique identifier for the beneficiary.
    
</dd>
</dl>

<dl>
<dd>

**purpose:** `typing.Optional[Purpose]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Custom metadata to attach to the order
    
</dd>
</dl>

<dl>
<dd>

**source_of_funds:** `typing.Optional[SourceOfFunds]` 
    
</dd>
</dl>

<dl>
<dd>

**beneficiary_relationship:** `typing.Optional[BeneficiaryRelationship]` 
    
</dd>
</dl>

<dl>
<dd>

**documents:** `typing.Optional[typing.List[OrderDocumentInput]]` — Optional array of supporting documents
    
</dd>
</dl>

<dl>
<dd>

**customer_reference_id:** `typing.Optional[str]` — Your internal reference ID for this order
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/mesta/orders/client.py">get</a>(...) -> GetOrdersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves detailed information about a specific order, including its current status and progress.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.orders.get(
    order_id="orderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — Unique identifier for the order.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/mesta/orders/client.py">get_deposit_wallet_address</a>(...) -> GetDepositWalletAddressOrdersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the deposit wallet address for a specific order
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.orders.get_deposit_wallet_address(
    order_id="7f916142-a6ba-45ca-9d7e-ff6f93091efc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — The unique identifier of the order
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/mesta/orders/client.py">get_deposit_bank_account</a>(...) -> GetDepositBankAccountOrdersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the deposit bank account details for onramp orders. This endpoint provides bank account information where funds should be deposited to complete the order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.orders.get_deposit_bank_account(
    order_id="orderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — The unique identifier of the order
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/mesta/orders/client.py">cancel</a>(...) -> CancelOrdersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels an existing order. The order must be in a cancellable state.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.orders.cancel(
    order_id="orderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — Unique identifier for the order to cancel
    
</dd>
</dl>

<dl>
<dd>

**cancellation_remarks:** `typing.Optional[str]` — Optional remarks or reason for cancelling the order
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/mesta/orders/client.py">create_v2</a>(...) -> CreateV2OrdersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new order using a payment method ID. This is the recommended way to create orders. Requires an accepted quote, a sender, and a payment method.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.orders.create_v2(
    sender_id="550e8400-e29b-41d4-a716-446655440001",
    payment_method_id="550e8400-e29b-41d4-a716-446655440002",
    accepted_quote_id="550e8400-e29b-41d4-a716-446655440003",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` — ID of the sender initiating the order
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `str` — ID of the payment method to use for delivery
    
</dd>
</dl>

<dl>
<dd>

**accepted_quote_id:** `str` — ID of the accepted quote
    
</dd>
</dl>

<dl>
<dd>

**purpose:** `typing.Optional[Purpose]` — Purpose of payment for the order. Required if the beneficiary does not have a purpose of payment configured during onboarding.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Custom metadata to attach to the order
    
</dd>
</dl>

<dl>
<dd>

**beneficiary_relationship:** `typing.Optional[BeneficiaryRelationship]` — Beneficiary relationship for the order. Required if the beneficiary does not have a beneficiary relationship configured during onboarding.
    
</dd>
</dl>

<dl>
<dd>

**source_of_funds:** `typing.Optional[SourceOfFunds]` — Source of funds for the order. Required if the sender does not have a source of funds configured during onboarding.
    
</dd>
</dl>

<dl>
<dd>

**documents:** `typing.Optional[typing.List[OrderDocumentInput]]` — Supporting documents for the order. Required if the beneficiary does not have a purpose of payment document on file.
    
</dd>
</dl>

<dl>
<dd>

**customer_reference_id:** `typing.Optional[str]` — Your internal reference ID for this order
    
</dd>
</dl>

<dl>
<dd>

**senders_own_funds:** `typing.Optional[bool]` — Declaration that the funds belong to the sender.
    
</dd>
</dl>

<dl>
<dd>

**use_pooled_funds:** `typing.Optional[bool]` — Optional. When true, the order is funded from your pooled merchant account balance instead of the sender’s individual wallet. The order still belongs to the sender and the payout runs in the sender’s name — only the funding source changes. Supported for stablecoin-source orders. Pooled Merchant Accounts is available to select merchants only — please reach out to Mesta support to have it enabled for your account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/mesta/orders/client.py">list_events</a>(...) -> ListEventsOrdersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the event history for a specific order. Returns a chronological list of state transitions and their timestamps.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.orders.list_events(
    order_id="orderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — Order ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/mesta/webhooks/client.py">list</a>(...) -> ListWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of all registered webhooks for the calling client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.webhooks.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of webhooks per page
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListWebhooksRequestSortBy]` — Field to sort the webhooks by
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListWebhooksRequestSortOrder]` — Sort order (ascending or descending)
    
</dd>
</dl>

<dl>
<dd>

**event:** `typing.Optional[ListWebhooksRequestEvent]` — Filter webhooks by specific event type
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/mesta/webhooks/client.py">create</a>(...) -> CreateWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers a new webhook for a specific event.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.webhooks.create(
    events=[
        "order:*",
        "sender:kyb_approved",
        "fiat_deposit:settled"
    ],
    url="https://example.com/webhooks/mesta",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**events:** `typing.List[CreateWebhooksRequestEventsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL where events will be posted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/mesta/webhooks/client.py">get</a>(...) -> GetWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific webhook by its unique identifier.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.webhooks.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the webhook.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/mesta/webhooks/client.py">delete</a>(...) -> DeleteWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a registered webhook.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.webhooks.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the webhook to be deleted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/mesta/webhooks/client.py">update</a>(...) -> UpdateWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a registered webhook.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.webhooks.update(
    id="id",
    events=[
        "order:*"
    ],
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the webhook to be updated.
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.List[UpdateWebhooksRequestEventsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL where events will be posted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PaymentMethods
<details><summary><code>client.payment_methods.<a href="src/mesta/payment_methods/client.py">list</a>(...) -> ListPaymentMethodsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a paginated list of payment methods. Filter by beneficiary, type, or status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.payment_methods.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number (0-indexed)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of records per page
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListPaymentMethodsRequestSortBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListPaymentMethodsRequestSortOrder]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search query
    
</dd>
</dl>

<dl>
<dd>

**beneficiary_id:** `typing.Optional[str]` — Filter by beneficiary ID
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[PaymentMethodType]` — Filter by payment method type
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PaymentMethodStatus]` — Filter by status
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_methods.<a href="src/mesta/payment_methods/client.py">create</a>(...) -> CreatePaymentMethodsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new payment method for a beneficiary. The payment method type determines the required data fields.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta, BankAccountInfo
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.payment_methods.create(
    beneficiary_id="550e8400-e29b-41d4-a716-446655440001",
    type="bank_account",
    data=BankAccountInfo(
        account_number="1234567890",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**beneficiary_id:** `str` — ID of the beneficiary this payment method belongs to
    
</dd>
</dl>

<dl>
<dd>

**type:** `PaymentMethodType` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `CreatePaymentMethodRequestData` — Payment method data. Structure depends on the type field. See BankAccountInfo, PixInfo, InstapayInfo, etc.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Display label for the payment method
    
</dd>
</dl>

<dl>
<dd>

**requires_user_consent:** `typing.Optional[bool]` — Whether user consent is required before approval
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_methods.<a href="src/mesta/payment_methods/client.py">get</a>(...) -> GetPaymentMethodsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific payment method by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.payment_methods.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Payment method ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_methods.<a href="src/mesta/payment_methods/client.py">update</a>(...) -> UpdatePaymentMethodsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing payment method. All required fields must be provided.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta, BankAccountInfo
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.payment_methods.update(
    id="id",
    type="bank_account",
    data=BankAccountInfo(
        account_number="1234567890",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Payment method ID
    
</dd>
</dl>

<dl>
<dd>

**type:** `PaymentMethodType` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `UpdatePaymentMethodRequestData` — Payment method data. Structure depends on the type field.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Display label for the payment method
    
</dd>
</dl>

<dl>
<dd>

**requires_user_consent:** `typing.Optional[bool]` — Whether user consent is required before approval
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_methods.<a href="src/mesta/payment_methods/client.py">delete</a>(...) -> DeletePaymentMethodsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a payment method by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.payment_methods.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Payment method ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_methods.<a href="src/mesta/payment_methods/client.py">decide_consent</a>(...) -> DecideConsentPaymentMethodsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approve or decline a payment method that requires user consent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.payment_methods.decide_consent(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Payment method ID
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ConsentDecisionRequestStatus]` — The consent decision — either approve or decline the payment method
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ValidationRules
<details><summary><code>client.validation_rules.<a href="src/mesta/validation_rules/client.py">list_states</a>(...) -> ListStatesValidationRulesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of states/provinces for a given country code. Returns state codes in ISO 3166-2 format.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.validation_rules.list_states(
    country="US",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**country:** `str` — ISO 3166-1 alpha-2 country code
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Events
<details><summary><code>client.events.<a href="src/mesta/events/client.py">list</a>(...) -> ListEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a paginated list of external events. Filter by aggregate type, merchant, or event name.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.events.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number (0-indexed)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of records per page
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListEventsRequestSortBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListEventsRequestSortOrder]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**aggregate_type:** `typing.Optional[ListEventsRequestAggregateType]` — Filter by aggregate type
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `typing.Optional[str]` — Filter by merchant ID
    
</dd>
</dl>

<dl>
<dd>

**aggregate_id:** `typing.Optional[str]` — Filter by aggregate ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by event name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ApiKeys
<details><summary><code>client.api_keys.<a href="src/mesta/api_keys/client.py">list</a>(...) -> ListApiKeysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a paginated list of API keys for the merchant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.api_keys.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number (zero-based)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items per page
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListApiKeysRequestSortBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListApiKeysRequestSortOrder]` — Sort direction
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search filter
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `typing.Optional[str]` — Filter by merchant ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/mesta/api_keys/client.py">create</a>(...) -> CreateApiKeysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new API key for the merchant. The API secret is only returned in the creation response and cannot be retrieved later.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.api_keys.create(
    name="name",
    permissions=[
        "permissions"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Human-readable name for the API key
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.List[str]` — List of permissions to grant to this API key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/mesta/api_keys/client.py">get</a>(...) -> GetApiKeysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details of a specific API key by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.api_keys.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the API key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/mesta/api_keys/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes an API key. This action cannot be undone.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.api_keys.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the API key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.api_keys.<a href="src/mesta/api_keys/client.py">update</a>(...) -> UpdateApiKeysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the name and/or permissions of an existing API key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.api_keys.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the API key
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Updated name for the API key
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Optional[typing.List[str]]` — Updated list of permissions
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Transfers
<details><summary><code>client.transfers.<a href="src/mesta/transfers/client.py">create</a>(...) -> CreateTransfersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an internal transfer that moves funds between two verified senders belonging to your merchant account. Funds move on Mesta's internal ledger from the source sender's USD balance to the recipient sender's USD balance — no external payment rails are involved.

> 🚧 Limited availability — enabled on request only
>
> Internal transfers are **not enabled by default**. This capability is only enabled for select merchants and approved use cases. To discuss enabling internal transfers for your account, please reach out to our [Support Team](mailto:support@mesta.xyz).

**Flow**
1. Create an internal quote via `POST /v1/quotes` with `transferType: "internal"`, `sourceCurrency: "USD"` and `targetCurrency: "USD"`.
2. Call this endpoint with the quote id as `acceptedQuoteId` before the quote expires. A quote can fund at most one transfer.

Internal transfers are order-backed: the response is a standard order with `transferType: "internal"`, the transfer appears in `GET /v1/orders` and `GET /v1/orders/{orderId}`, and it emits the standard order webhook events. The lifecycle is `created` → `funds_received` → `success`.

**Requirements**
- Both senders must belong to your merchant account and be verified and active.
- Both senders must be enabled for internal transfers (USD).
- The source sender's USD balance must cover the quote's gross source amount (amount + fees).
- The source and recipient sender must be different (self-transfers are rejected).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.transfers.create(
    sender_id="877157e3-5433-4a17-b89e-92bb2709fc44",
    beneficiary_sender_id="3f1f8dcb-42a5-4c46-a41b-2f7f2f6a9f10",
    accepted_quote_id="ad0d23ef-8482-47a1-bb08-d2556f4347e5",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` — Identifier of the source sender whose USD balance funds the transfer
    
</dd>
</dl>

<dl>
<dd>

**beneficiary_sender_id:** `str` — Identifier of the recipient sender. Must belong to the same merchant and be different from senderId
    
</dd>
</dl>

<dl>
<dd>

**accepted_quote_id:** `str` — Identifier of the internal quote (created with transferType "internal") to execute. A quote can fund at most one transfer and must be used before it expires
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Beneficiaries Documents
<details><summary><code>client.beneficiaries.documents.<a href="src/mesta/beneficiaries/documents/client.py">get_presigned_url</a>(...) -> GetPresignedUrlDocumentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a pre-signed URL to download a beneficiary's uploaded document. The URL expires after 300 seconds.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.documents.get_presigned_url(
    beneficiary_id="beneficiaryId",
    document_id="documentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**beneficiary_id:** `str` — Unique identifier of the beneficiary
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` — Unique identifier of the document
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetPresignedUrlDocumentsRequestType]` — Type of document to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.beneficiaries.documents.<a href="src/mesta/beneficiaries/documents/client.py">get_purpose_of_payment_presigned_url</a>(...) -> GetPurposeOfPaymentPresignedUrlDocumentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a pre-signed URL for downloading the purpose of payment document attached to a beneficiary. The URL expires in 300 seconds.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.beneficiaries.documents.get_purpose_of_payment_presigned_url(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Beneficiary ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Merchants Withdrawals
<details><summary><code>client.merchants.withdrawals.<a href="src/mesta/merchants/withdrawals/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Paginated list of your withdrawals. Poll this or the by-id endpoint to track progress — there are no withdrawal webhooks today.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment
import datetime

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.withdrawals.list(
    sender_id="c715b301-9654-438a-8893-72c90c8ce467",
    created_from=datetime.datetime.fromisoformat("2026-08-01T00:00:00+00:00"),
    created_to=datetime.datetime.fromisoformat("2026-08-31T23:59:59+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number (0-indexed)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of records per page
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListWithdrawalsRequestStatus]` — Filter by status. `needs_reconciliation` means the outcome is not yet known — not that the withdrawal failed.
    
</dd>
</dl>

<dl>
<dd>

**chain:** `typing.Optional[ListWithdrawalsRequestChain]` — Filter by network
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[ListWithdrawalsRequestCurrency]` — Filter by currency
    
</dd>
</dl>

<dl>
<dd>

**sender_id:** `typing.Optional[str]` — Filter to one sender's withdrawals
    
</dd>
</dl>

<dl>
<dd>

**created_from:** `typing.Optional[datetime.datetime]` — Full ISO-8601 datetime WITH a timezone offset. A bare date is rejected rather than silently read in your local timezone.
    
</dd>
</dl>

<dl>
<dd>

**created_to:** `typing.Optional[datetime.datetime]` — Full ISO-8601 datetime WITH a timezone offset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.withdrawals.<a href="src/mesta/merchants/withdrawals/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Withdraw your own balance to the wallet you registered for that network.

The destination is NOT supplied in the request. It is resolved from your registered, verified withdrawal wallet for the network implied by `currency`, so there is no request shape that sends funds to an address you have not already registered and verified. Register wallets in the merchant portal — registration cannot be done over the API.

No fee is charged; Mesta absorbs the network fee.

Only one withdrawal may be in flight per network at a time.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.withdrawals.create(
    idempotency_key="3f2a1c40-9b7e-4d51-8a62-0c9d4e7b1f88",
    currency="USDC_ETH",
    amount="250.00",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**idempotency_key:** `str` — Client-generated UUID, one per withdrawal attempt. Resubmitting the same key returns the original withdrawal instead of creating a second one. Reuse it when retrying a request whose response you did not receive.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `CreateWithdrawalsRequestCurrency` — Determines the network, and therefore which registered wallet receives the funds.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `str` — Decimal STRING, at most 2 decimal places, greater than zero. Send a string, not a number — precision matters.
    
</dd>
</dl>

<dl>
<dd>

**sender_id:** `typing.Optional[str]` — The sender whose balance to withdraw. Omit and set `pooled: true` to withdraw from your pooled balance instead.
    
</dd>
</dl>

<dl>
<dd>

**pooled:** `typing.Optional[bool]` — Set true to withdraw from your pooled balance. Mutually exclusive with `senderId`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.withdrawals.<a href="src/mesta/merchants/withdrawals/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A single withdrawal. `txHash` is populated once the status is `completed`. `failureReason` carries one of `screening_rejected`, `insufficient_onchain_funds`, `send_failed` or `undecidable`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.withdrawals.get(
    id="b73e567f-71cc-49fa-ad13-e68e3ca57be4",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Withdrawal ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Merchants Accounts
<details><summary><code>client.merchants.accounts.<a href="src/mesta/merchants/accounts/client.py">list</a>(...) -> ListAccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the list of merchant accounts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.accounts.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Records per page
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListAccountsRequestSortBy]` — Sort column
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListAccountsRequestSortOrder]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Merchants StablecoinDeposits
<details><summary><code>client.merchants.stablecoin_deposits.<a href="src/mesta/merchants/stablecoin_deposits/client.py">list</a>(...) -> ListStablecoinDepositsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a paginated list of stablecoin deposits for a merchant. Supports filtering by currency, status, sender, and risk level.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.stablecoin_deposits.list(
    search="abc123",
    merchant_id="550e8400-e29b-41d4-a716-446655440000",
    sender_id="550e8400-e29b-41d4-a716-446655440001",
    source_wallet_address="0x1234567890abcdef1234567890abcdef12345678",
    deposit_wallet_address_id="550e8400-e29b-41d4-a716-446655440002",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number (0-indexed)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of records per page
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListStablecoinDepositsRequestSortBy]` — Sort column
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListStablecoinDepositsRequestSortOrder]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search query
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[ListStablecoinDepositsRequestCurrency]` — Filter by stablecoin currency
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `typing.Optional[str]` — Filter by merchant ID
    
</dd>
</dl>

<dl>
<dd>

**sender_id:** `typing.Optional[str]` — Filter by sender ID
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListStablecoinDepositsRequestStatus]` — Filter by deposit status
    
</dd>
</dl>

<dl>
<dd>

**swa_risk_level:** `typing.Optional[ListStablecoinDepositsRequestSwaRiskLevel]` — Filter by SWA risk level
    
</dd>
</dl>

<dl>
<dd>

**source_wallet_address:** `typing.Optional[str]` — Filter by source wallet address
    
</dd>
</dl>

<dl>
<dd>

**deposit_wallet_address_id:** `typing.Optional[str]` — Filter by deposit wallet address ID
    
</dd>
</dl>

<dl>
<dd>

**is_pooled:** `typing.Optional[bool]` — Optional. true returns only pooled merchant account deposits (merchant-level top-ups, no sender attribution); false returns only sender-attributed deposits; omit for all deposits. Pooled Merchant Accounts is available to select merchants only — please reach out to Mesta support to have it enabled for your account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.stablecoin_deposits.<a href="src/mesta/merchants/stablecoin_deposits/client.py">get</a>(...) -> GetStablecoinDepositsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific stablecoin deposit by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.stablecoin_deposits.get(
    id="550e8400-e29b-41d4-a716-446655440000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Stablecoin deposit ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Merchants FiatDeposits
<details><summary><code>client.merchants.fiat_deposits.<a href="src/mesta/merchants/fiat_deposits/client.py">list</a>(...) -> ListFiatDepositsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a paginated list of fiat deposits for a merchant. Only completed deposits are returned. Supports filtering by currency, sender, and deposit bank account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.fiat_deposits.list(
    search="abc123",
    merchant_id="550e8400-e29b-41d4-a716-446655440000",
    sender_id="550e8400-e29b-41d4-a716-446655440001",
    deposit_bank_account_id="550e8400-e29b-41d4-a716-446655440002",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number (0-indexed)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of records per page
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListFiatDepositsRequestSortBy]` — Sort column
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListFiatDepositsRequestSortOrder]` — Sort order
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search query
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[ListFiatDepositsRequestCurrency]` — Filter by fiat currency
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `typing.Optional[str]` — Filter by merchant ID
    
</dd>
</dl>

<dl>
<dd>

**sender_id:** `typing.Optional[str]` — Filter by sender ID
    
</dd>
</dl>

<dl>
<dd>

**deposit_bank_account_id:** `typing.Optional[str]` — Filter by deposit bank account ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.fiat_deposits.<a href="src/mesta/merchants/fiat_deposits/client.py">get</a>(...) -> GetFiatDepositsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific fiat deposit by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.fiat_deposits.get(
    id="550e8400-e29b-41d4-a716-446655440000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Fiat deposit ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Merchants SourceWalletAddresses
<details><summary><code>client.merchants.source_wallet_addresses.<a href="src/mesta/merchants/source_wallet_addresses/client.py">list</a>(...) -> ListSourceWalletAddressesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all source wallet addresses for a specific merchant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.source_wallet_addresses.list(
    merchant_id="merchantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` — ID of the merchant
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.source_wallet_addresses.<a href="src/mesta/merchants/source_wallet_addresses/client.py">create</a>(...) -> CreateSourceWalletAddressesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates source wallet addresses for a merchant. Accepts an array of addresses.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta, SourceAddressInput
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.source_wallet_addresses.create(
    merchant_id="merchantId",
    request=[
        SourceAddressInput(
            address="address",
            chain="chain",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` — ID of the merchant
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[SourceAddressInput]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.source_wallet_addresses.<a href="src/mesta/merchants/source_wallet_addresses/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a specific source wallet address for a merchant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.source_wallet_addresses.delete(
    merchant_id="merchantId",
    source_wallet_address_id="sourceWalletAddressId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` — ID of the merchant
    
</dd>
</dl>

<dl>
<dd>

**source_wallet_address_id:** `str` — ID of the source wallet address to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Merchants DepositWalletAddresses
<details><summary><code>client.merchants.deposit_wallet_addresses.<a href="src/mesta/merchants/deposit_wallet_addresses/client.py">generate</a>(...) -> GenerateDepositWalletAddressesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates deposit wallet addresses across supported blockchain networks for a merchant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.deposit_wallet_addresses.generate(
    merchant_id="merchantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` — Unique identifier of the merchant
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.deposit_wallet_addresses.<a href="src/mesta/merchants/deposit_wallet_addresses/client.py">confirm</a>(...) -> ConfirmDepositWalletAddressesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Confirms and finalizes the deposit wallet addresses for a merchant. This should be called after generate-deposit-wallet-addresses to complete the setup process.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.merchants.deposit_wallet_addresses.confirm(
    merchant_id="merchantId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**merchant_id:** `str` — Unique identifier of the merchant
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Orders Documents
<details><summary><code>client.orders.documents.<a href="src/mesta/orders/documents/client.py">get_presigned_url</a>(...) -> GetPresignedUrlDocumentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a temporary presigned URL for downloading an order document. The URL expires after 5 minutes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.orders.documents.get_presigned_url(
    order_id="orderId",
    document_id="documentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` — ID of the order
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` — ID of the document
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Senders Associates
<details><summary><code>client.senders.associates.<a href="src/mesta/senders/associates/client.py">list</a>(...) -> SenderAssociateListEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the Directors and Authorized Representatives belonging to the specified sender.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.associates.list(
    sender_id="senderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.associates.<a href="src/mesta/senders/associates/client.py">create</a>(...) -> SenderAssociateEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a Director or Authorized Representative to a business sender. Use linkedUboId when the representative is the same person as an existing UBO; otherwise provide the person's own personal, address, identity, nationality, and document data.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.associates.create(
    sender_id="7e701fe5-d47b-4e44-b624-c48204cfead1",
    roles=[
        "director"
    ],
    linked_ubo_id="c4de346d-7972-4139-b132-974eca8b0606",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.List[SenderAssociateRole]` 
    
</dd>
</dl>

<dl>
<dd>

**linked_ubo_id:** `typing.Optional[str]` — Existing UBO representing the same person. Linked representatives reuse the UBO's stored data and verification session.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**birth_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[SenderAssociateAddress]` 
    
</dd>
</dl>

<dl>
<dd>

**nationality:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**identity:** `typing.Optional[SenderAssociateIdentityInput]` 
    
</dd>
</dl>

<dl>
<dd>

**pep_declaration:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**pep_questionnaire:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**sof_document:** `typing.Optional[str]` — Base64 encoded source-of-funds document.
    
</dd>
</dl>

<dl>
<dd>

**verification_report:** `typing.Optional[str]` — Base64 encoded verification report.
    
</dd>
</dl>

<dl>
<dd>

**verification_report_file_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.associates.<a href="src/mesta/senders/associates/client.py">get</a>(...) -> SenderAssociateEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one Director or Authorized Representative.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.associates.get(
    associate_id="associateId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**associate_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.associates.<a href="src/mesta/senders/associates/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the representative. An approved unlinked representative cannot be deleted; a linked representative uses the UBO's verification outcome.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.associates.delete(
    associate_id="associateId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**associate_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.associates.<a href="src/mesta/senders/associates/client.py">update</a>(...) -> SenderAssociateEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a Director or Authorized Representative. linkedUboId cannot be newly assigned or changed after creation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.associates.update(
    associate_id="associateId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**associate_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.List[SenderAssociateRole]]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**birth_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[PatchSenderAssociateAddress]` 
    
</dd>
</dl>

<dl>
<dd>

**nationality:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**identity:** `typing.Optional[PatchSenderAssociateIdentity]` 
    
</dd>
</dl>

<dl>
<dd>

**pep_declaration:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**pep_questionnaire:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**sof_document:** `typing.Optional[str]` — Base64 encoded source-of-funds document.
    
</dd>
</dl>

<dl>
<dd>

**verification_report:** `typing.Optional[str]` — Base64 encoded verification report.
    
</dd>
</dl>

<dl>
<dd>

**verification_report_file_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.associates.<a href="src/mesta/senders/associates/client.py">get_verification_url</a>(...) -> AssociateSelfieVerificationEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the latest selfie-verification session for an unlinked Director or Authorized Representative. Omit action to read the current session, use GENERATE only when no session exists, and use REGENERATE only when the latest session is DECLINED or EXPIRED. A representative linked through linkedUboId reuses the UBO verification session and must use the UBO verification endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.associates.get_verification_url(
    associate_id="associateId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**associate_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `typing.Optional[GetVerificationUrlAssociatesRequestAction]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Senders VirtualBankAccounts
<details><summary><code>client.senders.virtual_bank_accounts.<a href="src/mesta/senders/virtual_bank_accounts/client.py">get_setup_status</a>(...) -> VirtualAccountSetupEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the sender's current virtual bank account status for the currency. No request ID is required. This read can reconcile status but cannot start account setup. The endpoint follows the sender's current account configuration; if Mesta changes that configuration, a request associated with the previous configuration is no longer returned and the merchant should POST again for the current configuration.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.virtual_bank_accounts.get_setup_status(
    sender_id="senderId",
    currency="USD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `GetSetupStatusVirtualBankAccountsRequestCurrency` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.virtual_bank_accounts.<a href="src/mesta/senders/virtual_bank_accounts/client.py">request_setup</a>(...) -> VirtualAccountSetupEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or reuses the current virtual bank account request for this sender and currency. It is evaluated immediately and may begin setup automatically when all requirements are satisfied. Follow returned blocker actions when more information or verification is needed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.virtual_bank_accounts.request_setup(
    sender_id="senderId",
    currency="USD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `RequestSetupVirtualBankAccountsRequestCurrency` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.virtual_bank_accounts.<a href="src/mesta/senders/virtual_bank_accounts/client.py">cancel_setup</a>(...) -> VirtualAccountSetupEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels the current request before account setup begins or after failure. Provisioning and completed requests cannot be cancelled. A later POST creates a fresh current request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.virtual_bank_accounts.cancel_setup(
    sender_id="senderId",
    currency="USD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `CancelSetupVirtualBankAccountsRequestCurrency` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.virtual_bank_accounts.<a href="src/mesta/senders/virtual_bank_accounts/client.py">update_setup_data</a>(...) -> VirtualAccountSetupEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fills supported missing sender, UBO, or existing-representative values, then re-evaluates the current setup request. Fields that are not current blockers are skipped and identified in unacceptedFields; other submitted fields are still processed. Existing values cannot be overwritten. To reuse the registered address as the trading address, set senderDetails.tradingAddressSameAsRegistered to true. If a manual tradingAddress is also supplied, the reuse flag takes precedence. Documents and new representatives use their dedicated APIs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment
from mesta.senders.virtual_bank_accounts import UpdateVirtualAccountSetupDataSenderDetails, UpdateVirtualAccountSetupDataUboDetailsItem, UpdateVirtualAccountSetupDataAssociateDetailsItem
import datetime

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.virtual_bank_accounts.update_setup_data(
    sender_id="senderId",
    currency="USD",
    sender_details=UpdateVirtualAccountSetupDataSenderDetails(
        website_url="https://example.com",
        trading_address_same_as_registered=True,
    ),
    ubo_details=[
        UpdateVirtualAccountSetupDataUboDetailsItem(
            ubo_id="c4de346d-7972-4139-b132-974eca8b0606",
            birth_date=datetime.date.fromisoformat("1990-01-01"),
            nationality="GB",
        )
    ],
    associate_details=[
        UpdateVirtualAccountSetupDataAssociateDetailsItem(
            associate_id="a5de346d-7972-4139-b132-974eca8b0606",
            nationality="GB",
            birth_date=datetime.date.fromisoformat("1985-01-01"),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `UpdateSetupDataVirtualBankAccountsRequestCurrency` 
    
</dd>
</dl>

<dl>
<dd>

**sender_details:** `typing.Optional[UpdateVirtualAccountSetupDataSenderDetails]` — Previously absent business-sender details required by the requested account.
    
</dd>
</dl>

<dl>
<dd>

**ubo_details:** `typing.Optional[typing.List[UpdateVirtualAccountSetupDataUboDetailsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**associate_details:** `typing.Optional[typing.List[UpdateVirtualAccountSetupDataAssociateDetailsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.virtual_bank_accounts.<a href="src/mesta/senders/virtual_bank_accounts/client.py">get</a>(...) -> SenderVirtualAccountsEnvelope</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the virtual bank accounts available to the sender for the requested currency. The response is an array and currently contains at most one account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.virtual_bank_accounts.get(
    sender_id="senderId",
    currency="USD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `GetVirtualBankAccountsRequestCurrency` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Senders SourceWalletAddresses
<details><summary><code>client.senders.source_wallet_addresses.<a href="src/mesta/senders/source_wallet_addresses/client.py">list</a>(...) -> ListSourceWalletAddressesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all source wallet addresses for a specific sender. Supports pagination, sorting, and search.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.source_wallet_addresses.list(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the sender
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number (0-indexed)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of records per page
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[ListSourceWalletAddressesRequestSortBy]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[ListSourceWalletAddressesRequestSortOrder]` — Sort direction
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search query to filter results
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.source_wallet_addresses.<a href="src/mesta/senders/source_wallet_addresses/client.py">create</a>(...) -> CreateSourceWalletAddressesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates new source addresses for a specific sender. Multiple addresses can be created in a single request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta, SourceAddressInput
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.source_wallet_addresses.create(
    id="id",
    request=[
        SourceAddressInput(
            address="address",
            chain="chain",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the sender
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.List[SourceAddressInput]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.source_wallet_addresses.<a href="src/mesta/senders/source_wallet_addresses/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a specific source wallet address for a sender.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.source_wallet_addresses.delete(
    id="id",
    source_wallet_address_id="sourceWalletAddressId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the sender
    
</dd>
</dl>

<dl>
<dd>

**source_wallet_address_id:** `str` — ID of the source wallet address to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Senders Ubos
<details><summary><code>client.senders.ubos.<a href="src/mesta/senders/ubos/client.py">create_v1</a>(...) -> CreateV1UbosResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new UBO (Ultimate Beneficial Owner) for a specific sender.  Note: Document requirements (documentFront, documentBack) vary by country. Please refer to the validation-rules endpoint with ownerType='business' and the specific country to determine exact documentation requirements. Multiple UBOs can be added by calling this endpoint multiple times. The total ownership percentage across all UBOs should not exceed 100%.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment
import datetime
from mesta.senders.ubos import CreateV1UbosRequestAddress, CreateV1UbosRequestIdentity

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.ubos.create_v1(
    first_name="firstName",
    last_name="lastName",
    birth_date=datetime.date.fromisoformat("2023-01-15"),
    phone="phone",
    email="email",
    ownership_percent=1.1,
    address=CreateV1UbosRequestAddress(
        street="street",
        city="city",
        postal_code="12345 or 00000",
        country="country",
    ),
    sender_id="senderId",
    identity=CreateV1UbosRequestIdentity(
        document_type="PASSPORT",
        country_code="countryCode",
        document_number="documentNumber",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**first_name:** `str` — First name of the UBO (Ultimate Beneficial Owner).
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `str` — Last name of the UBO (Ultimate Beneficial Owner).
    
</dd>
</dl>

<dl>
<dd>

**birth_date:** `datetime.date` — Birthdate of the UBO (Ultimate Beneficial Owner) in the format yyyy-mm-dd.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `str` — Phone number of the UBO (Ultimate Beneficial Owner) in international format (e.g., +11234567890).
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Email address of the UBO (Ultimate Beneficial Owner).
    
</dd>
</dl>

<dl>
<dd>

**ownership_percent:** `float` — Ownership percentage of the UBO in the company
    
</dd>
</dl>

<dl>
<dd>

**address:** `CreateV1UbosRequestAddress` — UBO postal address.
    
</dd>
</dl>

<dl>
<dd>

**sender_id:** `str` — Unique identifier for the sender.
    
</dd>
</dl>

<dl>
<dd>

**identity:** `CreateV1UbosRequestIdentity` — Ultimate Beneficial Owner information. Note: Document requirements (documentFront, documentBack) vary by country. Please refer to the validation-rules endpoint with ownerType='ubo' and the specific country to determine exact documentation requirements.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.ubos.<a href="src/mesta/senders/ubos/client.py">create_v2</a>(...) -> CreateV2UbosResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new UBO (Ultimate Beneficial Owner) for a specific sender. Note: Document requirements (documentFront, documentBack) vary by country. Please refer to the validation-rules endpoint with ownerType='business' and the specific country to determine exact documentation requirements. Multiple UBOs can be added by calling this endpoint multiple times. The total ownership percentage across all UBOs should not exceed 100%.

Additional v2 details:
* `pepDeclaration` is required.
* `verificationReport` and `verificationReportFileName` are supported.
* The total request payload size must be less than 10 MB.
* `sofDocument` is required when any of the following is true:
  * UBO age is less than 25
  * UBO age is greater than 60
  * `pepDeclaration` is `true`
  * `address.country` is one of: `DZ`, `AO`, `BO`, `BG`, `BF`, `CM`, `CI`, `ET`, `HT`, `IQ`, `KE`, `LA`, `LB`, `ML`, `MC`, `MZ`, `NA`, `NP`, `NI`, `NG`, `SO`, `SY`, `VN`, `VG`, `YE`
  * `identity.countryCode` is one of: `DZ`, `AO`, `BO`, `BG`, `BF`, `CM`, `CI`, `ET`, `HT`, `IQ`, `KE`, `LA`, `LB`, `ML`, `MC`, `MZ`, `NA`, `NP`, `NI`, `NG`, `SO`, `SY`, `VN`, `VG`, `YE`
* `pepQuestionnaire` is supported. It is required when `pepDeclaration` is `true`.
* `pepQuestionnaire.declarationType` controls which section is required: `self` (for `SELF`) or `association` (for `IMMEDIATE_FAMILY` and `CLOSE_ASSOCIATE`).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment
import datetime
from mesta.senders.ubos import CreateV2UbosRequestAddress, CreateV2UbosRequestIdentity

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.ubos.create_v2(
    first_name="firstName",
    last_name="lastName",
    birth_date=datetime.date.fromisoformat("2023-01-15"),
    phone="phone",
    email="email",
    ownership_percent=1.1,
    address=CreateV2UbosRequestAddress(
        street="street",
        city="city",
        postal_code="postalCode",
        country="country",
    ),
    sender_id="senderId",
    identity=CreateV2UbosRequestIdentity(
        document_type="PASSPORT",
        country_code="countryCode",
        document_number="documentNumber",
    ),
    pep_declaration=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**first_name:** `str` — First name of the UBO.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `str` — Last name of the UBO.
    
</dd>
</dl>

<dl>
<dd>

**birth_date:** `datetime.date` — Birthdate of the UBO in the format YYYY-MM-DD.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `str` — Phone number of the UBO in international format (for example, +11234567890).
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Email address of the UBO.
    
</dd>
</dl>

<dl>
<dd>

**ownership_percent:** `float` — Ownership percentage of the UBO in the company.
    
</dd>
</dl>

<dl>
<dd>

**address:** `CreateV2UbosRequestAddress` — UBO postal address.
    
</dd>
</dl>

<dl>
<dd>

**sender_id:** `str` — Unique identifier for the sender.
    
</dd>
</dl>

<dl>
<dd>

**identity:** `CreateV2UbosRequestIdentity` — Identity information for the UBO.
    
</dd>
</dl>

<dl>
<dd>

**pep_declaration:** `bool` — Whether the UBO is politically exposed. This field is required.
    
</dd>
</dl>

<dl>
<dd>

**nationality:** `typing.Optional[str]` — UBO nationality as an ISO 3166-1 alpha-2 country code. This is distinct from residence and identity-document country.
    
</dd>
</dl>

<dl>
<dd>

**identification_number:** `typing.Optional[str]` — Tax identification number for the UBO. Required for a non-US UBO when `usd_account` is requested.
    
</dd>
</dl>

<dl>
<dd>

**verification_report:** `typing.Optional[str]` — Optional base64 encoded verification report document.
    
</dd>
</dl>

<dl>
<dd>

**verification_report_file_name:** `typing.Optional[str]` — Optional file name for the verification report.
    
</dd>
</dl>

<dl>
<dd>

**sof_document:** `typing.Optional[str]` — Base64 encoded source-of-funds document. Required when the UBO is younger than 25 or older than 60, when `pepDeclaration` is `true`, or when either `address.country` or `identity.countryCode` is one of: `DZ`, `AO`, `BO`, `BG`, `BF`, `CM`, `CI`, `ET`, `HT`, `IQ`, `KE`, `LA`, `LB`, `ML`, `MC`, `MZ`, `NA`, `NP`, `NI`, `NG`, `SO`, `SY`, `VN`, `VG`, `YE`.
    
</dd>
</dl>

<dl>
<dd>

**pep_questionnaire:** `typing.Optional[CreateV2UbosRequestPepQuestionnaire]` — Required when `pepDeclaration` is true. Contains declarationType with conditional `self` or `association` sections.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.ubos.<a href="src/mesta/senders/ubos/client.py">get</a>(...) -> GetUbosResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details of a specific Ultimate Beneficial Owner (UBO)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.ubos.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the UBO
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.ubos.<a href="src/mesta/senders/ubos/client.py">delete</a>(...) -> DeleteUbosResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing UBO (Ultimate Beneficial Owner)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.ubos.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the UBO
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.ubos.<a href="src/mesta/senders/ubos/client.py">update</a>(...) -> UpdateUbosResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing Ultimate Beneficial Owner (UBO). In addition to the base UBO fields, this endpoint supports `pepDeclaration`, `verificationReport`, and `sofDocument`. `sofDocument` is required when the UBO is younger than 25 or older than 60, when `pepDeclaration` is `true`, or when either `address.country` or `identity.countryCode` is one of: `DZ`, `AO`, `BO`, `BG`, `BF`, `CM`, `CI`, `ET`, `HT`, `IQ`, `KE`, `LA`, `LB`, `ML`, `MC`, `MZ`, `NA`, `NP`, `NI`, `NG`, `SO`, `SY`, `VN`, `VG`, `YE`. `pepQuestionnaire` is supported. When `pepDeclaration` is `true`, include `pepQuestionnaire` with `declarationType` and the matching conditional section (`self` or `association`).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.ubos.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the UBO
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — First name of the UBO
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — Last name of the UBO
    
</dd>
</dl>

<dl>
<dd>

**birth_date:** `typing.Optional[datetime.date]` — Birth date of the UBO
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Email address of the UBO
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — Phone number of the UBO in international format (e.g., +11234567890)
    
</dd>
</dl>

<dl>
<dd>

**nationality:** `typing.Optional[str]` — UBO nationality as an ISO 3166-1 alpha-2 country code. This is distinct from residence and identity-document country.
    
</dd>
</dl>

<dl>
<dd>

**identification_number:** `typing.Optional[str]` — Tax identification number for the UBO. Required for a non-US UBO when `usd_account` is requested.
    
</dd>
</dl>

<dl>
<dd>

**ownership_percent:** `typing.Optional[float]` — Percentage of the sender owned by this UBO.
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[Address]` 
    
</dd>
</dl>

<dl>
<dd>

**identity:** `typing.Optional[UpdateUbosRequestIdentity]` 
    
</dd>
</dl>

<dl>
<dd>

**verification_report:** `typing.Optional[str]` — Optional base64 encoded verification report document.
    
</dd>
</dl>

<dl>
<dd>

**verification_report_file_name:** `typing.Optional[str]` — Optional file name for the verification report.
    
</dd>
</dl>

<dl>
<dd>

**pep_declaration:** `typing.Optional[bool]` — Whether the UBO is politically exposed.
    
</dd>
</dl>

<dl>
<dd>

**sof_document:** `typing.Optional[str]` — Base64 encoded source-of-funds document. Required when the UBO is younger than 25 or older than 60, when `pepDeclaration` is `true`, or when either `address.country` or `identity.countryCode` is one of: `DZ`, `AO`, `BO`, `BG`, `BF`, `CM`, `CI`, `ET`, `HT`, `IQ`, `KE`, `LA`, `LB`, `ML`, `MC`, `MZ`, `NA`, `NP`, `NI`, `NG`, `SO`, `SY`, `VN`, `VG`, `YE`.
    
</dd>
</dl>

<dl>
<dd>

**pep_questionnaire:** `typing.Optional[UpdateUbosRequestPepQuestionnaire]` — Required when `pepDeclaration` is true. Contains declarationType with conditional `self` or `association` sections.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.ubos.<a href="src/mesta/senders/ubos/client.py">get_verification_url</a>(...) -> GetVerificationUrlUbosResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches the latest selfie verification session for a UBO and, optionally, generates or regenerates a verification link.

Action behavior:
* no `action`: return the current verification-session state without creating a new link.
* `GENERATE`: create the first verification link only when no previous selfie session exists.
* `REGENERATE`: create a fresh verification link only when the latest session is `DECLINED` or `EXPIRED`.

Response behavior:
* `latestSession`: the most recent selfie verification session, or `null` if none exists.
* `previousSessions`: older selfie verification sessions in reverse chronological order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.ubos.get_verification_url(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the UBO
    
</dd>
</dl>

<dl>
<dd>

**action:** `typing.Optional[GetVerificationUrlUbosRequestAction]` — Optional action for selfie-link creation. Omit it to fetch the current session state only. Use `GENERATE` to create the first link when no session exists. Use `REGENERATE` only when the latest session is `DECLINED` or `EXPIRED`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Senders Documents
<details><summary><code>client.senders.documents.<a href="src/mesta/senders/documents/client.py">upload</a>(...) -> UploadDocumentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads one Base64-encoded document for a specific sender. Use type `directors_registry` for a Directors' and shareholders' registry. Multiple registry files are supported by calling this endpoint once per file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.documents.upload(
    sender_id="senderId",
    file_name="fileName",
    type="",
    blob="blob",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` — Unique identifier for the sender
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` — The name of the file.
    
</dd>
</dl>

<dl>
<dd>

**type:** `UploadDocumentsRequestType` — The document type. Use directors_registry for each Directors' and shareholders' registry file.
    
</dd>
</dl>

<dl>
<dd>

**blob:** `str` — Base64 encoded document content.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.documents.<a href="src/mesta/senders/documents/client.py">delete</a>(...) -> DeleteDocumentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a specific document associated with a sender.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.documents.delete(
    sender_id="senderId",
    document_id="documentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` — Unique identifier for the sender
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` — Unique identifier for the document to be deleted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.documents.<a href="src/mesta/senders/documents/client.py">get_presigned_url</a>(...) -> GetPresignedUrlDocumentsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a temporary presigned URL for downloading a sender document. The URL expires after 5 minutes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.documents.get_presigned_url(
    id="id",
    document_id="documentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the sender
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` — ID of the document
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetPresignedUrlDocumentsRequestType]` — Type of document to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Senders TermsOfService
<details><summary><code>client.senders.terms_of_service.<a href="src/mesta/senders/terms_of_service/client.py">get_status</a>(...) -> GetStatusTermsOfServiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the current Terms of Service acceptance status for a specific sender, along with the active shareable acceptance link. In the current sender flow, a TOS acceptance link is generated during sender creation. Use this endpoint to check whether the sender has accepted the TOS, retrieve the active acceptance link, and verify whether the link has expired.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.terms_of_service.get_status(
    sender_id="senderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sender_id:** `str` — Unique identifier for the sender
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.terms_of_service.<a href="src/mesta/senders/terms_of_service/client.py">create_link</a>(...) -> CreateLinkTermsOfServiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a Terms of Service acceptance link for a sender. If a valid link already exists and regenerate is not set to true, returns the existing link.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.terms_of_service.create_link(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the sender
    
</dd>
</dl>

<dl>
<dd>

**regenerate:** `typing.Optional[bool]` — When true, forces generation of a new TOS link even if one already exists
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.terms_of_service.<a href="src/mesta/senders/terms_of_service/client.py">get_acceptance</a>(...) -> GetAcceptanceTermsOfServiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the Terms of Service acceptance details for a given token. This is a public endpoint that does not require authentication.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.terms_of_service.get_acceptance(
    token="token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `str` — TOS acceptance token (base64url encoded)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.terms_of_service.<a href="src/mesta/senders/terms_of_service/client.py">accept</a>(...) -> AcceptTermsOfServiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Accepts the Terms of Service on behalf of a sender using the provided token. This is a public endpoint that does not require authentication. The client's IP address and user agent are recorded automatically.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.terms_of_service.accept(
    token="token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `str` — TOS acceptance token (base64url encoded)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Senders DepositBankAccounts
<details><summary><code>client.senders.deposit_bank_accounts.<a href="src/mesta/senders/deposit_bank_accounts/client.py">generate_eur_gbp</a>(...) -> GenerateEurGbpDepositBankAccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Deprecated.** Use [`POST /v1/senders/{id}/generate-ondemand-deposit-bank-accounts`](#post_v1-senders-id-generate-ondemand-deposit-bank-accounts) instead.

Initiates the creation of EUR or GBP virtual IBAN deposit bank accounts for a sender. This is an asynchronous operation that may take up to 60 seconds to complete.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.deposit_bank_accounts.generate_eur_gbp(
    id="id",
    currency="EUR",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the sender
    
</dd>
</dl>

<dl>
<dd>

**currency:** `GenerateEurGbpDepositBankAccountsRequestCurrency` — The currency for the deposit bank account. Only EUR and GBP are supported.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.senders.deposit_bank_accounts.<a href="src/mesta/senders/deposit_bank_accounts/client.py">generate_on_demand</a>(...) -> GenerateOnDemandDepositBankAccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates the creation of a deposit bank account for a sender on demand, in the requested currency.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.deposit_bank_accounts.generate_on_demand(
    id="id",
    currency="EUR",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the sender
    
</dd>
</dl>

<dl>
<dd>

**currency:** `GenerateOnDemandDepositBankAccountsRequestCurrency` — The currency for the deposit bank account.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Senders DepositWalletAddresses
<details><summary><code>client.senders.deposit_wallet_addresses.<a href="src/mesta/senders/deposit_wallet_addresses/client.py">confirm</a>(...) -> ConfirmDepositWalletAddressesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Confirms and finalizes the deposit wallet addresses for a sender. This should be called after generate-deposit-wallet-addresses to complete the setup process.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.senders.deposit_wallet_addresses.confirm(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the sender
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ValidationRules Senders
<details><summary><code>client.validation_rules.senders.<a href="src/mesta/validation_rules/senders/client.py">get_v1</a>(...) -> GetV1SendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all validation rules required for creating a sender in a specific country. Use these rules to validate sender information before submission.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.validation_rules.senders.get_v1(
    owner_type="individual",
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_type:** `GetV1SendersRequestOwnerType` — Type of sender entity (individual or business)
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Two-letter ISO country code (e.g., IN for India)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.validation_rules.senders.<a href="src/mesta/validation_rules/senders/client.py">get_ubo_rules_v1</a>(...) -> GetUboRulesV1SendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves validation rules for UBO information based on country and owner type. These rules specify all required fields for UBO verification.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.validation_rules.senders.get_ubo_rules_v1(
    owner_type="individual",
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_type:** `GetUboRulesV1SendersRequestOwnerType` — Type of sender entity
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Two-letter ISO country code
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.validation_rules.senders.<a href="src/mesta/validation_rules/senders/client.py">list_document_types_v1</a>(...) -> ListDocumentTypesV1SendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the list of required documents for sender verification. This includes business registration documents and identity proofs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.validation_rules.senders.list_document_types_v1(
    owner_type="individual",
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_type:** `ListDocumentTypesV1SendersRequestOwnerType` — Type of sender entity
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Two-letter ISO country code
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.validation_rules.senders.<a href="src/mesta/validation_rules/senders/client.py">get_v2</a>(...) -> GetV2SendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all validation rules required for creating a sender in a specific country. V2 adds structured `supportedDocumentTypes` on identity fields, indicating which document types are available per country and their file upload requirements. The `documentNumber`, `documentFront`, and `documentBack` nested fields are removed as their requirements are conveyed by `supportedDocumentTypes`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.validation_rules.senders.get_v2(
    owner_type="individual",
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_type:** `GetV2SendersRequestOwnerType` — Type of sender entity (individual or business)
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Two-letter ISO country code (e.g., IN for India)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.validation_rules.senders.<a href="src/mesta/validation_rules/senders/client.py">get_ubo_rules_v2</a>(...) -> GetUboRulesV2SendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves validation rules for UBO (Ultimate Beneficial Owner) information. V2 adds structured `supportedDocumentTypes` on the identity documentType field, indicating available document types per country and their file upload requirements.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.validation_rules.senders.get_ubo_rules_v2(
    owner_type="business",
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_type:** `GetUboRulesV2SendersRequestOwnerType` — Type of sender entity (must be business for UBO rules)
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Two-letter ISO country code
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.validation_rules.senders.<a href="src/mesta/validation_rules/senders/client.py">list_document_types_v2</a>(...) -> ListDocumentTypesV2SendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the list of required documents for sender verification. This includes business registration documents and identity proofs. Same as V1.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.validation_rules.senders.list_document_types_v2(
    owner_type="individual",
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_type:** `ListDocumentTypesV2SendersRequestOwnerType` — Type of sender entity
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Two-letter ISO country code
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.validation_rules.senders.<a href="src/mesta/validation_rules/senders/client.py">list_countries</a>() -> ListCountriesSendersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of countries from which senders can originate payments.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.validation_rules.senders.list_countries()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ValidationRules Beneficiaries
<details><summary><code>client.validation_rules.beneficiaries.<a href="src/mesta/validation_rules/beneficiaries/client.py">get</a>(...) -> GetBeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all validation rules required for creating a beneficiary, including required fields and payment information requirements.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.validation_rules.beneficiaries.get(
    owner_type="individual",
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_type:** `GetBeneficiariesRequestOwnerType` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.validation_rules.beneficiaries.<a href="src/mesta/validation_rules/beneficiaries/client.py">list_document_types</a>(...) -> ListDocumentTypesBeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the list of required documents for beneficiary verification based on country and owner type. Note that some countries may not require any documents.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.validation_rules.beneficiaries.list_document_types(
    owner_type="individual",
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_type:** `ListDocumentTypesBeneficiariesRequestOwnerType` — Type of beneficiary entity
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Two-letter ISO country code
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.validation_rules.beneficiaries.<a href="src/mesta/validation_rules/beneficiaries/client.py">list_payment_types</a>(...) -> ListPaymentTypesBeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the list of supported payment types and their required fields for a beneficiary in a specific country. Use this to determine what payment information needs to be collected.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.validation_rules.beneficiaries.list_payment_types(
    owner_type="individual",
    country="country",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**owner_type:** `ListPaymentTypesBeneficiariesRequestOwnerType` — Type of beneficiary entity
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — Two-letter ISO country code
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.validation_rules.beneficiaries.<a href="src/mesta/validation_rules/beneficiaries/client.py">list_countries</a>() -> ListCountriesBeneficiariesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of countries to which payments can be delivered.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
    environment=MestaEnvironment.PRODUCTION,
)

client.validation_rules.beneficiaries.list_countries()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

