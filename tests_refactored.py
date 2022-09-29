from conversions_refactored import convert, ConversionNotPossible

def test_convert():
    assert convert("celsius", "kelvin", 0) == 273.15
    assert convert("celsius", "fahrenheit", 100) == 212
    assert convert("meters", "yards", 1) == 1.09361
    assert convert("yards", "meters", 1.09361) == 1

    # Test same unit conversion
    assert convert("celsius", "celsius", 100) == 100

    # Test invalid conversion
    try:
        convert("celsius", "meters", 0)
    except ConversionNotPossible:
        print("Passed invalid conversion test")
    else:
        assert False, "Failed invalid conversion test"

if __name__ == "__main__":
    test_convert()