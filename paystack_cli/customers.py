from typing import Optional

from pypaystack2 import RiskAction, Identification, Country
from typer import Typer

from paystack_cli.utils import (
    get_paystack_wrapper,
    parse_cli_string,
    override_output,
    colorized_print,
)

customer_app = Typer()


@customer_app.command()
@colorized_print
@override_output
def get_customer(email_or_code: str, data_only: bool = False):
    """Get details of a customer on your integration."""
    return get_paystack_wrapper().customers.get_customer(email_or_code=email_or_code)


@customer_app.command()
@colorized_print
@override_output
def get_customers(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    page: int = 1,
    pagination: int = 50,
    data_only: bool = False,
):
    """Fetches customers available on your integration"""
    return get_paystack_wrapper().customers.get_customers(
        start_date=start_date, end_date=end_date, page=page, pagination=pagination
    )


@customer_app.command()
@colorized_print
@override_output
def create(
    email: str,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    phone: Optional[str] = None,
    metadata: Optional[str] = None,
    data_only: bool = False,
):
    """Fetches customers available on your integration."""
    if metadata:
        metadata = parse_cli_string(
            raw_string=metadata, arg_or_option_name="metadata", expected_type=dict
        )
    return get_paystack_wrapper().customers.create(
        email=email,
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        metadata=metadata,
    )


@customer_app.command()
@colorized_print
@override_output
def update(
    code: str,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    phone: Optional[str] = None,
    metadata: Optional[str] = None,
    data_only: bool = False,
):
    """Update a customer's details on your integration"""
    if metadata:
        metadata = parse_cli_string(
            raw_string=metadata, arg_or_option_name="metadata", expected_type=dict
        )
    return get_paystack_wrapper().customers.update(
        code=code,
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        metadata=metadata,
    )


@customer_app.command()
@colorized_print
@override_output
def flag(
    customer: str, risk_action: Optional[RiskAction] = None, data_only: bool = False
):
    """Whitelist or blacklist a customer on your integration"""
    return get_paystack_wrapper().customers.flag(
        customer=customer, risk_action=risk_action
    )


@customer_app.command()
@colorized_print
@override_output
def deactivate(auth_code: str, data_only: bool = False):
    """Deactivate an authorization when the card needs to be forgotten"""
    return get_paystack_wrapper().customers.deactivate(auth_code=auth_code)


@customer_app.command()
@colorized_print
@override_output
def validate(
    email_or_code: str,
    first_name: str,
    last_name: str,
    identification_type: Identification,
    country: Country,
    bvn: str,
    identification_number: Optional[str] = None,
    bank_code: Optional[str] = None,
    account_number: Optional[str] = None,
    middle_name: Optional[str] = None,
    data_only: bool = False,
):
    """Validate a customer's identity"""
    return get_paystack_wrapper().customers.validate(
        email_or_code=email_or_code,
        first_name=first_name,
        last_name=last_name,
        identification_type=identification_type,
        country=country,
        bvn=bvn,
        identification_number=identification_number,
        bank_code=bank_code,
        account_number=account_number,
        middle_name=middle_name,
    )
