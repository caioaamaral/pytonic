import os, sys
from pathlib import Path
from pytonic.package_factory.catkin.components.manifest_tags import *
from pytonic.model.package.catkin_package import CatkinPackage

def create(package : CatkinPackage):
    with open('package.xml', 'w+') as manifest:
        manifest.write(xmlVersion('1.0'))
        manifest.write(package_format(package.header.get('manifest_format')))
        manifest.write(name(package.header.get('project_name')))
        manifest.write(description(package.header.get('description')))
        manifest.write(maintainer('', ''))
        manifest.write(pkg_license(package.header.get('license')))
        manifest.write(version(package.header.get('version')))
        manifest.write(buildtool_depend(package.header.get('pkg_type')))

        for catkin_pkg in package.catkin_deps['build_depend']:
            manifest.write(build_depend(catkin_pkg))

        for sys_pkg in package.system_deps['build_depend']:
            manifest.write(build_depend(sys_pkg))

        for catkin_pkg in package.catkin_deps['exec_depend']:
            manifest.write(exec_depend(catkin_pkg))

        for sys_pkg in package.system_deps['exec_depend']:
            manifest.write(exec_depend(sys_pkg))

        for catkin_pkg in package.catkin_deps['build_export_depend']:
            manifest.write(build_export_depend(catkin_pkg))

        for sys_pkg in package.system_deps['build_export_depend']:
            manifest.write(build_export_depend(sys_pkg))

        for catkin_pkg in package.catkin_deps['test_depend']:
            manifest.write(test_depend(catkin_pkg))

        for sys_pkg in package.system_deps['test_depend']:
            manifest.write(test_depend(sys_pkg))

        for catkin_pkg in package.catkin_deps['doc_depend']:
            manifest.write(doc_depend(catkin_pkg))

        for sys_pkg in package.system_deps['doc_depend']:
            manifest.write(doc_depend(sys_pkg))

        manifest.write(close_package())
