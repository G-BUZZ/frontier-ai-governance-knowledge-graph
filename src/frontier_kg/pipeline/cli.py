"""
Frontier KG command line interface.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from frontier_kg.validation.validator import Validator


def validate():

    validator = Validator(Path("data"))

    result = validator.validate()

    if result.valid:

        print("✓ Validation successful")

        return

    print()

    print("Validation failed")

    print()

    for error in result.errors:

        print(f"- {error.location}: {error.message}")


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(

        "command",

        choices=["validate", "build", "export"],

    )

    args = parser.parse_args()

    if args.command == "validate":

        validate()

        return

    print(f"{args.command} not implemented yet.")


if __name__ == "__main__":

    main()
