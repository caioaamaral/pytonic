import os, sys
from pathlib import Path
from configparser import ConfigParser
from pytonic.model.includes.project_include import ProjectInclude
from pytonic.model.environment_variable.cmake_var import CmakeVar

package_factory_path = Path(os.path.dirname(sys.argv[0])).parent

class ConfigFactory:
  CATKIN_LIBRARIES = CmakeVar('catkin_LIBRARIES')
  PROJECT_NAME = CmakeVar('PROJECT_NAME')
  config_file = Path(package_factory_path / 'build/package_factory.config')
  cmake_version = '3.1.3'
  cpp_version = '11'
  include_directories = ['include', '${catkin_INCLUDE_DIRS}']
  libs = [[str(PROJECT_NAME), ['src/class_b.cpp', 'src/_class_c.cpp', 'src/class_d.cpp']]]
  executables = [['my_node',['src/my_node.cpp', 'src/another_source.cpp'],[str(PROJECT_NAME)]]]
  extern = False
  install = False
  catkin_deps = {
      "build_depend"          : ['rospy', 'xmlrpcpp'],
      "exec_depend"           : [],
      "build_export_depend"   : [],
      "test_depend"           : [],
      "doc_depend"            : []
  }

  system_deps = {
      "build_depend"          : [],
      "exec_depend"           : [],
      "build_export_depend"   : [],
      "test_depend"           : [],
      "doc_depend"            : []
  }

  catkin_package = {
      "INCLUDE_DIRS"   : ' '.join(include_directories),
      "LIBRARIES"      : ' '.join(list(lib[0] for lib in libs)),
      "CATKIN_DEPENDS" : catkin_deps.get("build_export_depend")
  }

  def __init__(self):
    self.includes = ProjectInclude()
    self.config = ConfigParser()
  
  def add_package_name(self, name:str):
    CmakeVar.environ['PROJECT_NAME'] = name
    
  def add_include(self, include):
    self.includes.add(include)
  
  def read_config(self):
    self.config.read(config_file)

  def make_config(self):
    project_name = CmakeVar.environ['PROJECT_NAME']

    self.config[project_name] = {
      'project_name'          : project_name,
      'cmake_version'         : self.cmake_version,
      'cpp_version'           : self.cpp_version,
      'cmake_envar'           : CmakeVar.environ,
      'catkin_deps'           : self.catkin_deps,
      'system_deps'           : self.system_deps,
      'catkin_package'        : self.catkin_package,
      'libs'                  : self.libs,
      'executables'           : self.executables,
      'extern'                : self.extern,
      'install'               : self.install,
      'include_directories'   : self.includes
    }
    with self.config_file.open('w') as configfile:
      self.config.write(configfile)
  
if __name__ == '__main__':
  factory = ConfigFactory()
  factory.add_package_name('package_factory')
  factory.add_include(['include', '${catkin_INCLUDE_DIRS}'])
  factory.make_config()
