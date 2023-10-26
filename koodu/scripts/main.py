import argparse

from koodu.scripts.checks import check_templates, list_command
from koodu.scripts.generate import generate


def print_koodu():
    print("╔═══════════════════════════════════════════════════╗")
    print("║                  KOODU CLI TOOLS                  ║")
    print("║   Simple and lightweight code generator engine.   ║")
    print("╠═══════════════════════════════════════════════════╣")
    print("║ Options:                                          ║")
    print("║                                                   ║")
    print("║ 1. generate                                       ║")
    print("║ 2. list                                           ║")
    print("║ 3. check                                          ║")
    print("╚═══════════════════════════════════════════════════╝")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="koodu CLI Tool - Simple and lightweight code generator engine.",
        usage="koodu [options] arguments",
    )
    subparser = parser.add_subparsers(dest="command", help="The command to execute")
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
        output = check_templates(args)
        print("\n".join(output))
    elif args.command == "list":
        output = list_command(args)
        print("\n".join(output))


if __name__ == "__main__":
    main()
