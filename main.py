
import requests as r
import constants
import sys
import os
from API import API

# Program metadata
version = "version 0.01"
size = os.get_terminal_size()
w = size.columns
# API variebles
apis = []
googleMaps = API("Google Maps API", 1.0, "a", constants.JAVASCRIPT, constants.EMBED, constants.API_KEY)
apis.append(googleMaps)
googleMaps.registerFunc("Standard Map", "The standard google map", "googleMaps\\android\\hello.java")
googleMaps.registerFunc("Std. Map w/ marker", "Map with custom marker text", "googleMaps\\android\\hellomarker.java")
googleMaps.registerFunc("Map types", "Map with choice of types", "googleMaps\\android\\type.java")
googleMaps.registerFunc("Map w/ custom markers", "Map with custom marker image", "googleMaps\\android\\markerimage.java")
googleMaps.registerFunc("Map w/ flat markers", "Map w/ flat marker img that rotate w/ prespective", "googleMaps\\android\\markerflat.java")
#googleMaps.printFuncs()

def startup():
    print("=" * w)
    print(" " * int(w/2-4) + "motherApi")
    print(" " * int(w/2-6) + "By Jake Irvine")
    print(" " * int(w/2-5) + version)
    print(" " * int(w/2-12) + "Testing Internet Connectivity:")
    try:
        res = r.get("http://www.google.com")
    except("*"):
        print("Error 101: No internet detected")
        sys.exit(1)
    print(" " * int(w/2-6) + "Connection Succesful")
    print("=" * w)
def listApis():
    for a in apis:
        print("["+ a.letter + "] | " + a.name.ljust(20) + "| " + str(a.version))
    ch = input("Choose an API >>>  ")
    for a in apis:
        if ch == a.letter:
            return a
    print("Please choose am API")
    listApis()
startup()
choice = listApis()
print("=" * w)
print("Ok, now choose a function:")
print("=" * w)
ch = choice.printFuncs()
print("=" * w)
print("You have selected: " + ch.name + " from " + choice.name)
params = ch.parseData()
for i in params:
    print("=" * w)
    input("Please enter value for " + i + ">>")
