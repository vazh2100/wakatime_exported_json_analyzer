import argparse
import datetime
import json
import re
from collections import defaultdict

##----Parser----##
parser = argparse.ArgumentParser(description='Count hours in a wakatime data dump')
parser.add_argument('-f', '--file', metavar='file', type=open, required=True)
search = parser.add_mutually_exclusive_group(required=True)
search.add_argument('-a', '--all', action='store_true')
search.add_argument('-s', '--search', metavar='<term>')
search.add_argument('-p', '--project', metavar='<name>')
search.add_argument('-r', '--regex', metavar='<regex>')
parser.add_argument('-bd', '--before', metavar='YYYY-MM-DD')
parser.add_argument('-ad', '--after', metavar='YYYY-MM-DD')
parser.add_argument("-show", "--show", metavar="plome", default="p",
                    help="output options: p - projects, l - languages, o - os, m - machines e - editors, ")

##----Variables----##
args = parser.parse_args()
input_data = json.load(args.file)
showP = "p" in args.show
showL = "l" in args.show
showO = "o" in args.show
showM = "m" in args.show
showE = "e" in args.show
total_time = 0.0
projects_dict = defaultdict(int)
languages_dict = defaultdict(int)
operating_systems_dict = defaultdict(int)
editors_dict = defaultdict(int)
machines_dict = defaultdict(int)


##----Functions----##
def match_project(project_entry):
    if args.search is not None:
        return args.search.lower() in project_entry['name'].lower()
    if args.project is not None:
        return args.project == project_entry['name']
    if args.regex is not None:
        return re.match(args.regex, project_entry['name'])
    if args.all is not None:
        return True


def match_date(date):
    project_date = datetime.datetime.strptime(date['date'], '%Y-%m-%d')
    if args.before is not None:
        before_date = datetime.datetime.strptime(args.before, '%Y-%m-%d')
        if before_date < project_date:
            return False
    if args.after is not None:
        after_date = datetime.datetime.strptime(args.after, '%Y-%m-%d')
        if after_date > project_date:
            return False
    return True


def add_project(project):
    projects_dict[project['name']] += project['grand_total']['total_seconds']
    global total_time
    total_time += project['grand_total']['total_seconds']


def add_language(language):
    languages_dict[language['name']] += language['total_seconds']


def add_os(os):
    operating_systems_dict[os['name']] += os['total_seconds']


def add_editor(editor):
    editors_dict[editor['name']] += editor['total_seconds']


def add_machine(machine):
    machines_dict[machine['name']] += machine['total_seconds']


def display_time(seconds):
    """Returns time in hours and minutes format"""
    hours, minutes = divmod(int(seconds / 60), 60)
    return f"{hours}h {minutes}m"


def print_summary(title: str, data: list[tuple[any, int]]):
    if len(data) > 0:
        print(title + ":")
        for item in data:
            print(f"    {item[0]}: {display_time(item[1])}")
        print()


##----Execution Section----##
def main():
    # Processing
    for day in input_data['days']:
        if match_date(day):
            for project in day['projects']:
                if match_project(project):
                    add_project(project)
                    if showL:
                        for language in project['languages']:
                            add_language(language)
                    if showO:
                        for os in project['operating_systems']:
                            add_os(os)
                    if showE:
                        for editor in project['editors']:
                            add_editor(editor)
                    if showM:
                        for machine in project['machines']:
                            add_machine(machine)
    # Printing
    print("Total time: " + display_time(total_time))
    if showP:
        projects = sorted(projects_dict.items(), key=lambda x: x[1], reverse=True)
        print_summary("Projects", projects)
    if showL:
        languages = sorted(languages_dict.items(), key=lambda x: x[1], reverse=True)
        print_summary("Languages", languages)
    if showO:
        operating_systems = sorted(operating_systems_dict.items(), key=lambda x: x[1], reverse=True)
        print_summary("Operating systems", operating_systems)
    if showM:
        machines = sorted(machines_dict.items(), key=lambda x: x[1], reverse=True)
        print_summary("Machines", machines)
    if showE:
        editors = sorted(editors_dict.items(), key=lambda x: x[1], reverse=True)
        print_summary("Editors", editors)


main()
exit()
