# Mesta Python Library

[![pypi](https://img.shields.io/pypi/v/mesta)](https://pypi.python.org/pypi/mesta)

The official Mesta client library. It is generated from the Mesta OpenAPI specification and updated with every API release. Each method calls one API endpoint. For end-to-end flows such as onboarding a sender or making a payout, follow the guides at https://docs.mesta.xyz.

## Table of Contents

- [Documentation](#documentation)
- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Environments](#environments)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)

## Documentation

API reference documentation is available [here](https://docs.mesta.xyz).

## Installation

```sh
pip install mesta
```

## Reference

A full reference for this library is available [here](https://github.com/mestafi/mesta-python/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from mesta import Mesta

client = Mesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
)

client.merchants.accept_terms(
    merchant_id="merchantId",
)
```

## Environments

This SDK allows you to configure different environments for API requests.

```python
from mesta import Mesta
from mesta.environment import MestaEnvironment

client = Mesta(
    environment=MestaEnvironment.PRODUCTION,
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from mesta import AsyncMesta

client = AsyncMesta(
    api_key="<value>",
    api_secret="<x-api-secret>",
)


async def main() -> None:
    await client.merchants.accept_terms(
        merchant_id="merchantId",
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from mesta.core.api_error import ApiError

try:
    client.merchants.accept_terms(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from mesta import Mesta

client = Mesta(...)
response = client.merchants.with_raw_response.accept_terms(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

Which status codes are retried depends on the `retryStatusCodes` generator configuration:

**`legacy`** (current default): retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses) (All server errors, including 500)

**`recommended`**: retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [502](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502) (Bad Gateway)
- [503](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) (Service Unavailable)
- [504](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504) (Gateway Timeout)

Use the `max_retries` request option to configure this behavior.

```python
client.merchants.accept_terms(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from mesta import Mesta

client = Mesta(..., timeout=20.0)

# Override timeout for a specific method
client.merchants.accept_terms(..., request_options={
    "timeout": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from mesta import Mesta

client = Mesta(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Retries and writes

The client retries a request up to two times on 408, 429 and 5xx responses, with backoff and jitter. The Mesta API does not accept an idempotency key yet, so a retried write, for example creating an order or a beneficiary, can be processed twice if the first attempt reached the server before it failed. Until idempotency keys are available, disable retries on writes and handle the error in your code:

```python
client.orders.create(..., request_options={"max_retries": 0})
```
