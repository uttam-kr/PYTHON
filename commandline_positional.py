import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display square of given number", type=int)
args = parser.parse_args()
print(args.square**2)
