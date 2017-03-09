import argparse
import time

t0 = time.time()


def print_warning(file_name: str, line: int, message: str):
	print('{0}({1}): warning : {2}'.format(file_name, line, message))


def print_error(file_name: str, line: int, message: str):
	print('{0}({1}): error : {2}'.format(file_name, line, message))


def check_content(file_name: str, file_content: str):
	print_warning(file_name, 1, 'yub yub, commander')


def check_source_file(file_name: str):
	with open(file_name, 'r') as file:
		file_content = file.read()
		check_content(file_name, file_content)


parser = argparse.ArgumentParser(description='Check source code')
parser.add_argument('--sources', dest='sources', type=str, help='an integer for the accumulator')
parser.add_argument('--projectdir', dest='projectdir', type=str, help='an integer for the accumulator')
parser.add_argument('--output', dest='output', type=str, help='an integer for the accumulator')

args = parser.parse_args()
#print(args.projectdir)
#print(args.output)
#print(args.sources)

source_files = args.sources.split(';')

for source_file in source_files:
	check_source_file(source_file)

t1 = time.time()
total = t1-t0
print('Done. Took {0:.2f}s'.format(total))