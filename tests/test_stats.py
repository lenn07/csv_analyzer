from csv_analyzer.stats import average, median
import pytest


def test_average_of_numbers():
    assert average([["Header"], [1], [2], [3], [4]], 0) == 2.5


def test_average_single_value():
    assert average([["Header"], [10]], 0) == 10


def test_average_empty_list_raises_error():
    assert average([], 0) == "ERROR - EMPTY TABLE"


def test_median_odd_count():
    assert median([["Header"], [3], [1], [2]], 0) == 2


def test_median_even_count():
    assert median([["Header"], [1], [2], [3], [4]], 0) == 2.5


def test_median_empty_list_raises_error():
    assert median([], 0) == "ERROR - EMPTY TABLE"