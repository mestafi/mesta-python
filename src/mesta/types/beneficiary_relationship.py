
import typing

BeneficiaryRelationship = typing.Union[
    typing.Literal[
        "business_partner",
        "children",
        "colleague",
        "creditor",
        "customer",
        "debtor",
        "director",
        "employee",
        "franchisee",
        "holding_company",
        "self",
        "subsidiary_company",
        "supplier",
        "parents",
        "relative",
        "sibling",
    ],
    typing.Any,
]
