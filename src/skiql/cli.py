import tomllib

import click

from skiql.run_files import run_all_files

DEFAULT_CFG = ".skiql"


def configure(ctx, param, filename):
    try:
        with open(filename, "rb") as file:
            cfg = tomllib.load(file)
            options = dict(cfg["options"])
    except (KeyError, FileNotFoundError):
        options = {}
    ctx.default_map = options


@click.command()
@click.argument("folders", nargs=-1)
@click.option(
    "-c",
    "--config",
    type=click.Path(dir_okay=False),
    default=DEFAULT_CFG,
    callback=configure,
    is_eager=True,
    expose_value=False,
    help="Read option defaults from the specified toml file",
    show_default=True,
)
@click.option("--connection_string", required=True, help="Connection string")
@click.option("--max_tries", default=2, help="Maximum number of retries")
def cli(folders, connection_string, max_tries):
    failed_files = run_all_files(folders, connection_string, max_tries)

    if failed_files:
        print("Unable to run all files:")
        for file in failed_files:
            print(str(file))
