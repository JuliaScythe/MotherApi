import constants

class Func:
    def __init__(self, name, desc, identifyer):
        self.name = name
        self.desc = desc
        self.identifyer = identifyer

class API:
    name = ""
    version = 0
    language = 0
    auth = 0
    mode = 0
    funcs = []
    def __init__(self, name, version, letter, language,  mode=constants.REST, auth=constants.NONE):
        self.name = name
        self.version = version
        self.language = language
        self.mode = mode
        self.auth = auth
        self.letter = letter
    def registerFunc(self, name, desc, identifyer):
        self.funcs.append(Func(name, desc, identifyer))

    def printFuncs(self):
        i = "a"
        for f in self.funcs:
            print("["+ i + "] | " + f.name.ljust(30) + "| " + f.desc.ljust(50) + " | " + f.identifyer)
            i = chr(ord(i) + 1)
