from typing import Optional

from pypaystack2 import Currency
from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, override_output, colorized_print

product_app = Typer()


@product_app.command()
@colorized_print
@override_output
def create(
    name: str,
    description: str,
    price: int,
    currency: Currency,
    unlimited: Optional[bool] = None,
    quantity: Optional[int] = None,
    data_only: bool = False,
):
    """Create a product on your integration"""
    return get_paystack_wrapper().products.create(
        name=name,
        description=description,
        price=price,
        currency=currency,
        unlimited=unlimited,
        quantity=quantity,
    )


@product_app.command()
@colorized_print
@override_output
def update(
    id: str,
    name: str,
    description: str,
    price: int,
    currency: Currency,
    unlimited: Optional[bool] = None,
    quantity: Optional[int] = None,
    data_only: bool = False,
):
    """Update a product details on your integration"""
    return get_paystack_wrapper().products.update(
        id=id,
        name=name,
        description=description,
        price=price,
        currency=currency,
        unlimited=unlimited,
        quantity=quantity,
    )


@product_app.command()
@colorized_print
@override_output
def get_product(id: str, data_only: bool = False):
    """Get details of a product on your integration."""
    return get_paystack_wrapper().products.get_product(id=id)


@product_app.command()
@colorized_print
@override_output
def get_products(
    page: int = 1,
    pagination: int = 50,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    data_only: bool = False,
):
    """Fetches products available on your integration."""
    return get_paystack_wrapper().products.get_products(
        page=page, pagination=pagination, start_date=start_date, end_date=end_date
    )
