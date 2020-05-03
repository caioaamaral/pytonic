import sys
from pathlib import Path
from pytonic.model.package.catkin_package import CatkinPackage
from pytonic.package_factory.catkin import manifest_factory

catkin_templates = str(Path(Path(sys.modules[__name__].__file__).parent / 'templates' / 'catkin_package.yaml'))

def getTemplatePkg():
    pkg = CatkinPackage('kinetic')
    pkg.readAsPyYAML(catkin_templates)
    return pkg