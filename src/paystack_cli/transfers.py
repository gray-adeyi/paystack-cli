from typing import Optional

from pypaystack2 import TransferInstruction, Currency
from typer import Typer

from paystack_cli.utils import (
    get_paystack_wrapper,
    parse_cli_string,
    colorized_print,
    override_output,
)

transfer_app = Typer()


@transfer_app.command()
@colorized_print
@override_output
def initiate(
    amount: int,
    recipient: str,
    reason: Optional[str] = None,
    currency: Optional[Currency] = None,
    reference: Optional[str] = None,
    source: str = "balance",
    data_only: bool = False,
):
    """Initiate transfer"""
    return get_paystack_wrapper().transfers.initiate(
        amount=amount,
        recipient=recipient,
        reason=reason,
        currency=currency,
        reference=reference,
        source=source,
    )


@transfer_app.command()
@colorized_print
@override_output
def get_transfer(id_or_code: str, data_only: bool = False):
    """Retrieve a transfer"""
    return get_paystack_wrapper().transfers.get_transfer(id_or_code=id_or_code)


@transfer_app.command()
@colorized_print
@override_output
def get_transfers(
    page: int = 1,
    pagination: int = 50,
    customer: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    data_only: bool = False,
):
    """Retrieve transfers made to a customer"""
    return get_paystack_wrapper().transfers.get_transfers(
        page=page,
        pagination=pagination,
        customer=customer,
        start_date=start_date,
        end_date=end_date,
    )


@transfer_app.command()
@colorized_print
@override_output
def verify(reference: str, data_only: bool = False):
    """Verify a transfer"""
    return get_paystack_wrapper().transfers.verify(reference=reference)


@transfer_app.command()
@colorized_print
@override_output
def finalize(transfer_code: str, otp: str, data_only: bool = False):
    """Finalize transfer"""
    return get_paystack_wrapper().transfers.finalize(
        transfer_code=transfer_code, otp=otp
    )


@transfer_app.command()
@colorized_print
@override_output
def bulk_transfer(transfers: str, source="balance", data_only: bool = False):
    """Transfer in bulk"""
    transfers = parse_cli_string(
        raw_string=transfers,
        arg_or_option_name="transfers",
        expected_type=TransferInstruction,
        many=True,
    )
    return get_paystack_wrapper().transfers.bulk_transfer(
        transfers=transfers, source=source
    )
