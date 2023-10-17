from enum import Enum


class AuthApiEndpoints(Enum):
    TOKEN = 'oauth/token'

    def getPath(self, *args):
        res = self.value
        for parameter in args:
            # convert to str
            arg = parameter if parameter is str else str(parameter)
            # replace
            res = res.replace('{}', arg, 1)
        return res

