from pathlib import Path
import sys
import pytonic
from pytonic.model.package.catkin_package import CatkinPackage
from pytonic.package_factory.catkin import cmakelists_factory
from itertools import islice
import mmap

from typing import List
from pytonic.model.library.library import Library
from pytonic.model.executable.executable import Executable




cmake_lists = (Path(Path(sys.modules['pytonic'].__file__).parent / 'build' / 'CMakeLists.txt'))

class CMakeListParser:
    def __init__(self, cmake_file : Path):
        with cmake_file.open('r+b') as cmake_file:
            self.mapped =  mmap.mmap(cmake_file.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)
            self.type = 'catkin' if self.isCatkin else 'cmake'
            self.sources = self.getSources()
            self.libs = self.getLibs()
            self.mapped.close()
    
    def findToken(self, token : str, begin : int=0, end : int=None):
        line_num = begin
        self.mapped.seek(0)
        iterable = iter(self.mapped.readline, b'')
        for line in islice(iterable, begin, end):
            if token in line:
                return line, line_num
            line_num += 1
        return None, None

    def getFirst(self, key : str):
        key = key.encode('utf-8')
        return self.findToken(key)
    
    def getAll(self, key : str):
        key = key.encode('utf-8')
        matches = []
        line_num = 0
        while (True):
            line, line_num = self.findToken(key, line_num)
            if not line:
                return matches
            else:
                index = self.mapped.tell() - len(line)
                begin = self.mapped.find(b'(', index)
                end = self.mapped.find(b')', begin)

                line = self.mapped[begin+1:end]
                line = line.decode('utf-8').replace('\n', '')
                matches.append(line.split())
                line_num += 1

    def isCatkin(self):
        return True if self.getFirst('catkin_package') is not None else False

    def getSources(self):
        return self.getAll('add_executable')
        
    def getLibs(self):
        return self.getAll('add_library')

parser = CMakeListParser(cmake_lists)
print(parser.type)
print(parser.sources)
print(parser.libs)
