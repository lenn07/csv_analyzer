import argparse
from csv_analyzer import load_csv
from csv_analyzer import average
from csv_analyzer import median
from csv_analyzer import min
from csv_analyzer import max
from csv_analyzer import count
from csv_analyzer import sum


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("file")
    parser.add_argument("column", type=int)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--average", action="store_true")
    group.add_argument("--median", action="store_true")
    group.add_argument("--min", action="store_true")
    group.add_argument("--max", action="store_true")
    group.add_argument("--sum", action="store_true")
    group.add_argument("--count", action="store_true")

    args = parser.parse_args()

    table = load_csv(args.file)

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

    print(result)

if __name__ == "__main__":
    main()