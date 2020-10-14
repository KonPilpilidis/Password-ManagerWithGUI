###################################
##         Theme Module          ##
###################################
import os
import platform

TITLE = "Password Manager"

VERSION = "0.1"
if platform.system() != "Linux":
    LOGO = "logo.ico"
else:
    LOGO = "logo.gif"
    
# Geometry
Height = 1024
Width = 1024
WindowsSize = f'{str(Height)}x{str(Width)}'
PaddingUP = 0.1
PaddingDOWN = 0.1
PaddingRIGHT= 0.1
PaddingLEFT = 0.1

# Palette
bgColor = "#8cbcac"
windowColor = "#488f31"
buttonColor = "#f1f1f1"
textColor = "#691f2b"
altbgColor = "#b08587"