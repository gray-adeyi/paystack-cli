from typing import Optional

from typer import Typer
from pypaystack2 import Currency
from paystack_cli.utils import get_paystack_wrapper, override_output, colorized_print

dva_app = Typer()


@dva_app.command()
@colorized_print
@override_output
def get_dva(dedicated_account_id: int, data_only: bool = False):
    """Get details of a dedicated virtual account on your integration."""
    return get_paystack_wrapper().dedicated_accounts.get_dedicated_account(
        dedicated_account_id=dedicated_account_id
    )


@dva_app.command()
@colorized_print
@override_output
def get_dvas(
    active: bool = True,
    currency: Currency = Currency.NGN,
    provider_slug: Optional[str] = None,
    bank_id: Optional[str] = None,
    customer: Optional[str] = None,
    data_only: bool = False,
):
    """Fetches dedicated virtual accounts available on your integration."""
    return get_paystack_wrapper().dedicated_accounts.get_dedicated_accounts(
        active=active,
        currency=currency,
        provider_slug=provider_slug,
        bank_id=bank_id,
        customer=customer,
    )


@dva_app.command()
@colorized_print
@override_output
def create(
    customer: str,
    preferred_bank: Optional[str] = None,
    subaccount: Optional[str] = None,
    split_code: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    phone: Optional[str] = None,
    data_only: bool = False,
):
    """Create a dedicated virtual account and assign to a customer"""
    return get_paystack_wrapper().dedicated_accounts.create(
        customer=customer,
        preferred_bank=preferred_bank,
        subaccount=subaccount,
        split_code=split_code,
        first_name=first_name,
        last_name=last_name,
        phone=phone,
    )


@dva_app.command()
@colorized_print
@override_output
def deactivate(dedicated_account_id: int, data_only: bool = False):
    """Deactivate a dedicated virtual account on your integration."""
    return get_paystack_wrapper().dedicated_accounts.deactivate(
        dedicated_account_id=dedicated_account_id
    )


@dva_app.command()
@colorized_print
@override_output
def split(
    customer: str,
    subaccount: Optional[str] = None,
    split_code: Optional[str] = None,
    preferred_bank: Optional[str] = None,
    data_only: bool = False,
):
    """Split a dedicated virtual account transaction with one or more accounts"""
    return get_paystack_wrapper().dedicated_accounts.split(
        customer=customer,
        subaccount=subaccount,
        split_code=split_code,
        preferred_bank=preferred_bank,
    )


@dva_app.command()
@colorized_print
@override_output
def remove_split(account_number: str, data_only: bool = False):
    """Removes a split.

    If you've previously set up split payment for transactions on a
    dedicated virtual account, you can remove it with this method."""
    return get_paystack_wrapper().dedicated_accounts.remove_split(
        account_number=account_number
    )


@dva_app.command()
@colorized_print
@override_output
def get_providers(data_only: bool = False):
    """Get available bank providers for a dedicated virtual account"""
    return get_paystack_wrapper().dedicated_accounts.get_providers()


@dva_app.command()
@colorized_print
@override_output
def requery(
    customer: str,
    subaccount: Optional[str] = None,
    split_code: Optional[str] = None,
    preferred_bank: Optional[str] = None,
    data_only: bool = False,
):
    """Get details of a dedicated virtual account on your integration."""
    return get_paystack_wrapper().dedicated_accounts.requery(
        customer=customer,
        subaccount=subaccount,
        split_code=split_code,
        preferred_bank=preferred_bank,
    )
