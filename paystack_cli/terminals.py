from typing import Optional

from pypaystack2 import TerminalEvent, TerminalEventAction
from typer import Typer

from paystack_cli.utils import (
    get_paystack_wrapper,
    parse_cli_string,
    override_output,
    colorized_print,
)

terminal_app = Typer()


@terminal_app.command()
@colorized_print
@override_output
def get_terminal(terminal_id: str, data_only: bool = False):
    """Get the details of a Terminal"""
    return get_paystack_wrapper().terminals.get_terminal(terminal_id=terminal_id)


@terminal_app.command()
@colorized_print
@override_output
def get_terminals(
    pagination: int = 50,
    next: Optional[str] = None,
    previous: Optional[str] = None,
    data_only: bool = False,
):
    """List the Terminals available on your integration"""
    return get_paystack_wrapper().terminals.get_terminals(
        pagination=pagination, next=next, previous=previous
    )


@terminal_app.command()
@colorized_print
@override_output
def get_terminal_status(terminal_id: str, data_only: bool = False):
    """Check the availability of a Terminal before sending an event to it."""
    return get_paystack_wrapper().terminals.get_terminal_status(terminal_id=terminal_id)


@terminal_app.command()
@colorized_print
@override_output
def update_terminal(terminal_id: str, name: str, address: str, data_only: bool = False):
    """Update the details of a Terminal"""
    return get_paystack_wrapper().terminals.updated_terminal(
        terminal_id=terminal_id, name=name, address=address
    )


@terminal_app.command()
@colorized_print
@override_output
def commission_terminal(serial_number: str, data_only: bool = False):
    """Activate your debug device by linking it to your integration"""
    return get_paystack_wrapper().terminals.commission_terminal(
        serial_number=serial_number
    )


@terminal_app.command()
@colorized_print
@override_output
def decommission_terminal(serial_number: str, data_only: bool = False):
    """Unlink your debug device from your integration"""
    return get_paystack_wrapper().terminals.decommission_terminal(
        serial_number=serial_number
    )


@terminal_app.command()
@colorized_print
@override_output
def get_event_status(terminal_id: str, event_id: str, data_only: bool = False):
    """Check the status of an event sent to the Terminal"""
    return get_paystack_wrapper().terminals.get_event_status(
        terminal_id=terminal_id, event_id=event_id
    )


@terminal_app.command()
@colorized_print
@override_output
def send_event(
    terminal_id: str,
    type: TerminalEvent,
    action: TerminalEventAction,
    data: str,
    data_only: bool = False,
):
    """Send an event from your application to the Paystack Terminal"""
    data = parse_cli_string(
        raw_string=data, arg_or_option_name="data", expected_type=dict
    )
    return get_paystack_wrapper().terminals.send_event(
        terminal_id=terminal_id, type=type, action=action, data=data
    )
