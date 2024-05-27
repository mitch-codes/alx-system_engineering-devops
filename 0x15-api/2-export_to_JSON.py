#!/usr/bin/python3

import sys
import requests
import json

if __name__ == "__main__":
    myId = sys.argv[1]
    initialReq = requests.get("http://jsonplaceholder.typicode.com/todos/").json()
    secRequest = requests.get("http://jsonplaceholder.typicode.com/users").json()
    userName = secRequest[int(myId) - 1]["name"]
    my_dict = {myId: []}
    for i in initialReq:
        if i["userId"] == int(myId):
            my_dict[myId].append({"task": i["title"], "completed": i["completed"], "username": userName})
    f = open(myId+".json", "w")
    f.write(json.dumps(my_dict))
    f.close()
    print(len(my_dict[str(myId)]))
