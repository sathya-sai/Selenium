"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium setup method
"""
import pytest


@pytest.fixture()
def setup():
    print("once before every method")


def testmethod1(setup):
    print("method 1")


def testmethod2(setup):
    print("method 2")
