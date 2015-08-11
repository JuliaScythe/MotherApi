import constants
import re
r = re.compile(r"£\S*£")

class Func:
    def __init__(self, name, desc, identifyer):
        self.name = name
        self.desc = desc
        self.identifyer = identifyer

    def parseData(self):
        retur = []
        f = open("APIS\\" + self.identifyer, 'r', encoding='utf-8')
        fs = f.read()
        #print(fs)
        res = r.findall(fs)
        print(res)
        for string in res:
            string = string.replace('£', '').replace('Â', '') # No idea why
            retur.append(string)
            print(retur)
        return retur
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
            f.letter = i
            i = chr(ord(i) + 1)
        ch = input("Choose an function >>>  ")
        for f in self.funcs:
            if ch == f.letter:
                return f
        print("Please choose a function")
        self.printFuncs()
