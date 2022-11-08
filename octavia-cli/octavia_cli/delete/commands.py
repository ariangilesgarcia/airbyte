#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#

import uuid
from typing import List, Optional, Tuple, Type, Union

import airbyte_api_client
import click
from octavia_cli.base_commands import OctaviaCommand

from .resources import Connection, Destination, Source


def build_help_message(resource_type: str) -> str:
    """Helper function to build help message consistently for all the commands in this module.

    Args:
        resource_type (str): source, destination or connection

    Returns:
        str: The generated help message.
    """
    return f"Delete a remote {resource_type}."


@click.group(
    "delete",
    help=f'{build_help_message("source, destination or connection")} ID or name can be used as argument. Example: \'octavia delete source "My Pokemon source"\' or \'octavia delete source cb5413b2-4159-46a2-910a-dc282a439d2d\'',
)
@click.pass_context
def delete(ctx: click.Context):  # pragma: no cover
    pass


@delete.command(cls=OctaviaCommand, name="source", help=build_help_message("source"))
@click.argument("resource", type=click.STRING)
@click.pass_context
def source(ctx: click.Context, resource: str):
    click.echo(click.style(f"🐙 - Deleting source {resource}.", fg="green"))


@delete.command(cls=OctaviaCommand, name="destination", help=build_help_message("destination"))
@click.argument("resource", type=click.STRING)
@click.pass_context
def destination(ctx: click.Context, resource: str):
    click.echo(click.style(f"🐙 - Deleting source {destination}.", fg="green"))


@delete.command(cls=OctaviaCommand, name="connection", help=build_help_message("connection"))
@click.argument("resource", type=click.STRING)
@click.pass_context
def connection(ctx: click.Context, resource: str):
    click.echo(click.style(f"🐙 - Deleting source {connection}.", fg="green"))


AVAILABLE_COMMANDS: List[click.Command] = [source, destination, connection]


def add_commands_to_list():
    for command in AVAILABLE_COMMANDS:
        delete.add_command(command)


add_commands_to_list()
