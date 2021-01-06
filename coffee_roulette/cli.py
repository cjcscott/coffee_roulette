"""Console script for coffee_roulette."""
import sys
import click
from . import coffee_roulette

@click.command()
@click.argument("names", required=True, nargs = -1, type=string):
@click.argument("--min", "minsize", required=False, default = 2, type=int)
@click.argument("--max", "maxsize", required=False, default = 4, type=int)
@click.argument("-p","partitioning", required=False, default="max", 
def main(names, minsize, maxsize, partitioning):
    """Console script for coffee_roulette."""
    cofgen = coffee_roulette.CoffeeGenerator(names, minsize, maxsize)
    return cofgen.run(partitioning)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
