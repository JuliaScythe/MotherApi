
import requests as r
import constants
import sys
from API import API

# Program metadata
version = "version 0.01"

# API variebles
apis = []
googleMaps = API("Google Maps API", 1.0, "a", constants.JAVASCRIPT, constants.EMBED, constants.API_KEY)
apis.append(googleMaps)
googleMaps.registerFunc("Standard Map", "The standard google map", "googleMaps\\android\\hello.java")
googleMaps.registerFunc("Std. Map w/ marker", "Map with custom marker text", "googleMaps\\android\\hellomarker.java")
googleMaps.registerFunc("Map types", "Map with choice of types", "googleMaps\\android\\type.java")
googleMaps.registerFunc("Map w/ custom markers", "Map with custom marker image", "googleMaps\\android\\markerimage.java")
googleMaps.registerFunc("Map w/ flat markers", "Map with flat marker images. These rotate with prespective.", "googleMaps\\android\\markerflat.java")
googleMaps.printFuncs()

def startup():
    print("motherApi")
    print("By Jake Irvine")
    print(version)
    print("Testing Internet Connectivity:")
    try:
        res = r.get("http://www.google.com")
    except("*"):
        print("Error 101: No internet detected")
        sys.exit(1)
    print("Connection Succesful")

def listApis():
    for a in apis:
        print("["+ a.letter + "] | " + a.name.ljust(20) + "| " + str(a.version))
    ch = input("Choose an API >>>  ")
    for a in apis:
        if ch == a.letter:
            return a
    print("Please choose am API")
    listApis
startup()
listApis()
