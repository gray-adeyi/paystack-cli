from typing import Optional

from typer import Typer

from paystack_cli.utils import get_paystack_wrapper

subscription_app = Typer()


@subscription_app.command()
def create(
    customer: str,
    plan: str,
    authorization: Optional[str] = None,
    start_date: Optional[str] = None,
):
    return get_paystack_wrapper().subscriptions.create(
        customer=customer,
        plan=plan,
        authorization=authorization,
        start_date=start_date,
    )


@subscription_app.command()
def get_subscription(id_or_code: str):
    return get_paystack_wrapper().subscriptions.get_subscription(id_or_code=id_or_code)


@subscription_app.command()
def get_subscriptions(
    page: int = 1,
    pagination: int = 50,
    customer: Optional[int] = None,
    plan: Optional[int] = None,
):
    return get_paystack_wrapper().subscriptions.get_subscriptions(
        page=page, pagination=pagination, customer=customer, plan=plan
    )


@subscription_app.command()
def get_update_link(code: str):
    return get_paystack_wrapper().subscriptions.get_update_link(code=code)


@subscription_app.command()
def send_update_link(code: str):
    return get_paystack_wrapper().subscriptions.send_update_link(code=code)


@subscription_app.command()
def enable(code: str, token: str):
    return get_paystack_wrapper().subscriptions.enable(code=code, token=token)


@subscription_app.command()
def disable(code: str, token: str):
    return get_paystack_wrapper().subscriptions.disable(code=code, token=token)
