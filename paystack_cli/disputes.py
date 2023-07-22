from typing import Optional

from pypaystack2 import DisputeStatus, Resolution
from typer import Typer

from paystack_cli.utils import get_paystack_wrapper

dispute_app = Typer()


@dispute_app.command()
def get_dispute(id: str):
    return get_paystack_wrapper().disputes.get_dispute(id=id)


@dispute_app.command()
def get_disputes(
    start_date: str,
    end_date: str,
    pagination: int = 50,
    page: int = 1,
    transaction: Optional[str] = None,
    status: Optional[DisputeStatus] = None,
):
    return get_paystack_wrapper().disputes.get_disputes(
        start_date=start_date,
        end_date=end_date,
        pagination=pagination,
        page=page,
        transaction=transaction,
        status=status,
    )


@dispute_app.command()
def get_transaction_disputes(id: str):
    return get_paystack_wrapper().disputes.get_transaction_disputes(id=id)


@dispute_app.command()
def resolve_dispute(
    id: str,
    resolution: Resolution,
    message: str,
    refund_amount: int,
    uploaded_filename: str,
    evidence: Optional[int] = None,
):
    return get_paystack_wrapper().disputes.resolve_dispute(
        id=id,
        resolution=resolution,
        message=message,
        refund_amount=refund_amount,
        uploaded_filename=uploaded_filename,
        evidence=evidence,
    )


@dispute_app.command()
def export_disputes(
    start_date: str,
    end_date: str,
    pagination: int = 50,
    page: int = 1,
    transaction: Optional[str] = None,
    status: Optional[DisputeStatus] = None,
):
    return get_paystack_wrapper().disputes.export_disputes(
        start_date=start_date,
        end_date=end_date,
        pagination=pagination,
        page=page,
        transaction=transaction,
        status=status,
    )


@dispute_app.command()
def add_evidence(
    id: str,
    customer_email: str,
    customer_name: str,
    customer_phone: str,
    service_details: str,
    delivery_address: Optional[str] = None,
    delivery_date: Optional[str] = None,
):
    return get_paystack_wrapper().disputes.add_evidence(
        id=id,
        customer_email=customer_email,
        customer_name=customer_name,
        customer_phone=customer_phone,
        service_details=service_details,
        delivery_address=delivery_address,
        delivery_date=delivery_date,
    )


@dispute_app.command()
def get_upload_url(id: str, upload_filename: str):
    return get_paystack_wrapper().disputes.get_upload_url(
        id=id, upload_filename=upload_filename
    )


@dispute_app.command()
def update_dispute(id: str, refund_amount: int, uploaded_filename: Optional[str]):
    return get_paystack_wrapper().disputes.update_dispute(
        id=id, refund_amount=refund_amount, uploaded_filename=uploaded_filename
    )
