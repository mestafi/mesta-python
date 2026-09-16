
import typing

PaymentMethodType = typing.Union[
    typing.Literal["bank_account", "pix", "swiftpay_pesonet", "instapay", "spei", "mobile_money", "crypto_wallet"],
    typing.Any,
]
