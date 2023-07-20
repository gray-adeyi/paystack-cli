from typing import Optional

from pypaystack2 import Split, Currency, Bearer, SplitAccount
from typer import Typer
from paystack_cli.utils import get_paystack_wrapper, parse_cli_string

transaction_split_app = Typer()


@transaction_split_app.command()
def get_split(id: str):
    return get_paystack_wrapper().splits.get_split(id=id)


@transaction_split_app.command()
def get_splits(
    name: str,
    sort_by: Optional[str],
    page: Optional[int],
    start_date: Optional[str],
    end_date: Optional[str],
    active: bool = True,
    pagination: int = 50,
):
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
def create(
    name: str,
    type: Split,
    currency: Currency,
    subaccounts: str,
    bearer_type: Bearer,
    bearer_subaccount: str,
):
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
def update(
    id: str,
    name: str,
    active: bool,
    bearer_type: Optional[Bearer],
    bearer_subaccount: Optional[str],
):
    return get_paystack_wrapper().splits.update(
        id=id,
        name=name,
        active=active,
        bearer_type=bearer_type,
        bearer_subaccount=bearer_subaccount,
    )


@transaction_split_app.command()
def remove(id: str, subaccount: str):
    return get_paystack_wrapper().splits.remove(id=id, subaccount=subaccount)


@transaction_split_app.command()
def add_or_update(id: str, subaccount: str, share: str):
    return get_paystack_wrapper().splits.add_or_update(
        id=id, subaccount=subaccount, share=share
    )
