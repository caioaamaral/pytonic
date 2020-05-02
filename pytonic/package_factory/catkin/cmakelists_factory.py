import os, sys
from pathlib import Path
from configparser import ConfigParser
from pytonic.package_factory.cmake_commands import *

package_factory_path = Path(os.path.dirname(sys.argv[0])).parent

config = ConfigParser()
config.read(str(package_factory_path) + '/build/package_factory.config')

config = config['package_factory']

is_extern = config.getboolean('extern')
is_install = config.getboolean('install')
project_name = config['project_name']
cmake_version = config['cmake_version']
cpp_version = (int)(config['cpp_version'])
catkin_deps = eval(config['catkin_deps'])
catkin_package = eval(config['catkin_package'])
include_directories = config['include_directories']

libs = eval(config['libs'])
executables = eval(config['executables'])

is_extern = True

with open('CMakeLists.txt', 'w+') as file:
    # cmake version
    file.write(cmake_minimum_required(cmake_version))

    # project name
    file.write(project(project_name))

    # cpp version
    file.write(cmake_set('CMAKE_CXX_STANDARD', cpp_version))
    
    # find catkin packages
    file.write(find_package("catkin", True, catkin_deps.get('build_depend')))
    
    file.write('\ncatkin_package(\n')
    if is_extern:
        for key in catkin_package:
            if catkin_package.get(key):
                file.write('  %s %s\n' % (key, catkin_package.get(key)))
    file.write(')\n')

    CATKIN_LIBRARIES = '${catkin_LIBRARIES}'
    for lib in libs:
        lib_name = lib[0]
        lib_sources = lib[1]
        file.write(add_library(lib_name, lib_sources))
        file.write(target_link_libraries(lib_name, CATKIN_LIBRARIES))

    # add_executables
    for target in executables:
        name = target[0]
        sources = target[1]
        target_libs = " ".join(target[2])
        file.write(add_executable(name, sources))
        file.write(target_link_libraries(name, target_libs))
    
    # install
    if not is_install:
        # install libs
        for lib in libs:
            lib = lib[0]
            file.write(install(INSTALL_SIGNATURE.TARGETS, lib))
        
        # install executables
        for target in executables:
            target = target[0]
            file.write(install(INSTALL_SIGNATURE.TARGETS, target))

print('sucess')
