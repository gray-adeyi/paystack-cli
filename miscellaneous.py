from typer import Typer

from paystack_cli.utils import get_paystack_wrapper

miscellaneous_app = Typer()


@miscellaneous_app.command()
def get_providers():
    return get_paystack_wrapper().miscellaneous.get_providers()


@miscellaneous_app.command()
def get_banks():
    return get_paystack_wrapper().miscellaneous.get_banks()


@miscellaneous_app.command()
def get_states():
    return get_paystack_wrapper().miscellaneous.get_states()


@miscellaneous_app.command()
def get_countries():
    return get_paystack_wrapper().miscellaneous.get_countries()
