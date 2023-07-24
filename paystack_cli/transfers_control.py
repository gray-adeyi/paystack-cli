from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, override_output, colorized_print

transfer_control_app = Typer()


@transfer_control_app.command()
@colorized_print
@override_output
def get_balance_ledger(data_only: bool = False):
    return get_paystack_wrapper().transfer_control.get_balance_ledger()


@transfer_control_app.command()
@colorized_print
@override_output
def resend_otp(data_only: bool = False):
    return get_paystack_wrapper().transfer_control.resend_otp()


@transfer_control_app.command()
@colorized_print
@override_output
def enable_otp(data_only: bool = False):
    return get_paystack_wrapper().transfer_control.enable_otp()


@transfer_control_app.command()
@colorized_print
@override_output
def disable_otp(data_only: bool = False):
    return get_paystack_wrapper().transfer_control.disable_otp()


@transfer_control_app.command()
@colorized_print
@override_output
def check_balance(data_only: bool = False):
    return get_paystack_wrapper().transfer_control.check_balance()


@transfer_control_app.command()
@colorized_print
@override_output
def finalize_disable_otp(otp: str, data_only: bool = False):
    return get_paystack_wrapper().transfer_control.finalize_disable_otp(otp=otp)
