from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit,
)

def test_convertCelsiusToKelvin():
    test_cases = [
        (0, 273.15),
        (100, 373.15),
        (-273.15, 0),
        (300, 573.15),
        (25, 298.15),
    ]
    for celsius, expected in test_cases:
        result = convertCelsiusToKelvin(celsius)
        assert abs(result - expected) < 0.01, f"Failed: {celsius}C -> {result}K, Expected: {expected}K"
        print(f"Passed: {celsius}C -> {result}K")

def test_convertCelsiusToFahrenheit():
    test_cases = [
        (0, 32),
        (100, 212),
        (-40, -40),
        (300, 572),
        (25, 77),
    ]
    for celsius, expected in test_cases:
        result = convertCelsiusToFahrenheit(celsius)
        assert abs(result - expected) < 0.01, f"Failed: {celsius}C -> {result}F, Expected: {expected}F"
        print(f"Passed: {celsius}C -> {result}F")

def test_convertFahrenheitToCelsius():
    test_cases = [
        (32, 0),
        (212, 100),
        (-40, -40),
        (572, 300),
        (77, 25),
    ]
    for fahrenheit, expected in test_cases:
        result = convertFahrenheitToCelsius(fahrenheit)
        assert abs(result - expected) < 0.01, f"Failed: {fahrenheit}F -> {result}C, Expected: {expected}C"
        print(f"Passed: {fahrenheit}F -> {result}C")

def test_convertFahrenheitToKelvin():
    test_cases = [
        (32, 273.15),
        (212, 373.15),
        (-40, 233.15),
        (572, 573.15),
        (77, 298.15),
    ]
    for fahrenheit, expected in test_cases:
        result = convertFahrenheitToKelvin(fahrenheit)
        assert abs(result - expected) < 0.01, f"Failed: {fahrenheit}F -> {result}K, Expected: {expected}K"
        print(f"Passed: {fahrenheit}F -> {result}K")

def test_convertKelvinToCelsius():
    test_cases = [
        (273.15, 0),
        (373.15, 100),
        (0, -273.15),
        (573.15, 300),
        (298.15, 25),
    ]
    for kelvin, expected in test_cases:
        result = convertKelvinToCelsius(kelvin)
        assert abs(result - expected) < 0.01, f"Failed: {kelvin}K -> {result}C, Expected: {expected}C"
        print(f"Passed: {kelvin}K -> {result}C")

def test_convertKelvinToFahrenheit():
    test_cases = [
        (273.15, 32),
        (373.15, 212),
        (0, -459.67),
        (573.15, 572),
        (298.15, 77),
    ]
    for kelvin, expected in test_cases:
        result = convertKelvinToFahrenheit(kelvin)
        assert abs(result - expected) < 0.01, f"Failed: {kelvin}K -> {result}F, Expected: {expected}F"
        print(f"Passed: {kelvin}K -> {result}F")

# Run all tests
if __name__ == "__main__":
    test_convertCelsiusToKelvin()
    test_convertCelsiusToFahrenheit()
    test_convertFahrenheitToCelsius()
    test_convertFahrenheitToKelvin()
    test_convertKelvinToCelsius()
    test_convertKelvinToFahrenheit()
