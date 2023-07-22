from typing import Optional

from pypaystack2 import Status, BulkChargeInstruction
from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, parse_cli_string

bulk_charge_app = Typer()


@bulk_charge_app.command()
def initiate(body: str):
    body = parse_cli_string(
        raw_string=body,
        arg_or_option_name="body",
        expected_type=BulkChargeInstruction,
        many=True,
    )
    return get_paystack_wrapper().bulk_charges.initiate(body=body)


@bulk_charge_app.command()
def get_batch(id_or_code: str):
    return get_paystack_wrapper().bulk_charges.get_batch(id_or_code=id_or_code)


@bulk_charge_app.command()
def get_batches(
    page: int = 1,
    pagination: int = 50,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
):
    return get_paystack_wrapper().bulk_charges.get_batches(
        page=page, pagination=pagination, start_date=start_date, end_date=end_date
    )


@bulk_charge_app.command()
def get_charges_in_batch(
    id_or_code: str,
    status: Status,
    pagination: int = 50,
    page: int = 1,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
):
    return get_paystack_wrapper().bulk_charges.get_charges_in_batch(
        id_or_code=id_or_code,
        status=status,
        pagination=pagination,
        page=page,
        start_date=start_date,
        end_date=end_date,
    )


@bulk_charge_app.command()
def pause_batch(batch_code: str):
    return get_paystack_wrapper().bulk_charges.pause_batch(batch_code=batch_code)


@bulk_charge_app.command()
def resume_batch(batch_code: str):
    return get_paystack_wrapper().bulk_charges.resume_batch(batch_code=batch_code)
