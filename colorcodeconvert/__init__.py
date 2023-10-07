"""
colorcodeconvert by Simoso68

colorcodeconvert is released under the GNU General Public License version 3
and is free and open source software (FOSS) under the definitions of the
Open Source Initiative (OSI) as it is released under an officially
by the OSI approved license, the GNU General Public License version 3.

To see what you can do with the code, read the GNU General Public License
version 3 yourself:

GNU's Website: https://gnu.org/licenses/gpl-3.0
OSI's Website: https://opensource.org/license/gpl-3-0/
"""

from .colorcodes import *
from .convert import convert
from .types import HexCode, RgbCode
from .errors import *

metadata = {
    "title":"colorcodeconvert",
    "version":"1.0.1",
    "author":"Simoso68",
    "license":"GNU General Public License version 3",
    "source":"https://github.com/Simoso68/colorcodeconvert",
}