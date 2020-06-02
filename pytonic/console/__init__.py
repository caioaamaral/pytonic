import argparse
import pkg_resources
import sys

from pytonic.verbs import pytonic_create, pytonic_workspace

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
    verb_parser = parser.add_subparsers(metavar='verb', dest='verb')
    pytonic_create.add_parser(verb_parser)
    pytonic_workspace.add_parser(verb_parser)

def main():
    parser = argparse.ArgumentParser()
    generateOptionalArguments(parser)
    generatePytonicVerbs(parser)

    args = parser.parse_args()
    if args.version:
        print('pytonic {}'.format(version))
    if args.verb:
        verbsVisitor(args)