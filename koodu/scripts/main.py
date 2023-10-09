import argparse

from koodu.scripts.checks import check_templates, list_command
from koodu.scripts.generate import generate


def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")
    gen = subparser.add_parser("generate")
    check = subparser.add_parser("check")
    _list = subparser.add_parser("list")

    gen.add_argument(
        "-t",
        "--templates",
        type=str,
        required=True,
        help="The Path to the folder that contents the template's files.",
    )
    gen.add_argument(
        "-m",
        "--model",
        type=str,
        required=True,
        help="The Path to the model file(it should be a json file.)",
    )
    gen.add_argument(
        "-o", "--output", type=str, required=True, help="The Path to the output files."
    )

    check.add_argument(
        "--folder",
        "-f",
        type=str,
        required=True,
        help="The Path to the folder that contents the template's files.",
    )

    _list.add_argument(
        "option",
        type=str,
        choices=["models", "m", "templates", "t"],
        help="The option: what you want to list(model(m) or template(t))",
    )

    args = parser.parse_args()

    if args.command == "generate":
        generate(args)
    elif args.command == "check":
        check_templates(args)
    elif args.command == "list":
        list_command(args)


if __name__ == "__main__":
    main()
