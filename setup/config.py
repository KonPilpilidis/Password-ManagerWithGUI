from platform import system
Title = 'Password Manager'
Version = 0.1
OS = system()
Logo = "logo.ico" if system() != "Linux" else "logo.gif"
# Theme colors
BgColor = '#8cbcac'
TxtColor = '#691f2b'
BorderColor = '#488f31'
ButtonColor = '#f1f1f1'
WarningColor='#b08587'
# Geometry
Height = 1024
Width = 1024
BorderUp = 0.1
BorderDown = 0.1
BorderRight = 0.1
BorderLeft = 0.1