#!/usr/bin/python3

import sys
import requests
import json

if __name__ == "__main__":
    myId = sys.argv[1]
    my_list = []
    initialReq = requests.get("http://jsonplaceholder.typicode.com/todos/")
    secRequest = requests.get("http://jsonplaceholder.typicode.com/users").json()
    userName = secRequest[int(myId) - 1]["name"]
    complete = 0
    incomplete = 0
    response = initialReq.json()
    total = len(response)

    if (response):
        for i in response:
            if i["userId"] == 1:
                if i["completed"] == False:
                    incomplete = incomplete + 1
                else:
                    my_list.append(i["title"])
                    complete = complete + 1
        print("Employee {} is done with tasks({}/{}):".format(userName, complete, incomplete + complete))
        for jobs in my_list:
            print(" \t",jobs)
