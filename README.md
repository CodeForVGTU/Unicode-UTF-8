# Unicode-UTF-8

## Simple app for understanding Unicode standart & UTF-8 coding.

Unicode is a computing industry standard for the consistent encoding, representation, and handling of text expressed in most of the world's writing systems.

UTF-8 (8-bit Unicode Transformation Format) is a variable width character encoding capable of encoding all 1,112,064[nb 1] valid code points in Unicode using one to four 8-bit bytes.

First MENU option:
  Enter decimal number to get unicode number, UTF-8 code and symbol.
  Decimal number interval {0, ... , 65535}.
  Everything written in a function get_info()
  
Second MENU option:
  There is given 386intel.txt file which is coded with CP437 table.
  Some symbols can't be read, so we need to decode them.
  If symbol is larger than 127 it means symbol is unknown and we need convert it by using CP437.txt file.
  Everything is written in a function decode()
  
Console Menu is amazing Python menu-based UI system for terminal applications. It's used for navigating functions.
