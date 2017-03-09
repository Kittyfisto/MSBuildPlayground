from enum import Enum


class ProblemType(Enum):
	Info = 0
	Warning = 1
	Error = 2


problem_names = {
	ProblemType.Info: 'info',
	ProblemType.Warning : 'warning',
	ProblemType.Error : 'error'
}


class Problem:
	type = ProblemType.Info
	file_name = ''
	line_number = 0
	message = ''

	def __init__(self, type: ProblemType, file_name: str, line_number: int, message: str):
		self.type = type
		self.file_name = file_name
		self.line_number = line_number
		self.message = message

	def print(self):
		written_type = problem_names.get(self.type, '<Unkown>')
		print('{0}({1}): {2} : {3}'.format(self.file_name, self.line_number, written_type, self.message))


def info(file_name: str, line_number: int, message: str):
	return Problem(ProblemType.Info, file_name, line_number, message)


def warning(file_name: str, line_number: int, message: str):
	return Problem(ProblemType.Warning, file_name, line_number, message)


def error(file_name: str, line_number: int, message: str):
	return Problem(ProblemType.Error, file_name, line_number, message)
