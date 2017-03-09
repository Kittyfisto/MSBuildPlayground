from .problem import *


def print_report(problems: [], total_execution_time: int):
	problem_count = len(problems)
	if problem_count is 0:
		print ('No problems found, {0:.1f}s'.format(total_execution_time))
	else:
		for problem in problems:
			problem.print()
		print ('Found {0} problems, {1:.1f}s'.format(problem_count, total_execution_time))