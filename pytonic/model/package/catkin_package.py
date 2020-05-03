import subprocess
from configparser import ConfigParser
import yaml
from pytonic.model.includes.project_include import ProjectInclude

class CatkinPackage:
    def __init__(self, ros_distro=None):
        self.pkg_type = 'catkin'
        self.manifest_format = str()
        self.project_name = str()
        self.description = str()
        self.license = str()
        self.version = '0.0.1'
        self.cmake_version = str()
        self.cpp_version = str()
        self.is_extern = bool()
        self.is_install = bool()
        self.include_directories = ProjectInclude()
        self.libs = []
        self.execs = []
        self.catkin_deps = {
            "build_depend"          : [],
            "exec_depend"           : [],
            "build_export_depend"   : [],
            "test_depend"           : [],
            "doc_depend"            : []
        }

        self.system_deps = {
          "build_depend"          : [],
          "exec_depend"           : [],
          "build_export_depend"   : [],
          "test_depend"           : [],
          "doc_depend"            : []
        }

        if ros_distro is None:
            rosversion_cmd = subprocess.run('rosversion -d', shell=True, stdout=subprocess.PIPE, universal_newlines=True)
            self.ros_distro = rosversion_cmd.stdout.rstrip()
        else:
            self.ros_distro = ros_distro
    
    def readAsConfigParser(self, path):
        config = ConfigParser().read(path)

    def readAsPyYAML(self, path):
        distro = self.ros_distro
        pkg_type = self.pkg_type
        config = yaml.load(open(path, 'r'), Loader=yaml.FullLoader)
        config = config['catkin'][distro]
        self.cmake_version = config['cmake_version']
        self.cpp_version = config['cpp_version']
        self.is_extern = config['extern']
        self.is_install = config['install']
        self.license = config['license']
        self.manifest_format = config['manifest_format']
        