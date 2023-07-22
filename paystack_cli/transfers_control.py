from typer import Typer

from paystack_cli.utils import get_paystack_wrapper

transfer_control_app = Typer()


@transfer_control_app.command()
def get_balance_ledger():
    return get_paystack_wrapper().transfer_control.get_balance_ledger()


@transfer_control_app.command()
def resend_otp():
    return get_paystack_wrapper().transfer_control.resend_otp()


@transfer_control_app.command()
def enable_otp():
    return get_paystack_wrapper().transfer_control.enable_otp()


@transfer_control_app.command()
def disable_otp():
    return get_paystack_wrapper().transfer_control.disable_otp()


@transfer_control_app.command()
def check_balance():
    return get_paystack_wrapper().transfer_control.check_balance()


@transfer_control_app.command()
def finalize_disable_otp(otp: str):
    return get_paystack_wrapper().transfer_control.finalize_disable_otp(otp=otp)
