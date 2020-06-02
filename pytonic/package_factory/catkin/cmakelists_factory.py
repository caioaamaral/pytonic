import os, sys
from pathlib import Path
from configparser import ConfigParser
from pytonic.package_factory.catkin.components.cmake_commands import *
from pytonic.model.package.catkin_package import CatkinPackage

def create(pkg : CatkinPackage):
    with open('CMakeLists.txt', 'w+') as file:
        # cmake version
        file.write(cmake_minimum_required(pkg.header.get('cmake_version')))

        # project name
        file.write(project(pkg.header.get('project_name')))

        # cpp version
        file.write(cmake_set('CMAKE_CXX_STANDARD', pkg.header.get('cpp_version')))

        # find catkin packages
        file.write(find_package('catkin', True, pkg.catkin_deps.get('build_depend')))

        file.write(catkin_package(pkg))

        for lib in pkg.libs:
            lib_name = lib.getName()
            lib_sources = lib.getSources()
            lib_linked_libs = lib.getLinkedLibs()
            file.write(add_library(lib_name, lib_sources))
            if lib_linked_libs:
                file.write(target_link_libraries(lib_name, lib_linked_libs))

        # add_executables
        for target in pkg.execs:
            name = target.getName()
            sources = target.getSources()
            source_linked_libs = target.getLinkedLibs()
            file.write(add_executable(name, sources))
            if source_linked_libs:
                file.write(target_link_libraries(name, source_linked_libs))

        # install
        if pkg.header.get('is_install'):
            # install libs
            for lib in pkg.libs:
                lib = lib[0]
                file.write(install(INSTALL_SIGNATURE.TARGETS, lib))

            # install executables
            for target in pkg.execs:
                target = target[0]
                file.write(install(INSTALL_SIGNATURE.TARGETS, target))
