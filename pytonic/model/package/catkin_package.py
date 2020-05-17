import subprocess
import yaml
from pytonic.model.includes.project_include import ProjectInclude

from collections import OrderedDict

class Header:
    def __init__(self, pkg_type=[], manifest_format=[], version=[],
                 cpp_version=[], cmake_version=[], project_name=[],
                 description='', pkg_license=[], is_extern=[], is_install=[]):
        self.container = OrderedDict(
            [('project_name' , project_name),
            ('pkg_type' , pkg_type),
            ('manifest_format' , manifest_format),
            ('version' , version),
            ('cpp_version' , cpp_version),
            ('cmake_version' , cmake_version),
            ('description' , description),
            ('license' , pkg_license),
            ('is_extern' , is_extern),
            ('is_install' , is_install)
        ])
    
    def get(self, attribute):
        return self.container[attribute]
    
    def replace(self, attribute, value):
        self.container[attribute] = value

    def __repr__(self):
        representation = str()
        for key, value in self.container.items():
            representation += '\n{}: {}'.format(key, value)
        return representation


head = Header(pkg_type='catkin', version='0.0.1')
class CatkinPackage:
    def __init__(self, ros_distro=None):
        self.header = Header(pkg_type='catkin', version='0.0.1')
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

    def readAsPyYAML(self, path):
        distro = self.ros_distro
        pkg_type = self.header.get('pkg_type')
        config = yaml.load(open(path, 'r'), Loader=yaml.FullLoader)
        config = config[pkg_type][distro]
        self.header.replace('cmake_version', config['cmake_version'])
        self.header.replace('cpp_version', config['cpp_version'])
        self.header.replace('is_extern', config['extern'])
        self.header.replace('is_install', config['install'])
        self.header.replace('license', config['license'])
        self.header.replace('manifest_format', config['manifest_format'])
        