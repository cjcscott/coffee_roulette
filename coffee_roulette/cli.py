"""Console script for coffee_roulette."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for coffee_roulette."""
    click.echo("Replace this message by putting your code into "
               "coffee_roulette.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
