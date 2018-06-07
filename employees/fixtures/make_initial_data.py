#!/usr/bin/python

import json, random

json_obj = []
pk = 0

in_file = open("peeps", "r")

for line in in_file:
    lmf = line.split()
    pk += 1
    birthday = '-'.join(['{:4d}'.format(random.randint(1950, 2000)), '{:02d}'.format(random.randint(1, 12)), '{:02d}'.format(random.randint(1, 28))])
    json_item = {
        "model": "employees.employee",
        "pk": pk,
        "fields": {
            "first_name": lmf[0],
            "middle_name": lmf[2],
            "last_name": lmf[0],
            "birthday": birthday,
            "email": "sema@sema.ru",
            "phone": "+79998887766",
            "begin_work": "2018-06-07",
            "end_work": None,
            "position": "\u0413\u043b\u0430\u0432\u0431\u0443\u0445",
            "department": 6
        }
    }
    json_obj.append(json_item)

in_file.close()

out_file = open("__initial_data.json", "w")

json.dump(json_obj, out_file, indent=4)

out_file.close()
