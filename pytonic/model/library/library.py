from pytonic.misc import methdispatch

class Library:
    def __init__(self, name: str, sources: set=set(), linked_libs: set=set()):
        self.__name = name
        self.__sources = sources
        self.__linked_libs = linked_libs


    @methdispatch
    def addSource(self, source):
        self.__sources.add(source)

    @addSource.register(str)
    def _(self, source : str):
        self.__sources.add(source)

    @addSource.register(set)
    def _(self, source : set):
        for element in source:
            self.__sources.add(element)


    @methdispatch
    def removeSource(self, source):
        self.__sources.remove(source)

    @removeSource.register(str)
    def _(self, source : str):
        self.__sources.remove(source)
    
    @removeSource.register(set)
    def _(self, source : set):
        for element in source:
            self.__sources.remove(element)


    @methdispatch
    def linkToLib(self, lib : str):
        self.__linked_libs.add(lib)
    
    @linkToLib.register(str)
    def _(self, libs : str):
        self.__linked_libs.add(libs)
    
    @linkToLib.register(set)
    def _(self, libs : set):
        for lib in libs:
            self.__linked_libs.add(lib)

    @methdispatch
    def unlinkToLib(self, lib):
        self.__linked_libs.remove(lib)
    
    @unlinkToLib.register(str)
    def _(self, lib : str):
        self.__linked_libs.remove(lib)

    @unlinkToLib.register(set)
    def _(self, libs : set):
        for lib in libs:
            self.__linked_libs.remove(lib)


    
    def getName(self):
        return self.__name

    def getSources(self):
        return self.__sources
    
    def getLinkedLibs(self):
        return self.__linked_libs
    
    def getSourcesAsStr(self):
        return ', '.join(sorted(self.__sources))
    
    def getLinkedLibsAsStr(self):
        return ', '.join(sorted(self.__linked_libs))
    
    def __repr__(self):
        return '{NAME}: {{sources: {SOURCES}, linked_libs: {LINKEDLIBS}}}'.format(NAME=self.__name, SOURCES=self.getSourcesAsStr(), LINKEDLIBS=self.getLinkedLibsAsStr())

