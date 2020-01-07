"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium setup and yield method
"""
import pytest


@pytest.yield_fixture()
def setup():
    print("once before every method")
    yield
    print("once after every method")


def test_method1(setup):
    print("method1")


def test_method2(setup):
    print("method2")
