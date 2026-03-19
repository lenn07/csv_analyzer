import argparse
from csv_analyzer import load_csv
from csv_analyzer import average
from csv_analyzer import median


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("file")
    parser.add_argument("column", type=int)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--average", action="store_true")
    group.add_argument("--median", action="store_true")

    args = parser.parse_args()

    table = load_csv(args.file)

    if args.average:
        result = average(table, args.column)
    elif args.median:
        result = median(table, args.column)

    print(result)

if __name__ == "__main__":
    main()