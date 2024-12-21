import argparse
import datetime
import json
import re
from collections import defaultdict


def match_project(project_name):
    if args.search is not None:
        if args.search.lower() in project_name['name'].lower():
            projects.append({'name': project_name['name'], 'time': project_name['grand_total']['total_seconds']})
            return True
        else:
            return False

    if args.project is not None:
        if args.project == project_name['name']:
            projects.append({'name': project_name['name'], 'time': project_name['grand_total']['total_seconds']})
            return True
        else:
            return False

    if args.regex is not None:
        if re.match(args.regex, project_name['name']):
            projects.append({'name': project_name['name'], 'time': project_name['grand_total']['total_seconds']})
            return True
        else:
            return False

    if args.all is not None:
        projects.append({'name': project_name['name'], 'time': project_name['grand_total']['total_seconds']})
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


def display_time(seconds):
    """Returns time in hours and minutes format"""
    hours, minutes = divmod(int(seconds / 60), 60)
    return f"{hours}h {minutes}m"


parser = argparse.ArgumentParser(description='Count hours in a wakatime data dump')
parser.add_argument('-f', '--file', metavar='file', type=open, required=True)
search = parser.add_mutually_exclusive_group(required=True)
search.add_argument('-a', '--all', action='store_true')
search.add_argument('-s', '--search', metavar='<term>')
search.add_argument('-p', '--project', metavar='<name>')
search.add_argument('-r', '--regex', metavar='<regex>')
parser.add_argument('-bd', '--before', metavar='YYYY-MM-DD')
parser.add_argument('-ad', '--after', metavar='YYYY-MM-DD')

args = parser.parse_args()

input_data = json.load(args.file)

total_time = 0.0
projects = []

for day in input_data['days']:
    if match_date(day):
        for project in day['projects']:
            if match_project(project):
                total_time = total_time + project['grand_total']['total_seconds']

c = defaultdict(int)
for d in projects:
    c[d['name']] += d['time']

# Sorting projects by time in descending order
projects = sorted([{'name': name, 'time': time} for name, time in c.items()], key=lambda x: x['time'], reverse=True)

if len(projects) > 0:
    print("Counted time from matching projects: " + display_time(total_time))
    for p in projects:
        print(f"    {p['name']}: {display_time(p['time'])}")
exit()
