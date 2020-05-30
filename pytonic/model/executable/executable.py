from pytonic.misc import methdispatch

class Executable:
    def __init__(self, name : str, sources : set=set(), includes : set=set(), linked_libs : set=set() ):
        self.__name = name
        self.__sources = sources
        self.__includes = includes
        self.__linked_libs = linked_libs
    
    @methdispatch
    def addSource(self, source):
        self.__sources.add(source)

    @addSource.register(str)
    def _(self, source):
        self.__sources.add(source)

    @addSource.register(set)
    def _(self, sources):
        for source in sources:
            self.__sources.add(source)
    

    @methdispatch
    def removeSource(self, source):
        self.__sources.remove(source)

    @removeSource.register(str)
    def _(self, source : str):
        self.__sources.remove(source)

    @removeSource.register(set)
    def _(self, sources : set):
        for source in sources:
            self.__sources.remove(source)


    @methdispatch
    def addInclude(self, include):
        self.__includes.add(include)
    
    @addInclude.register(str)
    def _(self, include):
        self.__includes.add(include)
    
    @addInclude.register(set)
    def _(self, includes):
        for include in includes:
            self.__includes.add(include)


    @methdispatch
    def removeIncludes(self, include):
        self.__includes.remove(include)
    
    @removeIncludes.register(str)
    def _(self, include : str):
        self.__includes.remove(include)

    @removeIncludes.register(set)
    def _(self, includes : set):
        for include in includes:
            self.__includes.remove(include)
    

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
    
    def getIncludes(self):
        return self.__includes
    
    def getLinkedLibs(self):
        return self.__linked_libs
    
    def getSourcesAsStr(self):
        return ', '.join(sorted(self.__sources))
    
    def getIncludesAsStr(self):
        return ', '.join(sorted(self.__includes))
    
    def __repr__(self):
        return '{NAME}: {{sources: {SOURCES}, includes: {INCLUDES}}}'.format(NAME=self.__name, SOURCES=self.getSourcesAsStr(), INCLUDES=self.getIncludesAsStr())
    