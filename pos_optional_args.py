import argparse
import sys
import logging
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.info('expected result')
usage_str = ("usage: pos_optional.py [-h] [--verbose] [-v]")

def main(argv):
    if(len(argv) == 0):
        sys.stderr.write(usage_str)
        sys.exit(1)

parser=argparse.ArgumentParser()
parser.add_argument("square", help="display square of given number", type=int)
parser.add_argument("--verbose",action="store_true",help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print("the square of {} equal {}".format(args.square, answer))
else:
    print(answer)

if __name__ =='__main__':
    main(sys.argv[1:])

