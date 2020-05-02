import argparse

def main():
    parser = argparse.ArgumentParser(description='pytonic commands')
    add = parser.add_argument('--echo', help='echo the string passed')
    args = parser.parse_args()
    print(args.echo)