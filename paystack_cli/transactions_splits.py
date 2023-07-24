from typing import Optional

from pypaystack2 import Split, Currency, Bearer, SplitAccount
from typer import Typer
from paystack_cli.utils import (
    get_paystack_wrapper,
    parse_cli_string,
    override_output,
    colorized_print,
)

transaction_split_app = Typer()


@transaction_split_app.command()
@colorized_print
@override_output
def get_split(id: str, data_only: bool = False):
    return get_paystack_wrapper().splits.get_split(id=id)


@transaction_split_app.command()
@colorized_print
@override_output
def get_splits(
    name: str,
    sort_by: Optional[str],
    page: Optional[int],
    start_date: Optional[str],
    end_date: Optional[str],
    active: bool = True,
    pagination: int = 50,
    data_only: bool = False,
):
    """Get/search for the transaction splits available on your integration."""
    return get_paystack_wrapper().splits.get_splits(
        name=name,
        sort_by=sort_by,
        page=page,
        start_date=start_date,
        end_date=end_date,
        active=active,
        pagination=pagination,
    )


@transaction_split_app.command()
@colorized_print
@override_output
def create(
    name: str,
    type: Split,
    currency: Currency,
    subaccounts: str,
    bearer_type: Bearer,
    bearer_subaccount: str,
    data_only: bool = False,
):
    """Create a split payment on your integration"""
    subaccounts = parse_cli_string(
        raw_string=subaccounts,
        arg_or_option_name="subaccounts",
        expected_type=SplitAccount,
        many=True,
    )
    return get_paystack_wrapper().splits.create(
        name=name,
        type=type,
        currency=currency,
        subaccounts=subaccounts,
        bearer_type=bearer_type,
        bearer_subaccount=bearer_subaccount,
    )


@transaction_split_app.command()
@colorized_print
@override_output
def update(
    id: str,
    name: str,
    active: bool,
    bearer_type: Optional[Bearer],
    bearer_subaccount: Optional[str],
    data_only: bool = False,
):
    """Update a transaction split details on your integration"""
    return get_paystack_wrapper().splits.update(
        id=id,
        name=name,
        active=active,
        bearer_type=bearer_type,
        bearer_subaccount=bearer_subaccount,
    )


@transaction_split_app.command()
@colorized_print
@override_output
def remove(id: str, subaccount: str, data_only: bool = False):
    """Remove a subaccount from a transaction split"""
    return get_paystack_wrapper().splits.remove(id=id, subaccount=subaccount)


@transaction_split_app.command()
@colorized_print
@override_output
def add_or_update(id: str, subaccount: str, share: str, data_only: bool = False):
    """Add a Subaccount to a Transaction Split, or update the share of an existing Subaccount in a Transaction Split"""
    return get_paystack_wrapper().splits.add_or_update(
        id=id, subaccount=subaccount, share=share
    )
