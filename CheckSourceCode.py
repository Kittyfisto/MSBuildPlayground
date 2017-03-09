import argparse
import time

t0 = time.time()

parser = argparse.ArgumentParser(description='Check source code')
parser.add_argument('--sources', dest='sources', type=str, help='an integer for the accumulator')
parser.add_argument('--projectdir', dest='projectdir', type=str, help='an integer for the accumulator')
parser.add_argument('--output', dest='output', type=str, help='an integer for the accumulator')

args = parser.parse_args()
print(args.projectdir)
print(args.output)
print(args.sources)

source_files = args.sources.split(';')

for source_file in source_files:
	print("{0}({1}): error: fix it, baby!".format(source_file, 1))

t1 = time.time()
total = t1-t0
print('Done. Took {0:.2f}s'.format(total))