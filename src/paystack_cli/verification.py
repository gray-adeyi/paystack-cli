from typing import Optional

from pypaystack2 import AccountType, Country, Document
from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, override_output, colorized_print

verification_app = Typer()


@verification_app.command()
@colorized_print
@override_output
def validate_account(
    account_name: str,
    account_number: str,
    account_type: AccountType,
    bank_code: str,
    country_code: Country,
    document_type: Document,
    document_number: Optional[str] = None,
    data_only: bool = False,
):
    """Confirm the authenticity of a customer's account number before sending money"""
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
@colorized_print
@override_output
def resolve_card_bin(bin: str, data_only: bool = False):
    """Get more information about a customer's card"""
    return get_paystack_wrapper().verification.resolve_card_bin(bin=bin)


@verification_app.command()
@colorized_print
@override_output
def resolve_account_number(
    account_number: str, bank_code: str, data_only: bool = False
):
    """Confirm an account belongs to the right customer"""
    return get_paystack_wrapper().verification.resolve_account_number(
        account_number=account_number, bank_code=bank_code
    )
