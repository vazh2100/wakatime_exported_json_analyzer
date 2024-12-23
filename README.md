### The Wakatime Exported JSON Analyzer

is a tool designed to analyze exported JSON file from the **Export**
section in the account settings of [Wakatime](https://wakatime.com/settings/account).

### Features

- displays a sorted list of projects along with the time spent on each project.
- displays a sorted list of languages, operating systems, machines and editors along with the time spent on each
- displays days along with the time matching search request
- *case-insensitive search*: matches strings in project names, ignoring case.
- *regular expression search*: allows flexible string matching using regex patterns.
- *exact name search*: matches the full name of the project exactly as it appears.
- *date range filtering*

### Usage
```commandline
### All time and all projects

python wakahack.py -f wakatime4.json -a`

Total time: 2081h 38m
Projects:
    everyport_front: 644h 32m
    everylounge: 610h 56m
    evernow_mobile: 151h 35m
    ...
```

```commandline
### Searched projects before this year. Display projects, languages, os, machines, editors

python wakahack.py -f wakatime4.json -s tinkoff -bd 2024-01-01 --show=plome

Total time: 23h 39m
Projects:
    tinkoff_id_flutter: 10h 17m
    tinkoff_id_web: 7h 20m
    tinkoff_acquiring_native_flutter: 2h 50m
    TinkoffID: 2h 46m
    Tinkoff-Acquiring-SDK-Flutter: 0h 24m
    
Languages:
    Dart: 9h 49m
    Kotlin: 4h 25m
    Swift: 3h 35m
    Markdown: 2h 4m
    ...
Operating systems:
    Linux: 19h 38m
    Mac: 4h 1m
    
Machines:
    zen: 18h 19m
    MBP-admin: 4h 0m
    ...
Editors:
    Android Studio: 20h 50m
    Xcode: 2h 49m
```
```commandline
### Searched projects by regular expression in specific two months. Show projects and days

python wakahack.py -f wakatime4.json -r .*otlin.* -ad 2024-11-01 -bd 2024-12-31 -show pd

Total time: 65h 12m
Projects:
    KotlinPRO: 64h 3m
    KotlinCopyGenerator: 1h 8m

Days:
    2024-11-02: 0h 4m
    2024-11-03: 2h 38m
    2024-11-04: 1h 1m
    2024-11-05: 1h 28m
    2024-11-06: 2h 30m
    2024-11-07: 6h 10m
    ...
```
```bash
### Searched project by its exact name all time this year and show days as bars

python wakahack.py -f wakatime4.json -p "GeoEventApplication" -ad 2024-01-01 -show pb

Total time: 89h 21m
Projects:
    GeoEventApplication: 89h 21m
Days:
    2024-11-22: ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 7h 1m
    2024-11-23: ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 10h 30m
    2024-11-24: ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 13h 52m
    2024-11-25: ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 6h 21m
    2024-11-26: ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 5h 2m
    2024-11-27: ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 12h 7m
    2024-11-28: ■■■■■■■■■■■■■■■■■■■■■■■■■■■ 4h 31m
    2024-11-29: ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 8h 58m
    2024-11-30: ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 8h 22m
    2024-12-01: ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 5h 49m
    2024-12-02: ■■■■■■■■■■■■■■■■■■■■ 3h 27m
    2024-12-03: ■■ 0h 26m
    2024-12-04: ■■■■■■■■■■■ 1h 53m
    2024-12-05: ■■■ 0h 35m
    2024-12-08:  0h 2m
    2024-12-12: ■ 0h 10m
    2024-12-13:  0h 7m
```

```commandline
### Search all time and all projects and show only operating systems, machines and editors

python wakahack.py -f wakatime4.json -a -show ome

Total time: 2081h 38m
Operating systems:
    Linux: 2025h 51m
    Mac: 55h 46m

Machines:
    zen: 1710h 32m
    acer3: 315h 19m
    mac-mini.local: 25h 15m
    MacBook-Pro-admin.local: 15h 18m
    MBP-admin: 15h 12m

Editors:
    Android Studio: 1973h 6m
    IntelliJ IDEA: 66h 30m
    Xcode: 21h 55m
    VS Code: 12h 14m
    PyCharm: 4h 5m
    AppCode: 3h 32m
```

Fork of [yammyshep/wakahack](https://github.com/yammyshep/wakahack)
