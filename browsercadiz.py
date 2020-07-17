import os
import sys

# BrowserCadiz 1.0.0 - Copyright (c) @m3t4f0r4
# Created by @m3t4f0r4
# Enjoy it bro

try:
    url = sys.argv[1]
except:
    print("pon url bro")
try:
    os.system("firefox " + url + " &")
except:
    print("errooor!")

print("URL abierta! Disfruta bro!!!!!!!!")
