from typing import Optional

from pypaystack2 import Gateway, Country, BankType, Currency
from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, colorized_print, override_output

miscellaneous_app = Typer()


@miscellaneous_app.command()
@colorized_print
@override_output
def get_banks(
    country: Country,
    use_cursor: bool = False,
    next: Optional[str] = None,
    previous: Optional[str] = None,
    gateway: Optional[Gateway] = None,
    type: Optional[BankType] = None,
    currency: Optional[Currency] = None,
    pagination: int = 50,
    json: bool = False,
    data_only: bool = False,
):
    """Get a list of all supported banks and their properties"""
    return get_paystack_wrapper().miscellaneous.get_banks(
        country=country,
        use_cursor=use_cursor,
        next=next,
        previous=previous,
        gateway=gateway,
        type=type,
        currency=currency,
        pagination=pagination,
    )


@miscellaneous_app.command()
@colorized_print
@override_output
def get_states(country: Country, data_only: bool = False, json: bool = False):
    """Get a list of states for a country for address verification."""
    return get_paystack_wrapper().miscellaneous.get_states(country=country)


@miscellaneous_app.command()
@colorized_print
@override_output
def get_countries(json: bool = False, data_only: bool = False):
    """Gets a list of Countries that Paystack currently supports"""
    return get_paystack_wrapper().miscellaneous.get_countries()
