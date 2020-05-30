from pathlib import Path
from xml.etree import cElementTree
import sys
import pytonic

package_xml = (Path(Path(sys.modules['pytonic'].__file__).parent / 'build' / 'package.xml'))

class ManifestParser():
    def __init__(self, file : Path):
        if not file.is_file():
            raise FileNotFoundError(file)
        self.__map = cElementTree.parse(open(str(file), 'r')).getroot()
    
    def getName(self):
        return self.__map.find('name').text
    
    def getBuildTool(self):
        return self.__map.find('buildtool_depend').text

parser = ManifestParser(package_xml)
print(parser.getBuildTool())