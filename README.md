### The Wakatime Exported JSON Analyzer

is a tool designed to analyze exported JSON file from the **Export**
section in the account settings of [Wakatime](https://wakatime.com/settings/account).

### Features

1. **Projects Overview**  
   Displays a sorted list of projects along with the time spent on each project.  
   Also, displays a sorted list of languages, operating systems, machines and editors along with the time spent on each
   entry.

2. **Three types of project searches**  
   *Case-insensitive*: Matches strings in project names, ignoring case.  
   *Regular expression*: Allows flexible string matching using regex patterns.  
   *Exact name*: Matches the full name of the project exactly as it appears.

3. **Date Range Filtering**

### Usage

```commandline
All time and all projects:

python wakahack.py -f wakatime.json -a
Total time: 2078h 27m
Projects:
    ***: 644h 29m
    ***: 610h 56m
    ***: 151h 35m
    ...
```

```commandline
Searched projects in the current year:

python wakahack.py -f wakatime.json -s waka -ad 2024-01-01
Total time: 2h 25m
Projects:
    wakatime_exported_json_analyzer: 2h 10m
    kWaka: 0h 15m
```

```commandline
Searched projects by regular expression in specific month:

python wakahack.py -f wakatime.json -r .*json.* -ad 2024-12-01 -bd 2024-12-31 
Total time: 1113h 21m
Projects:
    wakatime_exported_json_analyzer: 2h 10m
    infinite_json_destroyer: 1111h 11m
```

```commandline
A searched project by its exact name all time before this year:

python wakahack.py -f wakatime.json -p "wakatime_exported_json_analyzer" -bd 2024-01-01 
Total time: 100h 7m
Projects:
    wakatime_exported_json_analyzer: 100h 7m
```

```commandline
Search all time and all projects and show only operating systems, machines and editors:

python wakahack.py -f wakatime.json -a -show ome
Total time: 2071h 46m
Operating systems:
    Linux: 2016h 0m
    ...
Machines:
    zen: 1699h 42m
    ...
Editors:
    Android Studio: 1968h 31m
    IntelliJ IDEA: 65h 12m
    PyCharm: 2h 10m
    ...
```

Fork of [yammyshep/wakahack](https://github.com/yammyshep/wakahack)
