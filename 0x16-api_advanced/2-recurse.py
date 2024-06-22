#!/usr/bin/env python
# get reddit info from api
import requests


def recurse(subreddit, hot_list=[]):
    myTa = requests.get("http://www.reddit.com/r/"+subreddit+"/hot.json")
    if myTa.status_code == 200:
        myresponse = myTa.json()
        responseArray = myresponse.get("data").get("children")
        for myA in responseArray:
            for myList in hot_list:
                if myList == myA.get("data").get("title"):
                    print(myList)
        return 0
    else:
        return None
