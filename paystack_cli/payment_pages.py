from typing import Optional, Union

from typer import Typer

from paystack_cli.utils import (
    get_paystack_wrapper,
    parse_cli_string,
    override_output,
    colorized_print,
)

payment_page_app = Typer()


@payment_page_app.command()
@colorized_print
@override_output
def create(
    name: str,
    description: Optional[str] = None,
    amount: Optional[int] = None,
    slug: Optional[str] = None,
    metadata: Optional[str] = None,
    redirect_url: Optional[str] = None,
    custom_fields: Optional[str] = None,
    data_only: bool = False,
):
    if custom_fields:
        custom_fields = parse_cli_string(
            raw_string=custom_fields,
            arg_or_option_name="custom_fields",
            expected_type=dict,
            many=True,
        )
    if metadata:
        metadata = parse_cli_string(
            raw_string=metadata, arg_or_option_name="metadata", expected_type=dict
        )
    return get_paystack_wrapper().payment_pages.create(
        name=name,
        description=description,
        amount=amount,
        slug=slug,
        metadata=metadata,
        redirect_url=redirect_url,
        custom_fields=custom_fields,
    )


@payment_page_app.command()
@colorized_print
@override_output
def update(
    id_or_slug: str,
    name: str,
    description: str,
    amount: int,
    active: Optional[bool] = None,
    data_only: bool = False,
):
    return get_paystack_wrapper().payment_pages.update(
        id_or_slug=id_or_slug,
        name=name,
        description=description,
        amount=amount,
        active=active,
    )


@payment_page_app.command()
@colorized_print
@override_output
def get_page(
    id_or_slug: str,
    data_only: bool = False,
):
    return get_paystack_wrapper().payment_pages.get_page(id_or_slug=id_or_slug)


@payment_page_app.command()
@colorized_print
@override_output
def get_pages(
    page: int = 1,
    pagination: int = 50,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    data_only: bool = False,
):
    """Fetch payment pages available on your integration."""
    return get_paystack_wrapper().payment_pages.get_pages(
        page=page, pagination=pagination, start_date=start_date, end_date=end_date
    )


@payment_page_app.command()
@colorized_print
@override_output
def add_products(
    id: str,
    products: list[str],
    data_only: bool = False,
):
    """Add products to a payment page"""
    return get_paystack_wrapper().payment_pages.add_products(id=id, products=products)


@payment_page_app.command()
@colorized_print
@override_output
def check_slug_available(
    slug: str,
    data_only: bool = False,
):
    """Check the availability of a slug for a payment page."""
    return get_paystack_wrapper().payment_pages.check_slug_available(slug=slug)
