# flake8: noqa
import pytest # type: ignore
from validator import validate_last_name

def test_input_less_than_3_characters():
    assert not validate_last_name("Li")

def test_input_starts_with_hyphen():
    assert not validate_last_name("-Johnson")

def test_input_ends_with_hyphen():
    assert not validate_last_name("Johnson-")

def test_input_contains_consecutive_hyphens():
    assert not validate_last_name("John--son")

def test_input_contains_invalid_characters():
    assert not validate_last_name("John$on")

def test_valid_input():
    assert validate_last_name("Smith")
    assert validate_last_name("O'Connor")
    assert validate_last_name("Li")
