from typing import Optional

from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, override_output, colorized_print

settlement_app = Typer()


@settlement_app.command()
@colorized_print
@override_output
def get_settlements(
    page: int = 1,
    pagination: int = 50,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    subaccount: Optional[str] = None,
    data_only: bool = False,
):
    """Fetch settlements made to your settlement accounts."""
    return get_paystack_wrapper().settlements.get_settlements(
        page=page,
        pagination=pagination,
        start_date=start_date,
        end_date=end_date,
        subaccount=subaccount,
    )


@settlement_app.command()
@colorized_print
@override_output
def get_settlement_txns(
    id: str,
    pagination: int = 50,
    page: int = 1,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    data_only: bool = False,
):
    """Get the transactions that make up a particular settlement"""
    return get_paystack_wrapper().settlements.get_settlement_transactions(
        id=id,
        pagination=pagination,
        page=page,
        start_date=start_date,
        end_date=end_date,
    )
