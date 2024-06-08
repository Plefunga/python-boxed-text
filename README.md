# python-boxed-text
Creates a border around text, with some formatting options

# How to use
```python
from boxedtext import Box

width = 47
boxedtext = Box(width)

boxedtext.add_text("BOXED TEXT DEMO", center=True)
boxedtext.add_text("This is a demonstration of the python-boxed-text. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
boxedtext.add_text("")
boxedtext.add_text("LIST DEMONSTRATION", center=True)
boxedtext.add_list(["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."])
print(boxedtext)
```

This prints the following:
```
#######################################################
##                  BOXED TEXT DEMO                  ##
##  This is a demonstration of the                   ##
##  python-boxed-text. Lorem ipsum dolor sit amet,   ##
##  consectetur adipiscing elit, sed do eiusmod      ##
##  tempor incididunt ut labore et dolore magna      ##
##  aliqua. Ut enim ad minim veniam, quis nostrud    ##
##  exercitation ullamco laboris nisi ut aliquip ex  ##
##  ea commodo consequat.                            ##
##                                                   ##
##                LIST DEMONSTRATION                 ##
##  1. Lorem ipsum dolor sit amet, consectetur       ##
##     adipiscing elit, sed do eiusmod tempor        ##
##     incididunt ut labore et dolore magna aliqua.  ##
##  2. Ut enim ad minim veniam, quis nostrud         ##
##     exercitation ullamco laboris nisi ut aliquip  ##
##     ex ea commodo consequat.                      ##
#######################################################
```
