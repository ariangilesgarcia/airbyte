#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#

import click
import octavia_cli.generate.definitions as definitions
from octavia_cli import resources
from octavia_cli.base_commands import OctaviaCommand
from octavia_cli.check_context import requires_init

# from .renderers import ConnectionRenderer, ConnectorSpecificationRenderer


@click.group("delete", help="Delete a source, destination or connection resource managed by octavia.")
@click.pass_context
@requires_init
def delete(ctx: click.Context):
    pass


# def generate_source_or_destination(definition_type, api_client, workspace_id, definition_id, resource_name):
#     definition = definitions.factory(definition_type, api_client, workspace_id, definition_id)
#     renderer = ConnectorSpecificationRenderer(resource_name, definition)
#     output_path = renderer.write_yaml(project_path=".")
#     message = f"✅ - Created the {definition_type} template for {resource_name} in {output_path}."
#     click.echo(click.style(message, fg="green"))


@delete.command(cls=OctaviaCommand, name="source", help="Delete a source.")
@click.argument("source_path", type=click.STRING)
@click.pass_context
def source(ctx: click.Context, source_path: str):
    # generate_source_or_destination("source", ctx.obj["API_CLIENT"], ctx.obj["WORKSPACE_ID"], definition_id, resource_name)
    source = resources.factory(ctx.obj["API_CLIENT"], ctx.obj["WORKSPACE_ID"], source_path)

    if not source.was_created:
        raise resources.NonExistingResourceError(
            f"Could not delete the source defined at {source_path}, it does not exist on your Airbyte instance."
        )

    source.delete()

    pass

@delete.command(cls=OctaviaCommand, name="destination", help="Delete a destination.")
@click.argument("destination_path", type=click.STRING)
@click.pass_context
def destination(ctx: click.Context, destination_path: str):
    # generate_source_or_destination("destination", ctx.obj["API_CLIENT"], ctx.obj["WORKSPACE_ID"], definition_id, resource_name)
    destination = resources.factory(ctx.obj["API_CLIENT"], ctx.obj["WORKSPACE_ID"], destination_path)
    pass

@delete.command(cls=OctaviaCommand, name="connection", help="Delete a connection.")
@click.argument("connection_path", type=click.STRING)
@click.pass_context
def connection(ctx: click.Context, connection_path: str):
    connection = resources.factory(ctx.obj["API_CLIENT"], ctx.obj["WORKSPACE_ID"], connection_path)

    # source = resources.factory(ctx.obj["API_CLIENT"], ctx.obj["WORKSPACE_ID"], source_path)
    # if not source.was_created:
    #     raise resources.NonExistingResourceError(
    #         f"The source defined at {source_path} does not exists. Please run octavia apply before creating this connection."
    #     )

    # destination = resources.factory(ctx.obj["API_CLIENT"], ctx.obj["WORKSPACE_ID"], destination_path)
    # if not destination.was_created:
    #     raise resources.NonExistingResourceError(
    #         f"The destination defined at {destination_path} does not exists. Please run octavia apply before creating this connection."
    #     )

    # connection_renderer = ConnectionRenderer(connection_name, source, destination)
    # output_path = connection_renderer.write_yaml(project_path=".")
    # message = f"✅ - Created the connection template for {connection_name} in {output_path}."
    # click.echo(click.style(message, fg="green"))
