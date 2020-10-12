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
HEIGHT = 1024
WIDTH = 1024
PADDINGUP = 20
PADDINGDOWN = 20
PADDINGRIGHT= 