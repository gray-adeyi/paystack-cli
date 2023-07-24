from typing import Optional

from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, override_output, colorized_print

subscription_app = Typer()


@subscription_app.command()
@colorized_print
@override_output
def create(
    customer: str,
    plan: str,
    authorization: Optional[str] = None,
    start_date: Optional[str] = None,
    data_only: bool = False,
):
    """Create a subscription on your integration"""
    return get_paystack_wrapper().subscriptions.create(
        customer=customer,
        plan=plan,
        authorization=authorization,
        start_date=start_date,
    )


@subscription_app.command()
@colorized_print
@override_output
def get_subscription(id_or_code: str, data_only: bool = False):
    """Fetch details of a subscription on your integration."""
    return get_paystack_wrapper().subscriptions.get_subscription(id_or_code=id_or_code)


@subscription_app.command()
@colorized_print
@override_output
def get_subscriptions(
    page: int = 1,
    pagination: int = 50,
    customer: Optional[int] = None,
    plan: Optional[int] = None,
    data_only: bool = False,
):
    """Fetch subscriptions available on your integration."""
    return get_paystack_wrapper().subscriptions.get_subscriptions(
        page=page, pagination=pagination, customer=customer, plan=plan
    )


@subscription_app.command()
@colorized_print
@override_output
def get_update_link(code: str, data_only: bool = False):
    """Generate a link for updating the card on a subscription"""
    return get_paystack_wrapper().subscriptions.get_update_link(code=code)


@subscription_app.command()
@colorized_print
@override_output
def send_update_link(code: str, data_only: bool = False):
    """Email a customer a link for updating the card on their subscription"""
    return get_paystack_wrapper().subscriptions.send_update_link(code=code)


@subscription_app.command()
@colorized_print
@override_output
def enable(code: str, token: str, data_only: bool = False):
    """Enable a subscription on your integration"""
    return get_paystack_wrapper().subscriptions.enable(code=code, token=token)


@subscription_app.command()
@colorized_print
@override_output
def disable(code: str, token: str, data_only: bool = False):
    """Disable a subscription on your integration"""
    return get_paystack_wrapper().subscriptions.disable(code=code, token=token)
