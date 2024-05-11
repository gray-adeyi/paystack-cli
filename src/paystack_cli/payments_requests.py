from typing import Optional

from pypaystack2 import Status, Currency, LineItem, Tax
from typer import Typer

from paystack_cli.utils import (
    get_paystack_wrapper,
    parse_cli_string,
    override_output,
    colorized_print,
)

payment_request_app = Typer()


@payment_request_app.command()
@colorized_print
@override_output
def create(
    customer: str,
    amount: int,
    due_date: Optional[str] = None,
    description: Optional[str] = None,
    line_items: Optional[str] = None,
    tax: Optional[str] = None,
    currency: Optional[Currency] = None,
    send_notification: Optional[bool] = None,
    draft: Optional[bool] = None,
    has_invoice: Optional[bool] = None,
    invoice_number: Optional[int] = None,
    split_code: Optional[str] = None,
    data_only: bool = False,
):
    """Create a payment request for a transaction on your integration"""
    if line_items:
        line_items = parse_cli_string(
            raw_string=line_items,
            arg_or_option_name="line_items",
            expected_type=LineItem,
            many=True,
        )
    if tax:
        tax = parse_cli_string(
            raw_string=tax, arg_or_option_name="tax", expected_type=Tax, many=True
        )
    return get_paystack_wrapper().payment_requests.create(
        customer=customer,
        amount=amount,
        due_date=due_date,
        description=description,
        line_items=line_items,
        tax=tax,
        currency=currency,
        send_notification=send_notification,
        draft=draft,
        has_invoice=has_invoice,
        invoice_number=invoice_number,
        split_code=split_code,
    )


@payment_request_app.command()
@colorized_print
@override_output
def update(
    customer: Optional[str] = None,
    status: Optional[Status] = None,
    currency: Optional[Currency] = None,
    include_archive: bool = False,
    page: int = 1,
    pagination: int = 50,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    data_only: bool = False,
):
    """Update the payment request details on your integration"""
    return get_paystack_wrapper().payment_requests.update(
        customer=customer,
        status=status,
        currency=currency,
        include_archive=include_archive,
        page=page,
        pagination=pagination,
        start_date=start_date,
        end_date=end_date,
    )


@payment_request_app.command()
@colorized_print
@override_output
def get_payment_request(id_or_code: str, data_only: bool = False):
    """Get details of a payment request on your integration"""
    return get_paystack_wrapper().payment_requests.get_payment_request(
        id_or_code=id_or_code
    )


@payment_request_app.command()
@colorized_print
@override_output
def get_payment_requests(
    customer: Optional[str] = None,
    status: Optional[Status] = None,
    currency: Optional[Currency] = None,
    include_archive: bool = False,
    page: int = 1,
    pagination: int = 50,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    data_only: bool = False,
):
    """Fetches the payment requests available on your integration."""
    return get_paystack_wrapper().payment_requests.get_payment_requests(
        customer=customer,
        status=status,
        currency=currency,
        include_archive=include_archive,
        page=page,
        pagination=pagination,
        start_date=start_date,
        end_date=end_date,
    )


@payment_request_app.command()
@colorized_print
@override_output
def verify(code: str, data_only: bool = False):
    """Verify details of a payment request on your integration."""
    return get_paystack_wrapper().payment_requests.verify(code=code)


@payment_request_app.command()
@colorized_print
@override_output
def archive(id_or_code: str, data_only: bool = False):
    """Used to archive a payment request.

    A payment request will no longer be fetched on list or returned on verify."""
    return get_paystack_wrapper().payment_requests.archive(id_or_code=id_or_code)


@payment_request_app.command()
@colorized_print
@override_output
def finalize(id_or_code: str, data_only: bool = False):
    """Finalize a draft payment request"""
    return get_paystack_wrapper().payment_requests.finalize(id_or_code=id_or_code)


@payment_request_app.command()
@colorized_print
@override_output
def get_total(data_only: bool = False):
    """Get payment requests metric"""
    return get_paystack_wrapper().payment_requests.get_total()
