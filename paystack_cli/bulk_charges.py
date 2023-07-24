from typing import Optional

from pypaystack2 import Status, BulkChargeInstruction
from typer import Typer

from paystack_cli.utils import (
    get_paystack_wrapper,
    parse_cli_string,
    override_output,
    colorized_print,
)

bulk_charge_app = Typer()


@bulk_charge_app.command()
@colorized_print
@override_output
def initiate(body: str, data_only: bool = False):
    """Send a list of dictionaries with authorization codes and amount (in kobo if currency is NGN, pesewas,
    if currency is GHS, and cents, if currency is ZAR ) so paystack can process transactions as a batch.

    Note: The body is a json serializable string of a list of bulk charge instructions.
    see https://gray-adeyi.github.io/pypaystack2/
    """
    body = parse_cli_string(
        raw_string=body,
        arg_or_option_name="body",
        expected_type=BulkChargeInstruction,
        many=True,
    )
    return get_paystack_wrapper().bulk_charges.initiate(body=body)


@bulk_charge_app.command()
@colorized_print
@override_output
def get_batch(id_or_code: str, data_only: bool = False):
    """This command retrieves a specific batch from its id or code.

    It also returns useful information on its progress by way of the
    total_charges and pending_charges attributes in the Response
    """
    return get_paystack_wrapper().bulk_charges.get_batch(id_or_code=id_or_code)


@bulk_charge_app.command()
@colorized_print
@override_output
def get_batches(
    page: int = 1,
    pagination: int = 50,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    data_only: bool = False,
):
    """This gets all bulk charge batches created by the integration."""
    return get_paystack_wrapper().bulk_charges.get_batches(
        page=page, pagination=pagination, start_date=start_date, end_date=end_date
    )


@bulk_charge_app.command()
@colorized_print
@override_output
def get_charges_in_batch(
    id_or_code: str,
    status: Status,
    pagination: int = 50,
    page: int = 1,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    data_only: bool = False,
):
    """This command retrieves the charges associated with a specified batch code. Pagination parameters are available.

    You can also filter by status. Charge statuses can be pending, success or failed."""
    return get_paystack_wrapper().bulk_charges.get_charges_in_batch(
        id_or_code=id_or_code,
        status=status,
        pagination=pagination,
        page=page,
        start_date=start_date,
        end_date=end_date,
    )


@bulk_charge_app.command()
@colorized_print
@override_output
def pause_batch(batch_code: str, data_only: bool = False):
    """Use this command to pause processing a batch."""
    return get_paystack_wrapper().bulk_charges.pause_batch(batch_code=batch_code)


@bulk_charge_app.command()
@colorized_print
@override_output
def resume_batch(batch_code: str, data_only: bool = False):
    """Use this command to resume processing a batch"""
    return get_paystack_wrapper().bulk_charges.resume_batch(batch_code=batch_code)
