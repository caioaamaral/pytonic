from enum import Enum

INSTALL_SIGNATURE = Enum('INSTALL_SIGNATURE', 'TARGETS DIRECTORY FILE')
CATKIN_PKG_PARAM = Enum('CATKIN_PKG_PARAM', 'INCLUDE_DIRS LIBRARIES, CATKIN_DEPENDS DEPENDS')

def cmake_minimum_required(cmake_version):
    return 'cmake_minimum_required(VERSION %s)\n' % cmake_version

def project(project_name):
    return 'project({})\n'.format(project_name)

def cmake_set(var, value):
    return '\nset({0} {1})\n'.format(var, value)

def find_package(package_name, required=False, components=False):
    
    return '\nfind_package({PACKAGENAME}{REQUIRED}{COMPONENTS})\n'.format(
                                                                    PACKAGENAME=package_name,
                                                                    REQUIRED=' REQUIRED' if required else '',
                                                                    COMPONENTS='' if not components
                                                                                  else ' COMPONENTS\n  '
                                                                                  + '\n  '.join(components)
                                                                                  + '\n')

def catkin_package(pkg):
    return ('\ncatkin_package('
    '{INCLUDE_DIRS}'
    '{CATKIN_DEPENDS}'
    '{DEPENDS}'
    ')').format(
        INCLUDE_DIRS='\n  ' + CATKIN_PKG_PARAM.INCLUDE_DIRS.name + str(pkg.include_directories) + '\n' if pkg.is_extern and not pkg.include_directories.empty() else '',
        CATKIN_DEPENDS='\n  ' + CATKIN_PKG_PARAM.CATKIN_DEPENDS.name + str(pkg.catkin_deps['build_export_depend']) + '\n' if bool(pkg.catkin_deps['build_export_depend']) else '',
        DEPENDS='\n  ' + CATKIN_PKG_PARAM.DEPENDS.name + str(pkg.system_deps['build_export_depend']) + '\n' if bool(pkg.system_deps['build_export_depend']) else ''
    )

    

def add_library(library, sources):
    return '\nadd_library({NAME}\n  {SOURCE}\n)'.format(NAME=library, SOURCE="\n  ".join(sources))

def add_executable(executable, sources):
    return '\nadd_executable({NAME}\n  {SOURCE}\n)'.format(NAME=executable, SOURCE="\n  ".join(sources))

def target_link_libraries(target, libraries):
    return '\rtarget_link_libraries({} {})\n'.format(target, libraries)

def install(signature, target):
    if signature is INSTALL_SIGNATURE.TARGETS:
        return ('\rinstall({} {}\n'
        'ARCHIVE DESTINATION ${{CATKIN_PACKAGE_LIB_DESTINATION}}\n'
        'LIBRARY DESTINATION ${{CATKIN_PACKAGE_LIB_DESTINATION}}\n'
        'RUNTIME DESTINATION ${{CATKIN_PACKAGE_BIN_DESTINATION}}\n'
        ')\n').format(signature.name, target)
    if signature is INSTALL_SIGNATURE.DIRECTORY:
        return ('\rinstall({} {}\n'
            'DESTINATION ${{CATKIN_PACKAGE_SHARE_DESTINATION}}\n' 
        ')\n').format(signature.name, target)
    else:
        raise TypeError('signature must be an instance of INSTALL_SIGNATURE Enum')


