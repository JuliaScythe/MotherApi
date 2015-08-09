import constants

class API:
    name = ""
    version = 0
    language = 0
    auth = 0
    mode = 0
    funcs = []
    def __init__(self, name, version, language, mode=constants.REST, auth=constants.NONE):
        self.name = name
        self.version = version
        self.language = language
        self.mode = mode
        self.auth = auth
