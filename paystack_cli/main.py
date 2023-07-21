from typer import Typer
from rich import print as rprint

from paystack_cli.apple_pay import app_pay_app
from paystack_cli.customers import customer_app
from paystack_cli.dedicated_virtual_accounts import dva_app
from paystack_cli.plans import plan_app
from paystack_cli.subaccounts import subaccount_app
from paystack_cli.terminals import terminal_app
from paystack_cli.transactions import transaction_app
from paystack_cli.transactions_splits import transaction_split_app
from paystack_cli.utils import reset_settings, update_settings

app = Typer(
    name="Paystack", help="A command line utility for interacting with Paystack's API"
)
app.add_typer(transaction_app, name="txn")
app.add_typer(transaction_split_app, name="txn-split")
app.add_typer(terminal_app, name="terminals")
app.add_typer(customer_app, name="customers")
app.add_typer(dva_app, name="dva")
app.add_typer(app_pay_app, name="apple-pay")
app.add_typer(subaccount_app, name="subacounts")
app.add_typer(plan_app, name="plans")


@app.command()
def config(auth_key: str):
    update_settings(option="auth_key", value=auth_key)
    rprint("auth key saved! :boom:")


@app.command()
def reset():
    reset_settings()
    rprint("auth key cleared! :boom:")


@app.command()
def version():
    rprint("Paystack CLI Version 0.1.0")


def run():
    app()


if __name__ == "__main__":
    run()
