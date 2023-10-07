from .errors import *
from .colorcodes import *
from .types import *

def convert(input, to):
    if not to in (HEX, RGB): 
        raise TypeError(f"can only convert into HEX or RGB not {to}")
    if not isinstance(input, (HexCode, RgbCode)):
        raise TypeError(f"input can only be 'HexCode' or 'RgbCode' not '{type(input).__name__}'")
    if isinstance(input, HexCode) and to == HEX:
        raise ConvertionError("can not convert HexCode to HexCode")
    if isinstance(input, RgbCode) and to == RGB:
        raise ConvertionError("can not convert RgbCode to RgbCode")
    
    if isinstance(input, HexCode): # Convert Hex to Rgb
        sep = [input._value[1:][i:i+2] for i in range(0, len(input._value[1:]), 2)]
        red = None
        green = None
        blue = None
        for hexval in sep:
            saveval = 0
            hexls = list(hexval)
            hexls[0] = hexls[0].replace("A", "10").replace("B", "11").replace("C", "12").replace("D", "13").replace("E", "14").replace("F", "15")
            hexls[1] = hexls[1].replace("A", "10").replace("B", "11").replace("C", "12").replace("D", "13").replace("E", "14").replace("F", "15")
            saveval += int(hexls[1]) * 16 ** 0
            saveval += int(hexls[0]) * 16 ** 1
            if red == None:
                red = saveval
            elif green == None:
                green = saveval
            else:
                blue = saveval
        return RgbCode(red, green, blue)
    elif isinstance(input, RgbCode): # Convert Rgb to Hex
        return HexCode(f"#{hex(input._value[0])[2:]}{hex(input._value[1])[2:]}{hex(input._value[2])[2:]}".upper())