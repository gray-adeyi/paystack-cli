from typing import Optional

from pypaystack2 import Schedule
from typer import Typer

from paystack_cli.utils import (
    get_paystack_wrapper,
    parse_cli_string,
    override_output,
    colorized_print,
)

subaccount_app = Typer()


@subaccount_app.command()
@colorized_print
@override_output
def create(
    business_name: str,
    settlement_bank: str,
    account_number: str,
    percentage_charge: float,
    description: Optional[str] = None,
    primary_contact_email: Optional[str] = None,
    primary_contact_name: Optional[str] = None,
    primary_contact_phone: Optional[str] = None,
    metadata: Optional[str] = None,
    data_only: bool = False,
):
    """Create a subacount on your integration."""
    if metadata:
        metadata = parse_cli_string(
            raw_string=metadata, arg_or_option_name="metadata", expected_type=dict
        )
    return get_paystack_wrapper().subaccounts.create(
        business_name=business_name,
        settlement_bank=settlement_bank,
        account_number=account_number,
        percentage_charge=percentage_charge,
        description=description,
        primary_contact_email=primary_contact_email,
        primary_contact_name=primary_contact_name,
        primary_contact_phone=primary_contact_phone,
        metadata=metadata,
    )


@subaccount_app.command()
@colorized_print
@override_output
def update(
    id_or_code: str,
    business_name: str,
    settlement_bank: str,
    account_number: Optional[str] = None,
    active: Optional[bool] = None,
    percentage_charge: Optional[float] = None,
    description: Optional[str] = None,
    primary_contact_email: Optional[str] = None,
    primary_contact_name: Optional[str] = None,
    primary_contact_phone: Optional[str] = None,
    settlement_schedule: Optional[Schedule] = None,
    metadata: Optional[str] = None,
    data_only: bool = False,
):
    """Update a subaccount details on your integration."""
    if metadata:
        metadata = parse_cli_string(
            raw_string=metadata, arg_or_option_name="metadata", expected_type=dict
        )
    return get_paystack_wrapper().subaccounts.update(
        id_or_code=id_or_code,
        business_name=business_name,
        settlement_bank=settlement_bank,
        account_number=account_number,
        active=active,
        percentage_charge=percentage_charge,
        description=description,
        primary_contact_email=primary_contact_email,
        primary_contact_name=primary_contact_name,
        primary_contact_phone=primary_contact_phone,
        settlement_schedule=settlement_schedule,
        metadata=metadata,
    )


@subaccount_app.command()
@colorized_print
@override_output
def get_subaccount(id_or_code: str, data_only: bool = False):
    """Get details of a subaccount on your integration."""
    return get_paystack_wrapper().subaccounts.get_subaccount(id_or_code=id_or_code)


@subaccount_app.command()
@colorized_print
@override_output
def get_subaccounts(
    start_date: str,
    end_date: str,
    page: int = 1,
    pagination: int = 50,
    data_only: bool = False,
):
    """Fetch subaccounts available on your integration."""
    return get_paystack_wrapper().subaccounts.get_subaccounts(
        start_date=start_date, end_date=end_date, page=page, pagination=pagination
    )
