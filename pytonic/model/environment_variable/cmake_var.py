class CmakeVar:
    environ = {}

    def __init__(self, name: str=None, value: str=None, environ=None):
        self.name = name
        self.value = value
        if environ is not None:
            self.environ.update(environ)
        if name is not None:
            self.environ[self.name] = value
    
    def getAllKeys(self):
        return list(self.environ.keys())
    
    def __repr__(self):
        return '${{{__name}}}'.format(__name=self.name)