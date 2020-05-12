from pathlib import Path
import pytonic.package_factory.catkin as catkin
from pytonic.package_factory.catkin import manifest_factory, cmakelists_factory
from pytonic.model.package.catkin_package import CatkinPackage

def execute(args):
    pkg = loadTemplatePkg(args.PKG)
    print('Creating package {}'.format(args.PKG))
    create(pkg)
    print('Sucess!')

def loadTemplatePkg(pkg_name):
    pkg = catkin.getTemplatePkg()
    pkg.header.replace('project_name', pkg_name)
    return pkg

def create(pkg):
    catkin.manifest_factory.create(pkg)
    catkin.cmakelists_factory.create(pkg)