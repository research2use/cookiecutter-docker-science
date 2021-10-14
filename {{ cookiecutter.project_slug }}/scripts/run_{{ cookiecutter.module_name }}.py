from {{ cookiecutter.project_slug }}.{{ cookiecutter.module_name }} import sample
import argparse

import sys


def main():
    """Sample script"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "arg", type=int, help="Argument for sample."
    )
    args = parser.parse_args()
    sample(args.epochs)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover