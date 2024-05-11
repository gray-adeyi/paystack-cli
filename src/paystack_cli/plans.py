from typing import Optional

from pypaystack2 import Interval, Currency
from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, override_output, colorized_print

plan_app = Typer()


@plan_app.command()
@colorized_print
@override_output
def create(
    name: str,
    amount: int,
    interval: Interval,
    description: Optional[str] = None,
    currency: Optional[Currency] = None,
    invoice_limit: Optional[int] = None,
    send_invoices: bool = False,
    send_sms: bool = False,
    data_only: bool = False,
):
    """Create a plan on your integration"""
    return get_paystack_wrapper().plans.create(
        name=name,
        amount=amount,
        interval=interval,
        description=description,
        currency=currency,
        invoice_limit=invoice_limit,
        send_invoices=send_invoices,
        send_sms=send_sms,
    )


@plan_app.command()
@colorized_print
@override_output
def update(
    id_or_code: str,
    name: Optional[str],
    amount: Optional[int],
    interval: Optional[Interval],
    description: Optional[str] = None,
    currency: Optional[Currency] = None,
    invoice_limit: Optional[int] = None,
    send_invoices: bool = False,
    send_sms: bool = False,
    data_only: bool = False,
):
    """Update a plan on your integration"""
    return get_paystack_wrapper().plans.update(
        id_or_code=id_or_code,
        name=name,
        amount=amount,
        interval=interval,
        description=description,
        currency=currency,
        invoice_limit=invoice_limit,
        send_invoices=send_invoices,
        send_sms=send_sms,
    )


@plan_app.command()
@colorized_print
@override_output
def get_plan(id_or_code: str, data_only: bool = False):
    """Get details of a plan on your integration."""
    return get_paystack_wrapper().plans.get_plan(id_or_code=id_or_code)


@plan_app.command()
@colorized_print
@override_output
def get_plans(id_or_code: str, data_only: bool = False):
    """Fetch plans available on your integration."""
    return get_paystack_wrapper().plans.get_plans(id_or_code=id_or_code)
