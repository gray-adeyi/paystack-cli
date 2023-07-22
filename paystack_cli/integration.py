from typer import Typer

from paystack_cli.utils import get_paystack_wrapper

integration_app = Typer()


@integration_app.command()
def get_payment_session_timeout():
    return get_paystack_wrapper().integration.get_payment_session_timeout()


@integration_app.command()
def update_payment_session_timeout(timeout: int):
    return get_paystack_wrapper().integration.update_payment_session_timeout(
        timeout=timeout
    )
