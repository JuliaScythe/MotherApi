import requests as r
import constants
import sys
from API import API

// Program metadata
version = "version 0.01"

// API variebles
googleMaps = API("Google Maps API", 1.0, constants.JAVASCRIPT, constants.EMBED, constants.API_KEY)



def startup():
    print("motherApi")
    print("By Jake Irvine")
    print(version)
    print("Testing Internet Connectivity:")
    try:
        res = r.get("http://www.google.com")
    except(*):
        print("Error 0x01: No internet detected")
        sys.exit(1)
    print("Connection Succesful")
startup()
