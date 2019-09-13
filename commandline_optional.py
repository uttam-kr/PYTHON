import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="please enter optional argument to proceed", action="store_true")
args = parser.parse_args()
if args.verbose:
    print(args.verbose)

