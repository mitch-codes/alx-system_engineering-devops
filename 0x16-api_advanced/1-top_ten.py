#!/usr/bin/env python
# get reddit info from api
import requests


def top_ten(subreddit):
    myTa = requests.get("http://www.reddit.com/r/"+subreddit+"/hot.json")
    if myTa.status_code == 200:
        myresponse = myTa.json()
        responseArray = myresponse.get("data").get("children")
        for i in range(10):
            print(responseArray[i]["data"]["title"])
            if responseArray[i + 1] is None:
                break
    else:
        print(None)
