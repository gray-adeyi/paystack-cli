from typer import Typer
from rich import print as rprint

from paystack_cli.charge import charge_app
from paystack_cli.miscellaneous import miscellaneous_app
from paystack_cli.apple_pay import app_pay_app
from paystack_cli.bulk_charges import bulk_charge_app
from paystack_cli.customers import customer_app
from paystack_cli.dedicated_virtual_accounts import dva_app
from paystack_cli.disputes import dispute_app
from paystack_cli.integration import integration_app
from paystack_cli.payment_pages import payment_page_app
from paystack_cli.payments_requests import payment_request_app
from paystack_cli.plans import plan_app
from paystack_cli.products import product_app
from paystack_cli.refunds import refund_app
from paystack_cli.settlements import settlement_app
from paystack_cli.subaccounts import subaccount_app
from paystack_cli.subscriptions import subscription_app
from paystack_cli.terminals import terminal_app
from paystack_cli.transactions import transaction_app
from paystack_cli.transactions_splits import transaction_split_app
from paystack_cli.transfer_recipients import transfer_recipient_app
from paystack_cli.transfers import transfer_app
from paystack_cli.transfers_control import transfer_control_app
from paystack_cli.utils import reset_settings, update_settings
from paystack_cli.verification import verification_app

app = Typer(
    name="Paystack", help="A command line utility for interacting with Paystack's API"
)

app.add_typer(
    transaction_app,
    name="txn",
    help=(
        "The `txn` subcommand interacts with the Transactions API"
        " which allows you to create and manage payments on your integration."
    ),
)
app.add_typer(
    transaction_split_app,
    name="splits",
    help=(
        "The `splits` subcommand interacts with the Transaction Splits API"
        " which enables merchants split the settlement for a transaction"
        " across their payout account, and one or more Subaccounts."
    ),
)
app.add_typer(
    terminal_app,
    name="terminals",
    help=(
        "The `terminals` subcommand interacts with Terminal API"
        " which allows you to build delightful in-person payment experiences."
    ),
)
app.add_typer(
    customer_app,
    name="customers",
    help=(
        "The `customers` subcommand interacts with Customers API "
        "and allows you to create and manage customers in your integration."
    ),
)
app.add_typer(
    dva_app,
    name="dva",
    help=(
        "The `dva` subcommand interacts with Dedicated Virtual Account "
        "API enables Nigerian merchants to manage unique payment accounts of their customers."
    ),
)
app.add_typer(
    app_pay_app,
    name="apple-pay",
    help=(
        "The `apple-pay` subcommand interacts with the Apple Pay API "
        "and allows you register your application's top-level domain or subdomain."
    ),
)
app.add_typer(
    subaccount_app,
    name="subacounts",
    help=(
        "The `subacounts` subcommand interacts with Subaccounts API which "
        "allows you to create and manage subaccounts on your integration. "
        "Subaccounts can be used to split payment between two accounts (your"
        " main account and a sub account)."
    ),
)
app.add_typer(
    plan_app,
    name="plans",
    help=(
        "The `plans` subcommand interacts with Plans API which allows"
        " you to create and manage installment payment options on your integration."
    ),
)
app.add_typer(
    subscription_app,
    name="subs",
    help=(
        "The `subs` subcommand interacts with Subscriptions API "
        "which allows you to create and manage recurring payment on your integration."
    ),
)
app.add_typer(
    product_app,
    name="products",
    help=(
        "The `products` subcommand interacts with Products API"
        " which allows you to create and manage inventories on your integration."
    ),
)
app.add_typer(
    payment_page_app,
    name="pp",
    help=(
        "The `pp` subcommand interacts with Payment Pages API"
        " and provides a quick and secure way to collect payment for products."
    ),
)
app.add_typer(
    payment_request_app,
    name="pr",
    help=(
        "The `pr` subcommand interacts with Payment Requests API"
        " which allows you to manage requests for payment of goods and services."
    ),
)
app.add_typer(
    settlement_app,
    name="settlements",
    help=(
        "The `settlements` subcommand interacts with the Settlements API"
        " which allows you gain insights into payouts made by Paystack to your bank account."
    ),
)
app.add_typer(
    transfer_recipient_app,
    name="tr",
    help=(
        "The `tr` subcommand interacts with Transfer Recipients API"
        " which allows you to create and manage beneficiaries that you send money to."
    ),
)
app.add_typer(
    transfer_app,
    name="transfers",
    help=(
        "The `transfers` subcommand interacts with Transfers API"
        " which allows you to automate sending money on your integration"
    ),
)
app.add_typer(
    transfer_control_app,
    name="transfer-ctrl",
    help=(
        "The `transfer-ctrl` subcommand interacts with Transfers Control API"
        " which allows you to manage settings of your transfers."
    ),
)
app.add_typer(
    bulk_charge_app,
    name="bc",
    help=(
        "The `bc` subcommand interacts with the Bulk Charges API and "
        "allows you to create and manage multiple recurring payments for your customers."
    ),
)
app.add_typer(
    integration_app,
    name="integration",
    help=(
        "The `integration` subcommand interacts with Integration API"
        " and allows you to manage some settings on your integration."
    ),
)
app.add_typer(
    charge_app,
    name="charge",
    help=(
        "The `charge` subcommand interacts with Charge API allows and "
        "you to configure a payment channel of your choice when initiating a payment."
    ),
)
app.add_typer(
    dispute_app,
    name="disputes",
    help="The Disputes API allows you manage transaction disputes on your integration.",
)
app.add_typer(
    refund_app,
    name="refunds",
    help=(
        "The `refunds` subcommand interacts with Refunds API"
        " which allows you to create and manage transaction refunds."
    ),
)
app.add_typer(
    verification_app,
    name="verification",
    help="The `verification` subcommand interacts with Verification API which allows you to perform KYC processes.",
)
app.add_typer(
    miscellaneous_app,
    name="misc",
    help=(
        "The `misc` subcommand interacts with Miscellaneous API which is a "
        "supporting API that can be used to provide more details to other APIs."
    ),
)


@app.command()
def config(auth_key: str):
    """Configure auth key"""
    update_settings(option="auth_key", value=auth_key)
    rprint("auth key saved! :boom:")


@app.command()
def reset():
    """Reset auth key"""
    reset_settings()
    rprint("auth key cleared! :boom:")


@app.command()
def version():
    """See CLI version"""
    rprint("Paystack CLI Version 0.1.2")


def run():
    app()


if __name__ == "__main__":
    run()
