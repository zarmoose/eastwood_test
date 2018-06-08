#!/usr/bin/python

import json
import random

json_obj = []
pk = 0
positions = ["Должность №1", "Должность №2", "Должность №3", "Должность №4", "Должность №5"]
departments = {1: "Бухгалтерия", 2: "Маркетинг", 3: "Разработка", 4: "Производство", 5: "Логиcтика"}

for key in departments.keys():
    json_item = {
        "model": "employees.department",
        "pk": key,
        "fields": {
            "name": departments.get(key)
        }
    }
    json_obj.append(json_item)

in_file = open("peeps", "r")
for line in in_file:
    lmf = line.split()
    pk += 1
    birthday = '-'.join(['{:4d}'.format(random.randint(1950, 2000)), '{:02d}'.format(random.randint(1, 12)), '{:02d}'.format(random.randint(1, 28))])
    begin_work = '-'.join(['{:4d}'.format(random.randint(2000, 2018)), '{:02d}'.format(random.randint(1, 12)), '{:02d}'.format(random.randint(1, 28))])
    if random.choice([True, False]) == True:
        end_work = '-'.join(['{:4d}'.format(random.randint(2000, 2018)), '{:02d}'.format(random.randint(1, 12)), '{:02d}'.format(random.randint(1, 28))])
    else:
        end_work = None
    position = random.choice(positions)
    department = random.choice(list(departments.keys()))
    json_item = {
        "model": "employees.employee",
        "pk": pk,
        "fields": {
            "first_name": lmf[1],
            "middle_name": lmf[2],
            "last_name": lmf[0],
            "birthday": birthday,
            "email": "writeme@letter.ru",
            "phone": "+76665554433",
            "begin_work": begin_work,
            "end_work": end_work,
            "position": position,
            "department": department
        }
    }
    json_obj.append(json_item)
in_file.close()

out_file = open("initial_data.json", "w")
json.dump(json_obj, out_file, indent=4)
out_file.close()
