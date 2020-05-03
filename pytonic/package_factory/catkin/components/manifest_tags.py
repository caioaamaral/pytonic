def xmlVersion(xml_version):
    return '<?xml version=\"{}\"?>\n'.format(xml_version)

def package_format(format):
    return '<package format=\"{}\">\n'.format(format)

def name(name):
    return '  <name>{}</name>\n'.format(name)

def description(description):
    return ('  <description>\n'
            '  {}\n'
            '  </description>\n').format(description)

def maintainer(email, fullname):
    return '  <maintainer email=\"{}\">{}</maintainer>\n'.format(email, fullname)

def pkg_license(pkg_license):
    return '  <license>{}</license>\n'.format(pkg_license)

def version(version):
    return '  <version>{}</version>\n'.format(version)

def buildtool_depend(buildtool_depend='carkin'):
    return '\n  <buildtool_depend>{}</buildtool_depend>\n\n'.format(buildtool_depend)

def depends(depends):
    return '  <depends>{}</depends>\n'.format(depends)

def build_depend(build_depend):
    return '  <build_depend>{}</build_depend>\n'.format(build_depend)

def exec_depend(exec_depend):
    return '  <exec_depend>{}</exec_depend>\n'.format(exec_depend)

def build_export_depend(build_export_depend):
    return '  <build_export_depend>{}</build_export_depend>\n'.format(build_export_depend)

def test_depend(test_depend):
    return '  <test_depend>{}</test_depend>\n'.format(test_depend)

def doc_depend(doc_depend):
    return '  <doc_depend>{}</doc_depend>\n'.format(doc_depend)

def close_package():
    return '\n</package>'