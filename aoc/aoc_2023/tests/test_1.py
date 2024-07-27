import pytest

from aoc.aoc_2023.day1 import main1


def test_main1_example():
    assert main1("inputs/2023/1_example.txt") == 142


def test_main1():
    assert main1("inputs/2023/1.txt") == 55607
