import argparse
import time
import tools

t0 = time.time()


def check_content(file_name: str, file_content: str):
	return [tools.error(file_name, 1, 'yub yub, commander')]


def check_source_file(file_name: str):
	with open(file_name, 'r') as file:
		file_content = file.read()
		return check_content(file_name, file_content)


parser = argparse.ArgumentParser(description='Check source code')
parser.add_argument('--sources', dest='sources', type=str, help='an integer for the accumulator')
parser.add_argument('--projectdir', dest='projectdir', type=str, help='an integer for the accumulator')
parser.add_argument('--output', dest='output', type=str, help='an integer for the accumulator')

args = parser.parse_args()
#print(args.projectdir)
#print(args.output)
#print(args.sources)

source_files = args.sources.split(';')

problems = []
for source_file in source_files:
	problems.extend(check_source_file(source_file))

problem_count = len(problems)
t1 = time.time()
total = t1-t0

if problem_count is 0:
	print ('No problems found, {0:.2f}s'.format(total))
else:
	for problem in problems:
		problem.print()
	print ('Found {0} problems, {1:.2f}'.format(problem_count, total))



