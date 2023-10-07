from .errors import *

class HexCode():
    def __init__(self, value: str):
        # checking hex code
        if not isinstance(value, (str, HexCode)):
            raise TypeError(f"HexCode values can only be 'str' or 'HexCode' not '{type(value).__name__}'")
        if not str(value).startswith("#"):
            raise HexFormatError("HexCode values must start with a #")
        if len(str(value)) != 7:
            raise HexFormatError(f"HexCode values usually are 7 characters long not {len(str(value))}")
        # Initialization
        self._value = str(value)
    def __str__(self) -> str:
        return self._value.upper()
    
class RgbCode():
    def __init__(self, red, green, blue):
        if not isinstance(red, int):
            raise TypeError(f"RgbCode red value can only be 'int' not '{type(red).__name__}'")
        if not isinstance(green, int):
            raise TypeError(f"RgbCode green value can only be 'int' not '{type(green).__name__}'")
        if not isinstance(blue, int):
            raise TypeError(f"RgbCode blue value can only be 'int' not '{type(blue).__name__}'")
        self._value = (red, green, blue)
    def __str__(self) -> str:
        return f"({self._value[0]}, {self._value[1]}, {self._value[2]})"