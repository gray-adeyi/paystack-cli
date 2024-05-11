from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, override_output, colorized_print

integration_app = Typer()


@integration_app.command()
@colorized_print
@override_output
def get_payment_session_timeout(data_only: bool = False):
    """Fetch the payment session timeout on your integration"""
    return get_paystack_wrapper().integration.get_payment_session_timeout()


@integration_app.command()
@colorized_print
@override_output
def update_payment_session_timeout(timeout: int, data_only: bool = False):
    """Update the payment session timeout on your integration"""
    return get_paystack_wrapper().integration.update_payment_session_timeout(
        timeout=timeout
    )
