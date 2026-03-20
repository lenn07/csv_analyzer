import argparse
from unittest import result
from csv_analyzer import load_csv
from csv_analyzer import average
from csv_analyzer import median
from csv_analyzer import min
from csv_analyzer import max
from csv_analyzer import count
from csv_analyzer import sum
from csv_analyzer import mode
from csv_analyzer import variance
from csv_analyzer import std_dev
from csv_analyzer.transform import headerToIndex


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("file")
    parser.add_argument("column")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--average", action="store_true")
    group.add_argument("--median", action="store_true")
    group.add_argument("--min", action="store_true")
    group.add_argument("--max", action="store_true")
    group.add_argument("--sum", action="store_true")
    group.add_argument("--count", action="store_true")
    group.add_argument("--mode", action="store_true")
    group.add_argument("--variance", action="store_true")
    group.add_argument("--std-dev", action="store_true")
    group.add_argument("--all", action="store_true")

    args = parser.parse_args()

    table = load_csv(args.file)

    args.column = headerToIndex(table, args.column)

    if args.average:
        result = average(table, args.column)
    elif args.median:
        result = median(table, args.column)
    elif args.min:
        result = min(table, args.column)
    elif args.max:
        result = max(table, args.column)
    elif args.sum:
        result = sum(table, args.column)
    elif args.count:
        result = count(table, args.column)
    elif args.mode:
        result = mode(table, args.column)
    elif args.variance:
        result = variance(table, args.column)
    elif args.std_dev:
        result = std_dev(table, args.column)
    elif args.all:
        result = {
            "average": average(table, args.column),
            "median": median(table, args.column),
            "min": min(table, args.column),
            "max": max(table, args.column),
            "sum": sum(table, args.column),
            "count": count(table, args.column),
            "mode": mode(table, args.column),
            "variance": variance(table, args.column),
            "std_dev": std_dev(table, args.column),
        }

    if isinstance(result, dict):
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(result)       

if __name__ == "__main__":
    main()