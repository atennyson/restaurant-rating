import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument(
    "action",
    help="Action to run: add, remove, update, view",
    action="store",

)
parser.add_argument(
    "[restaurant_name]",
    help="Name of restaurant to add, update, view, or delete",
    action="store",
    default=argparse.SUPPRESS,
)
parser.add_argument(
    "[restaurant_rating]",
    type=int,
    help="Rating of restaurant to add",
    action="store",
    default=argparse.SUPPRESS,
)
parser.add_argument(
    "-f",
    "--ratings-filename",
    type=str,
    help="File containing ratings. Defaults to ratings.csv",
    action="store",
)
parser.add_argument(
    "-r",
    "--reverse",
    help="Sort results in reverse order.",
    action="store_true",
)
parser.add_argument(
    "-s",
    "--sortbyrating",
    help="Sort results by rating rather than name.",
    action="store_true",
)

args = parser.parse_args(sys.argv[1:])

print(f"action: {args.action}")
print(f"restaurant_name: {args.restaurant_name}")
print(f"restaurant_rating: {args.restaurant_rating}")
print(f"ratings_filename: {args.ratings_filename}")
print(f"reverse: {args.reverse}")
print(f"sortbyrating: {args.sortbyrating}")
