from typing import Optional

from pypaystack2 import AccountType, Country, Document
from typer import Typer

from paystack_cli.utils import get_paystack_wrapper

verification_app = Typer()


@verification_app.command()
def validate_account(
    account_name: str,
    account_number: str,
    account_type: AccountType,
    bank_code: str,
    country_code: Country,
    document_type: Document,
    document_number: Optional[str] = None,
):
    return get_paystack_wrapper().verification.validate_account(
        account_name=account_name,
        account_number=account_number,
        account_type=account_type,
        bank_code=bank_code,
        country_code=country_code,
        document_type=document_type,
        document_number=document_number,
    )


@verification_app.command()
def resolve_card_bin(bin: str):
    return get_paystack_wrapper().verification.resolve_card_bin(bin=bin)


@verification_app.command()
def resolve_account_number(account_number: str, bank_code: str):
    return get_paystack_wrapper().verification.resolve_account_number(
        account_number=account_number, bank_code=bank_code
    )
