import json
import os.path
from pathlib import Path
from typing import Optional

from rich import print as rprint
import typer
from pypaystack2 import Paystack
from typer import get_app_dir

APP_CONFIG_DIR_NAME = ".paystack-cli"

CACHED_SETTINGS: Optional[dict] = None


def get_settings_path() -> Path:
    app_dir = get_app_dir(APP_CONFIG_DIR_NAME)
    if not os.path.isdir(app_dir):
        os.mkdir(app_dir)
    return Path(app_dir) / ".settings.json"


def get_all_settings() -> dict:
    global CACHED_SETTINGS
    if CACHED_SETTINGS:
        return CACHED_SETTINGS
    settings_path = get_settings_path()
    if not settings_path.is_file():
        with settings_path.open("w+") as f:
            f.write(json.dumps({}))
    with settings_path.open("r") as f:
        CACHED_SETTINGS = json.loads(f.read())
        return CACHED_SETTINGS


def get_settings(option: str) -> Optional[str]:
    all_settings = get_all_settings()
    return all_settings.get(option)


def update_settings(option: str, value: str):
    all_settings = get_all_settings()
    all_settings[option] = value
    settings_path = get_settings_path()
    with settings_path.open("w") as f:
        f.write(json.dumps(all_settings))


def reset_settings():
    global CACHED_SETTINGS
    CACHED_SETTINGS = None
    settings_path = get_settings_path()
    with settings_path.open("w+") as f:
        f.write(json.dumps({}))


def get_paystack_wrapper() -> Paystack:
    auth_key = get_settings("auth_key")
    if not auth_key:
        rprint(
            "[bold red]Error![/bold red] your auth key has not been configured. please run `paystack config <auth_key>`"
        )
        raise typer.Abort()
    return Paystack(auth_key=auth_key)
