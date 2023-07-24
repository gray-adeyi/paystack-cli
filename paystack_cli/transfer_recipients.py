from typing import Optional

from pypaystack2 import Recipient, Currency, RecipientType
from typer import Typer

from paystack_cli.utils import (
    get_paystack_wrapper,
    parse_cli_string,
    override_output,
    colorized_print,
)

transfer_recipient_app = Typer()


@transfer_recipient_app.command()
@colorized_print
@override_output
def create(
    type: RecipientType,
    name: str,
    account_number: str,
    bank_code: Optional[str] = None,
    description: Optional[str] = None,
    currency: Optional[Currency] = None,
    auth_code: Optional[str] = None,
    metadata: Optional[str] = None,
    data_only: bool = False,
):
    if metadata:
        metadata = parse_cli_string(
            raw_string=metadata, arg_or_option_name="metadata", expected_type=dict
        )
    return get_paystack_wrapper().transfer_recipients.create(
        type=type,
        name=name,
        account_number=account_number,
        bank_code=bank_code,
        description=description,
        currency=currency,
        auth_code=auth_code,
        metadata=metadata,
    )


@transfer_recipient_app.command()
@colorized_print
@override_output
def update(
    id_or_code: str, name: str, email: Optional[str] = None, data_only: bool = False
):
    return get_paystack_wrapper().transfer_recipients.update(
        id_or_code=id_or_code, name=name, email=email
    )


@transfer_recipient_app.command()
@colorized_print
@override_output
def get_transfer_recipient(id_or_code: str, data_only: bool = False):
    return get_paystack_wrapper().transfer_recipients.get_transfer_recipient(
        id_or_code=id_or_code
    )


@transfer_recipient_app.command()
@colorized_print
@override_output
def get_transfer_recipients(
    page: int = 1,
    pagination: int = 50,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    data_only: bool = False,
):
    return get_paystack_wrapper().transfer_recipients.get_transfer_recipients(
        page=page, pagination=pagination, start_date=start_date, end_date=end_date
    )


@transfer_recipient_app.command()
@colorized_print
@override_output
def bulk_create(batch: str, data_only: bool = False):
    batch = parse_cli_string(
        raw_string=batch, arg_or_option_name="batch", expected_type=Recipient, many=True
    )
    return get_paystack_wrapper().transfer_recipients.bulk_create(batch=batch)


@transfer_recipient_app.command()
@colorized_print
@override_output
def delete(id_or_code: str, data_only: bool = False):
    return get_paystack_wrapper().transfer_recipients.delete(id_or_code=id_or_code)
