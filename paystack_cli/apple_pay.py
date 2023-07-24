from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, override_output, colorized_print

app_pay_app = Typer()


@app_pay_app.command()
@colorized_print
@override_output
def get_domains(data_only: bool = False):
    """Fetches all registered domains on your integration.

    Returns an empty array if no domains have been added.
    """
    return get_paystack_wrapper().apple_pay.get_domains()


@app_pay_app.command()
@colorized_print
@override_output
def register_domain(domain_name: str, data_only: bool = False):
    """Register a top-level domain or subdomain for your Apple Pay integration.

    This method can only be called with one domain or subdomain at a time.
    """
    return get_paystack_wrapper().apple_pay.register_domain(domain_name=domain_name)


@app_pay_app.command()
@colorized_print
@override_output
def unregister_domain(domain_name: str, data_only: bool = False):
    """Unregister a top-level domain or subdomain previously used for your Apple Pay integration."""
    return get_paystack_wrapper().apple_pay.unregister_domain(domain_name=domain_name)
