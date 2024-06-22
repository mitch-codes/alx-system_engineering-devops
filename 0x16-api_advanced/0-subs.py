#!/usr/bin/env python
# get reddit info from api
import requests
import json


def number_of_subscribers(subreddit):
    myTa = requests.get("http://www.reddit.com/r/"+subreddit+"/about.json")
    if myTa.status_code == 200:
        response = myTa.json().get("data").get("subscribers")
        return response
    return 0
