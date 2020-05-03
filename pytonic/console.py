import argparse
import pkg_resources
import sys

version = pkg_resources.get_distribution('pytonic').version

def getVerbModule(verb):
    for _verb in pkg_resources.iter_entry_points(group='pytonic.verbs'):
        if verb == _verb.name:
            return _verb.load()

def verbsVisitor(args):
    verb = getVerbModule(args.verb)
    verb.execute(args)
    

def generateOptionalArguments(parser):
    add = parser.add_argument
    add('--version', action='store_true', help='prints the pytonic current version')

def generatePytonicVerbs(parser):
    verb_parser = parser.add_subparsers(metavar='verb', dest='verb', help='a helper')

    make_parser = verb_parser.add_parser('create', help='Makes a catkin package')
    make_parser.add_argument('PKG', type=str, help='package name')

def main():
    parser = argparse.ArgumentParser()
    generateOptionalArguments(parser)
    generatePytonicVerbs(parser)

    args = parser.parse_args()
    if args.version:
        print('pytonic {}'.format(version))
    if args.verb:
        verbsVisitor(args)