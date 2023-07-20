from typing import Optional

from pypaystack2 import TerminalEvent, TerminalEventAction
from typer import Typer

from paystack_cli.utils import get_paystack_wrapper, parse_cli_string

terminal_app = Typer()


@terminal_app.command()
def get_terminal(terminal_id: str):
    return get_paystack_wrapper().terminals.get_terminal(terminal_id=terminal_id)


@terminal_app.command()
def get_terminals(
    pagination: int = 50, next: Optional[str] = None, previous: Optional[str] = None
):
    return get_paystack_wrapper().terminals.get_terminals(
        pagination=pagination, next=next, previous=previous
    )


@terminal_app.command()
def get_terminal_status(terminal_id: str):
    return get_paystack_wrapper().terminals.get_terminal_status(terminal_id=terminal_id)


@terminal_app.command()
def update_termial(terminal_id: str, name: str, address: str):
    return get_paystack_wrapper().terminals.updated_terminal(
        terminal_id=terminal_id, name=name, address=address
    )


@terminal_app.command()
def commission_terminal(serial_number: str):
    return get_paystack_wrapper().terminals.commission_terminal(
        serial_number=serial_number
    )


@terminal_app.command()
def decommission_terminal(serial_number: str):
    return get_paystack_wrapper().terminals.decommission_terminal(
        serial_number=serial_number
    )


@terminal_app.command()
def get_event_status(terminal_id: str, event_id: str):
    return get_paystack_wrapper().terminals.get_event_status(
        terminal_id=terminal_id, event_id=event_id
    )


@terminal_app.command()
def send_event(
    terminal_id: str, type: TerminalEvent, action: TerminalEventAction, data: str
):
    data = parse_cli_string(
        raw_string=data, arg_or_option_name="data", expected_type=dict
    )
    return get_paystack_wrapper().terminals.send_event(
        terminal_id=terminal_id, type=type, action=action, data=data
    )
