import constants

class API:
    name = ""
    version = 0
    funcs = []
    def __init__(self, name, version, language, type=constants.REST, auth=constants.NONE):
        self.name = name
        self.version = version
