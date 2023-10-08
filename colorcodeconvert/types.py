from .errors import *

class HexCode():
    def __init__(self, value: str):
        # checking hex code
        if not isinstance(value, (str, HexCode)):
            raise TypeError(f"HexCode values can only be 'str' or 'HexCode' not '{type(value).__name__}'")
        if not str(value).startswith("#"):
            raise HexFormatError("HexCode values must start with a '#'")
        if len(str(value)) != 7:
            raise HexFormatError(f"HexCode values usually are 7 characters long not {len(str(value))}")
        for hexchar in value[1:]:
            if not hexchar in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f"):
                raise HexFormatError("at least one character in the HexCode isn't a Base16 character")
        # Initialization
        self._value = str(value).upper()
    def string(self):
        """
        Returns the set HexCode as a string.
        """
        return str(self._value)
    def __str__(self) -> str:
        return self._value
    def __repr__(self) -> str:
        return self.__str__()
    
class RgbCode():
    def __init__(self, red, green, blue):
        if not isinstance(red, int):
            raise TypeError(f"RgbCode red value can only be 'int' not '{type(red).__name__}'")
        if not isinstance(green, int):
            raise TypeError(f"RgbCode green value can only be 'int' not '{type(green).__name__}'")
        if not isinstance(blue, int):
            raise TypeError(f"RgbCode blue value can only be 'int' not '{type(blue).__name__}'")
        
        if red < 0 or red > 255:
            raise RgbFormatError(f"red parameter can only be an integer from 0 to 255")
        if green < 0 or green > 255:
            raise RgbFormatError(f"green parameter can only be an integer from 0 to 255")
        if blue < 0 or blue > 255:
            raise RgbFormatError(f"blue parameter can only be an integer from 0 to 255")
        self._value = (red, green, blue)
    def array(self):
        """
        Returns the set RgbCode as a tuple.
        """
        return self._value
    def string(self):
        """
        Returns the set RgbCode as a string.
        """
        return f"({self._value[0]}, {self._value[1]}, {self._value[2]})"
    def values(self):
        """
        Returns the set RgbCode as a dict.
        """
        return {"red":self._value[0], "green":self._value[1], "blue":self._value[2]}
    def __str__(self) -> str:
        return f"({self._value[0]}, {self._value[1]}, {self._value[2]})"
    def __repr__(self) -> str:
        return self.__str__()