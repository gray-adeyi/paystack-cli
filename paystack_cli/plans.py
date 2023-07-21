from typing import Optional

from pypaystack2 import Interval, Currency
from typer import Typer

from paystack_cli.utils import get_paystack_wrapper

plan_app = Typer()


@plan_app.command()
def create(
    name: str,
    amount: int,
    interval: Interval,
    description: Optional[str] = None,
    currency: Optional[Currency] = None,
    invoice_limit: Optional[int] = None,
    send_invoices: bool = False,
    send_sms: bool = False,
):
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
):
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
def get_plan(id_or_code: str):
    return get_paystack_wrapper().plans.get_plan(id_or_code=id_or_code)


@plan_app.command()
def get_plans(id_or_code: str):
    return get_paystack_wrapper().plans.get_plans(id_or_code=id_or_code)
