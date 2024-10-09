import click

from skiql.run_files import run_all_files


@click.command()
@click.argument("folders", nargs=-1)
@click.option("--connection_string", help="Connection string")
@click.option("--max_tries", default=2, help="Maximum number of retries")
def cli(folders, connection_string, max_tries):
    failed_files = run_all_files(folders, connection_string, max_tries)

    if failed_files:
        print("Unable to run all files:")
        for file in failed_files:
            print(str(file))
