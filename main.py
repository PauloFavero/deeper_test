# sys imports
import os
import sys
import glob
import json

# open json file
json_data = None
json_file_path = os.path.join("source_file_2.json")
json_managers = os.path.join("managers.json")
json_watchers = os.path.join("watchers.json")

with open(json_file_path) as json_file:
            json_data = json.load(json_file)

# print(json_data)

#sort the data
higher_priority_list = sorted(json_data, key=lambda key: key['priority']) 

manager_set = {}
watchers_set = {}

#create a set of managers and watchers
for project in higher_priority_list:
    for manager in project['managers']:
        manager_set[manager] = []
    for watcher in project['watchers']:
        watchers_set[watcher] = []

# set the project list for each manager and watchers
for project in higher_priority_list:
    for manager in project['managers']:
        manager_set[manager].append(project['name'])
    for watcher in project['watchers']:
        watchers_set[watcher].append(project['name'])


with open(json_managers, 'w') as manager_file:
    json.dump(manager_set, manager_file, indent=4)

with open(json_watchers, 'w') as watchers_file:
    json.dump(watchers_set, watchers_file, indent=4)