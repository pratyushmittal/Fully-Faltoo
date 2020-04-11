#!/usr/bin/python3
import sys
import re
import statistics
import json
from collections import namedtuple
from decimal import Decimal, InvalidOperation


class CantParse(Exception):
    pass


Stat = namedtuple("Statistic", "title, result")


def _parse_decimals(values):
    values = [v.strip() for v in values]
    values = [v for v in values if v]
    try:
        values = [Decimal(v) for v in values]
    except InvalidOperation:
        raise CantParse("Unable to parse as Decimals", values)
    return values


def _parse_as_csv(value):
    values = value.split(",")
    return _parse_decimals(values)


def _parse_numbers(value):
    value = value.replace(",", "")
    value = value.replace("\t", " ")
    value = value.replace("\n", " ")
    value = value.replace("%", " ")
    # replace all other characters with spaces
    pattern = "[^-0-9.]"
    value = re.sub(pattern, value, " ")
    values = value.split(" ")
    return _parse_decimals(values)


def _generate_json(stats):
    structure = {
        "items": [
            {
                "title": stat.title,
                "subtitle": "{:.2f}".format(stat.result),
                # respond to click
                "valid": True,
            }
            for stat in stats
        ]
    }
    print(json.dumps(structure))


def _calculate(fn_name, values):
    fn = getattr(statistics, fn_name)
    return fn(values)


if __name__ == "__main__":
    value = sys.argv[1]
    try:
        values = _parse_as_csv(value)
    except CantParse:
        values = _parse_numbers(value)

    calculations = ["median", "mean"]
    stats = [Stat(fn, _calculate(fn, values)) for fn in calculations]
    _generate_json(stats)
