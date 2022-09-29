class ConversionNotPossible(Exception):
    """Exception raised when conversion between units is not possible."""
    pass

def convert(from_unit, to_unit, value):
    conversions = {
        "celsius": {
            "kelvin": lambda c: c + 273.15,
            "fahrenheit": lambda c: c * 9/5 + 32,
        },
        "kelvin": {
            "celsius": lambda k: k - 273.15,
            "fahrenheit": lambda k: (k - 273.15) * 9/5 + 32,
        },
        "fahrenheit": {
            "celsius": lambda f: (f - 32) * 5/9,
            "kelvin": lambda f: (f - 32) * 5/9 + 273.15,
        },
        "meters": {
            "yards": lambda m: m * 1.09361,
            "miles": lambda m: m / 1609.34,
        },
        "yards": {
            "meters": lambda y: y / 1.09361,
            "miles": lambda y: y / 1760,
        },
        "miles": {
            "meters": lambda mi: mi * 1609.34,
            "yards": lambda mi: mi * 1760,
        },
    }

    if from_unit == to_unit:
        return value

    if from_unit not in conversions or to_unit not in conversions[from_unit]:
        raise ConversionNotPossible(f"Cannot convert {from_unit} to {to_unit}")

    return conversions[from_unit][to_unit](value)