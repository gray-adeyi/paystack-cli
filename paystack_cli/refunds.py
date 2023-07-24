from typing import Optional

from pypaystack2 import Currency
from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, override_output, colorized_print

refund_app = Typer()


@refund_app.command()
@colorized_print
@override_output
def create(
    transaction: str,
    amount: Optional[int] = None,
    currency: Optional[Currency] = None,
    customer_note: Optional[str] = None,
    merchant_note: Optional[str] = None,
    data_only: bool = False,
):
    """Initiate a refund on your integration"""
    return get_paystack_wrapper().refunds.create(
        transaction=transaction,
        amount=amount,
        currency=currency,
        customer_note=customer_note,
        merchant_note=merchant_note,
    )


@refund_app.command()
@colorized_print
@override_output
def get_refund(reference: str, data_only: bool = False):
    """Get details of a refund on your integration."""
    return get_paystack_wrapper().refunds.get_refund(reference=reference)


@refund_app.command()
@colorized_print
@override_output
def get_refunds(
    reference: Optional[str] = None,
    currency: Optional[Currency] = None,
    pagination: int = 50,
    page: int = 1,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    data_only: bool = False,
):
    """Fetch refunds available on your integration"""
    return get_paystack_wrapper().refunds.get_refunds(
        reference=reference,
        currency=currency,
        pagination=pagination,
        page=page,
        start_date=start_date,
        end_date=end_date,
    )
