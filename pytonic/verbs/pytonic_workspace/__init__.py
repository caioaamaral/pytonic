from pathlib import Path
import os

def execute(args):
    if args.init:
        init(args.init)
    else:
        print(args)

def init(args):
    component = Path(args)
    print(component)

def add_parser(verb_parser):
    workspace_parser = verb_parser.add_parser('workspace', help='Comands for workspace mode')
    workspace_load = workspace_parser.add_argument('--init', nargs='?', const=Path(os.getcwd()),  help='Start workspace mode')
