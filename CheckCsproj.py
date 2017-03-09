import argparse
import xml.etree.ElementTree as ET


def check_project_file(file_name: str):
	tree = ET.parse(file_name)
	root = tree.getroot()


parser = argparse.ArgumentParser(description='Check source code')
parser.add_argument('--projects', dest='projects', type=str, help='Full path to the csproj file(s) to parse. Use ; as separator if multiple files are passed')

args = parser.parse_args()

projects = args.projects.split(';')
for file_name in projects:
	check_project_file(file_name)
