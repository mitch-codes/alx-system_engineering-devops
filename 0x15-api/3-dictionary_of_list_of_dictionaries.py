#!/usr/bin/python3

import sys
import requests
import json

if __name__ == "__main__":
    initialReq = requests.get("http://jsonplaceholder.typicode.com/todos/").json()
    secRequest = requests.get("http://jsonplaceholder.typicode.com/users").json()
    my_dict = {}
    for i in secRequest:
        strId = str(i["id"])
        my_dict[strId] = []
    for j in initialReq:
        strId2 = str(j["userId"])
        my_dict[strId2].append({"username": secRequest[int(strId2) - 1]["name"], "task": j["title"], "completed": j["completed"]})
    f = open("todo_all_employees.json", "w")
    f.write(json.dumps(my_dict))
    f.close()
