from typing import Optional

from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, parse_cli_string

charge_app = Typer()


@charge_app.command(name="")
def charge(
    email: str,
    amount: int,
    bank: Optional[str] = None,
    auth_code: Optional[str] = None,
    pin: Optional[str] = None,
    metadata: Optional[str] = None,
    reference: Optional[str] = None,
    ussd: Optional[str] = None,
    mobile_money: Optional[str] = None,
    device_id: Optional[str] = None,
    birthday: Optional[str] = None,
):
    if bank:
        bank = parse_cli_string(
            raw_string=bank, arg_or_option_name="bank", expected_type=dict
        )
    if metadata:
        metadata = parse_cli_string(
            raw_string=metadata, arg_or_option_name="metadata", expected_type=dict
        )
    if ussd:
        ussd = parse_cli_string(
            raw_string=ussd, arg_or_option_name="ussd", expected_type=dict
        )
    if mobile_money:
        mobile_money = parse_cli_string(
            raw_string=mobile_money,
            arg_or_option_name="mobile_money",
            expected_type=dict,
        )
    return get_paystack_wrapper().charge.charge(
        email=email,
        amount=amount,
        bank=bank,
        auth_code=auth_code,
        pin=pin,
        metadata=metadata,
        reference=reference,
        ussd=ussd,
        mobile_money=mobile_money,
        device_id=device_id,
        birthday=birthday,
    )


@charge_app.command()
def check_pending_charge(reference: str):
    return get_paystack_wrapper().charge.check_pending_charge(reference=reference)


@charge_app.command()
def submit_otp(otp: str, reference: str):
    return get_paystack_wrapper().charge.submit_otp(otp=otp, reference=reference)


@charge_app.command()
def submit_pin(pin: str, reference: str):
    return get_paystack_wrapper().charge.submit_pin(pin=pin, reference=reference)


@charge_app.command()
def set_address(address: str, reference: str, city: str, state: str, zipcode: str):
    return get_paystack_wrapper().charge.set_address(
        address=address, reference=reference, city=city, state=state, zipcode=zipcode
    )


@charge_app.command()
def submit_phone(phone: str, reference: str):
    return get_paystack_wrapper().charge.submit_phone(phone=phone, reference=reference)


@charge_app.command()
def submit_birthday(birthday: str, reference: str):
    return get_paystack_wrapper().charge.submit_birthday(
        birthday=birthday, reference=reference
    )
