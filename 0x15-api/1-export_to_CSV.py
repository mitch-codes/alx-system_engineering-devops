#!/usr/bin/python3

import sys
import requests
import json

if __name__ == "__main__":
    myId = sys.argv[1]
    myResult = ""
    initialReq = requests.get("http://jsonplaceholder.typicode.com/todos/")
    secRequest = requests.get("http://jsonplaceholder.typicode.com/users").json()
    userName = secRequest[int(myId) - 1]["name"]
    complete = 0
    incomplete = 0
    response = initialReq.json()
    f = open(myId+".csv", "w")

    if (response):
        for i in response:
            if i["userId"] == int(myId):
                myResult += "\"{}\",\"{}\",\"{}\",\"{}\" \n".format(i["userId"], userName, i["completed"], i["title"])
                print(i["id"])
        f.write(myResult)
        f.close()
