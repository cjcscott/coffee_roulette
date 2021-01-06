"""Console script for coffee_roulette."""
import sys
import click
from . import coffee_roulette

@click.command()
@click.argument("names", required=True, nargs = -1, type=str)#, help="List of names to separate.")
@click.option("--minsize", required=False, default = 2, type=int, show_default=True, help="Minimum size of any group.")
@click.option("--maxsize", required=False, default = 4, type=int, show_default=True, help="Maximum size of any group.")
@click.option("-p","partitioning", required=False, default="max",
                type=click.Choice(['min', 'max'], case_sensitive=False), show_default=True,
                help="Approach to use to partition the list of names.")
def main(names, minsize, maxsize, partitioning):
    """A quick script to generate a random separation of a list of names for the sake of zoom coffees."""
    cofgen = coffee_roulette.CoffeeGenerator(names, minsize, maxsize)
    split = cofgen.run(partitioning)
    print("Determined splitting:")
    for i in split:
        print(i)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
