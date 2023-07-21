from typer import Typer

from paystack_cli.utils import get_paystack_wrapper

app_pay_app = Typer()


@app_pay_app.command()
def get_domains():
    return get_paystack_wrapper().apple_pay.get_domains()


@app_pay_app.command()
def register_domain(domain_name: str):
    return get_paystack_wrapper().apple_pay.register_domain(domain_name=domain_name)


@app_pay_app.command()
def unregister_domain(domain_name: str):
    return get_paystack_wrapper().apple_pay.unregister_domain(domain_name=domain_name)
