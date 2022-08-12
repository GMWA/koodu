import argparse

from koodu.scripts.generate import generate
from koodu.scripts.checks import check_templates

def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")
    gen = subparser.add_parser("generate")
    check = subparser.add_parser("check")
    
    gen.add_argument(
        "--templates",
        "-t",
        type=str,
        required=True,
        help="The Path to the folder that contents the template's files."
    )
    gen.add_argument(
        "--model",
        "-m",
        type=str,
        required=True,
        help="The Path to the model file(it should be a json file.)"
    )
    gen.add_argument(
        "--output",
        "-o",
        type=str,
        required=True,
        help="The Path to the output files."
    )

    check.add_argument(
        "--folder",
        "-f",
        type=str,
        required=True,
        help="The Path to the folder that contents the template's files."
    )

    args = parser.parse_args()

    if args.option == "generate":
        generate(args)
    elif args.command == "check":
        check_templates(args)


if __name__ == "__main__":
    main