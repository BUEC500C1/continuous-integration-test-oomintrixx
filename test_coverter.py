from converter import *
import pytest


def test_distance():

    assert distanceConvert(1, "m", "ft") == 3.28084
    assert distanceConvert(1, "inches", "feets") == 0.08333329100002286
    assert distanceConvert(1, "miles", "meters") == 1609.3444978925634

def test_weight():

    assert weightConvert(1, "kg", "ounces") == 35.274
    assert weightConvert(1, "kg", "pounds") == 2.20462
    assert weightConvert(1, "ounces", "pounds") == 0.06249985825253727

def test_temperature():

    assert temperatureConvert(-40, "F", "C") == -40.0
    assert temperatureConvert(80, "Fahrenheit", "Celcius") == 26.666666666666668

def test_converter():

    assert unitConverter("what is 56 KG in pounds ?") == "123.45871999999999 pounds"
    assert unitConverter("convert 12.5 miles to meters") == "20116.80622365704 meters"
