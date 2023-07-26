from pypaystack2 import Reason
from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, override_output, colorized_print

transfer_control_app = Typer()


@transfer_control_app.command()
@colorized_print
@override_output
def get_balance_ledger(data_only: bool = False):
    """Fetch all pay-ins and pay-outs that occurred on your integration"""
    return get_paystack_wrapper().transfer_control.get_balance_ledger()


@transfer_control_app.command()
@colorized_print
@override_output
def resend_otp(transfer_code: str, reason: Reason, data_only: bool = False):
    """Generates a new OTP and sends to customer in the event they are having trouble receiving one."""
    return get_paystack_wrapper().transfer_control.resend_otp(
        transfer_code=transfer_code, reason=reason
    )


@transfer_control_app.command()
@colorized_print
@override_output
def enable_otp(data_only: bool = False):
    """In the event that a customer wants to stop being able to complete transfers programmatically,
    this endpoint helps turn OTP requirement back on. No arguments required."""
    return get_paystack_wrapper().transfer_control.enable_otp()


@transfer_control_app.command()
@colorized_print
@override_output
def disable_otp(data_only: bool = False):
    """This is used in the event that you want to be able to complete transfers
    programmatically without use of OTPs. No arguments required.
    You will get an OTP to complete the request"""
    return get_paystack_wrapper().transfer_control.disable_otp()


@transfer_control_app.command()
@colorized_print
@override_output
def check_balance(data_only: bool = False):
    """Fetch the available balance on your integration"""
    return get_paystack_wrapper().transfer_control.check_balance()


@transfer_control_app.command()
@colorized_print
@override_output
def finalize_disable_otp(otp: str, data_only: bool = False):
    """Finalize the request to disable OTP on your transfers."""
    return get_paystack_wrapper().transfer_control.finalize_disable_otp(otp=otp)
