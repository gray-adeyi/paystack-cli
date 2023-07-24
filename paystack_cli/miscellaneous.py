from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, colorized_print, override_output

miscellaneous_app = Typer()


@miscellaneous_app.command()
@colorized_print
@override_output
def get_providers(data_only: bool = False):
    return get_paystack_wrapper().miscellaneous.get_providers()


@miscellaneous_app.command()
@colorized_print
@override_output
def get_banks(data_only: bool = False):
    return get_paystack_wrapper().miscellaneous.get_banks()


@miscellaneous_app.command()
@colorized_print
@override_output
def get_states(data_only: bool = False):
    return get_paystack_wrapper().miscellaneous.get_states()


@miscellaneous_app.command()
@colorized_print
@override_output
def get_countries(data_only: bool = False):
    return get_paystack_wrapper().miscellaneous.get_countries()