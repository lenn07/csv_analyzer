import argparse
import json
from csv_analyzer import load_csv
from csv_analyzer import average
from csv_analyzer import median
from csv_analyzer import min as csv_min
from csv_analyzer import max as csv_max
from csv_analyzer import count
from csv_analyzer import sum as csv_sum
from csv_analyzer import mode
from csv_analyzer import variance
from csv_analyzer import std_dev
from csv_analyzer.transform import headerToIndex
from csv_analyzer.transform import extractIndexOfNumericColumn


def format_text(results):
    if len(results) == 1:
        return str(next(iter(results.values())))

    lines = []
    for key, value in results.items():
        lines.append(f"{key}: {value}")
    return "\n".join(lines)


def format_json(results):
    return json.dumps(results, indent=2, ensure_ascii=False)


def render_output(results, output_format):
    if output_format == "json":
        return format_json(results)
    return format_text(results)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("file")
    parser.add_argument("column", nargs="?")

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
    group.add_argument("--analyzeAll", action="store_true")

    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text"
    )

    args = parser.parse_args()

    table = load_csv(args.file)
    results = {}

    if args.analyzeAll:
        numeric_columns = extractIndexOfNumericColumn(table)

        for column_index in numeric_columns:
            column_name = table[0][column_index]
            results[column_name] = {
                "average": average(table, column_index),
                "median": median(table, column_index),
                "min": csv_min(table, column_index),
                "max": csv_max(table, column_index),
                "sum": csv_sum(table, column_index),
                "count": count(table, column_index),
                "mode": mode(table, column_index),
                "variance": variance(table, column_index),
                "std_dev": std_dev(table, column_index),
            }
    else:
        if args.column is None:
            parser.error("column is required unless --analyzeAll is used")

        column_index = headerToIndex(table, args.column)

        if args.all or args.average:
            results["average"] = average(table, column_index)
        if args.all or args.median:
            results["median"] = median(table, column_index)
        if args.all or args.min:
            results["min"] = csv_min(table, column_index)
        if args.all or args.max:
            results["max"] = csv_max(table, column_index)
        if args.all or args.sum:
            results["sum"] = csv_sum(table, column_index)
        if args.all or args.count:
            results["count"] = count(table, column_index)
        if args.all or args.mode:
            results["mode"] = mode(table, column_index)
        if args.all or args.variance:
            results["variance"] = variance(table, column_index)
        if args.all or args.std_dev:
            results["std_dev"] = std_dev(table, column_index)

    print(render_output(results, args.format))


if __name__ == "__main__":
    main()
