import pytest

from csv_analyzer.stats import average, count, max, median, min, sum


class TestStats:
    @pytest.mark.parametrize(
        ("table", "expected"),
        [
            ([["Header"], [1], [2], [3], [4]], 2.5),
            ([["Header"], [10]], 10.0),
        ],
    )
    def test_average_returns_expected_value(self, table, expected):
        assert average(table, 0) == expected

    def test_average_returns_error_for_empty_table(self):
        assert average([], 0) == "ERROR - EMPTY TABLE"

    @pytest.mark.parametrize(
        ("table", "expected"),
        [
            ([["Header"], [3], [1], [2]], 2.0),
            ([["Header"], [1], [2], [3], [4]], 2.5),
        ],
    )
    def test_median_returns_expected_value(self, table, expected):
        assert median(table, 0) == expected

    def test_median_returns_error_for_empty_table(self):
        assert median([], 0) == "ERROR - EMPTY TABLE"

    def test_min_returns_smallest_value(self):
        assert min([["Header"], [4], [1], [3]], 0) == 1.0

    def test_max_returns_largest_value(self):
        assert max([["Header"], [4], [1], [3]], 0) == 4.0

    def test_count_returns_number_of_data_rows(self):
        assert count([["Header"], [4], [1], [3]], 0) == 3

    def test_sum_returns_total_of_column(self):
        assert sum([["Header"], [4], [1], [3]], 0) == 8.0

    @pytest.mark.parametrize("stat_func", [average, median, min, max, count, sum])
    def test_all_functions_return_error_for_non_numeric_column(self, stat_func):
        table = [["Header"], ["abc"], [2]]
        assert stat_func(table, 0) == "ERROR - COLUMN CONTAINS NON NUMERIC VALUES"

    @pytest.mark.parametrize("stat_func", [average, median, min, max, count, sum])
    def test_all_functions_return_error_when_table_has_only_header(self, stat_func):
        table = [["Header"]]
        assert stat_func(table, 0) == "ERROR - TABLE HAS NO COLUMNS(WE ASSUME THE FIRST ROW IS A HEADER)"
