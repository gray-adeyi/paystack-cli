from typing import Optional

from pypaystack2 import RiskAction, Identification, Country
from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, parse_cli_string

customer_app = Typer()


@customer_app.command()
def get_customer(email_or_code: str):
    return get_paystack_wrapper().customers.get_customer(email_or_code=email_or_code)


@customer_app.command()
def get_customers(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    page: int = 1,
    pagination: int = 50,
):
    return get_paystack_wrapper().customers.get_customers(
        start_date=start_date, end_date=end_date, page=page, pagination=pagination
    )


@customer_app.command()
def create(
    email: str,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    phone: Optional[str] = None,
    metadata: Optional[str] = None,
):
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
def update(
    code: str,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    phone: Optional[str] = None,
    metadata: Optional[str] = None,
):
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
def flag(customer: str, risk_action: Optional[RiskAction] = None):
    return get_paystack_wrapper().customers.flag(
        customer=customer, risk_action=risk_action
    )


@customer_app.command()
def deactivate(auth_code: str):
    return get_paystack_wrapper().customers.deactivate(auth_code=auth_code)


@customer_app.command()
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
):
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
