import json
from typing import Optional

from pypaystack2 import TransactionStatus, Currency, Channel, Bearer
from typer import Typer

from paystack_cli.utils import (
    get_paystack_wrapper,
    parse_cli_string,
    override_output,
    colorized_print,
)

transaction_app = Typer()


@transaction_app.command()
@colorized_print
@override_output
def get_txn(id: str, data_only: bool = False):
    """Get details of a transaction carried out on your integration."""
    return get_paystack_wrapper().transactions.get_transaction(id=id)


@transaction_app.command()
@colorized_print
@override_output
def get_txns(
    customer_id: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    status: Optional[TransactionStatus] = None,
    page: Optional[int] = None,
    amount: Optional[int] = None,
    pagination: int = 50,
    data_only: bool = False,
):
    """Fetch transactions carried out on your integration."""
    return get_paystack_wrapper().transactions.get_transactions(
        customer=customer_id,
        start_date=start_date,
        end_date=end_date,
        status=status,
        page=page,
        amount=amount,
        pagination=pagination,
    )


@transaction_app.command()
@colorized_print
@override_output
def get_timeline(id_or_ref: str, data_only: bool = False):
    """View the timeline of a transaction"""
    return get_paystack_wrapper().transactions.get_timeline(id_or_ref=id_or_ref)


@transaction_app.command()
@colorized_print
@override_output
def charge(
    amount: int,
    email: str,
    auth_code: str,
    reference: Optional[str] = None,
    currency: Optional[Currency] = None,
    metadata: Optional[str] = None,
    channels: Optional[list[Channel]] = None,
    subaccount: Optional[str] = None,
    transaction_charge: Optional[int] = None,
    bearer: Optional[Bearer] = None,
    queue: bool = False,
    data_only: bool = False,
):
    """All authorizations marked as reusable can be charged with this endpoint whenever you need to receive payments."""
    if metadata:
        metadata = parse_cli_string(
            raw_string=metadata, arg_or_option_name="metadata", expected_type=dict
        )
    return get_paystack_wrapper().transactions.charge(
        amount=amount,
        email=email,
        auth_code=auth_code,
        reference=reference,
        currency=currency,
        metadata=metadata,
        channels=channels,
        subaccount=subaccount,
        transaction_charge=transaction_charge,
        bearer=bearer,
        queue=queue,
    )


@transaction_app.command()
@colorized_print
@override_output
def export(
    page: Optional[int] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    customer_id: Optional[str] = None,
    status: Optional[TransactionStatus] = None,
    currency: Optional[Currency] = None,
    amount: Optional[int] = None,
    settled: Optional[bool] = None,
    settlement_id: Optional[int] = None,
    payment_page: Optional[int] = None,
    pagination: int = 50,
    data_only: bool = False,
):
    """Fetch transactions carried out on your integration."""
    return get_paystack_wrapper().transactions.export(
        page=page,
        start_date=start_date,
        end_date=end_date,
        customer=customer_id,
        status=status,
        currency=currency,
        amount=amount,
        settled=settled,
        settlement=settlement_id,
        payment_page=payment_page,
        pagination=pagination,
    )


@transaction_app.command()
@colorized_print
@override_output
def init(
    amount: int,
    email: str,
    currency: Optional[Currency] = None,
    reference: Optional[str] = None,
    callback_url: Optional[str] = None,
    plan_id: Optional[str] = None,
    invoice_limit: Optional[int] = None,
    metadata: Optional[str] = None,
    channels: Optional[list[Channel]] = None,
    split_code: Optional[str] = None,
    subaccount: Optional[str] = None,
    transfer_charge: Optional[int] = None,
    bearer: Optional[Bearer] = None,
    data_only: bool = False,
):
    """Initialize a transaction"""
    if metadata:
        metadata = parse_cli_string(
            raw_string=metadata, arg_or_option_name="metadata", expected_type=dict
        )
    return get_paystack_wrapper().transactions.initialize(
        amount=amount,
        email=email,
        currency=currency,
        reference=reference,
        callback_url=callback_url,
        plan=plan_id,
        invoice_limit=invoice_limit,
        metadata=metadata,
        channels=channels,
        split_code=split_code,
        subaccount=subaccount,
        transfer_charge=transfer_charge,
        bearer=bearer,
    )


@transaction_app.command()
@colorized_print
@override_output
def partial_debit(
    auth_code: str,
    currency: Currency,
    amount: int,
    email: str,
    reference: Optional[str] = None,
    at_least: Optional[int] = None,
    data_only: bool = False,
):
    """Retrieve part of a payment from a customer"""
    get_paystack_wrapper().transactions.partial_debit(
        auth_code=auth_code,
        currency=currency,
        amount=amount,
        email=email,
        reference=reference,
        at_least=at_least,
    )


@transaction_app.command()
@colorized_print
@override_output
def totals(
    page: Optional[int] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    pagination: int = 50,
    data_only: bool = False,
):
    """Total amount received on your account"""
    get_paystack_wrapper().transactions.totals(
        page=page, start_date=start_date, end_date=end_date, pagination=pagination
    )


@transaction_app.command()
@colorized_print
@override_output
def verify(reference: str, data_only: bool = False):
    get_paystack_wrapper().transactions.verify(reference=reference)
