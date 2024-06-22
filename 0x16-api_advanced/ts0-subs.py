#!/usr/bin/env python
# get reddit info from api
import requests

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

def number_of_subscribers():
    headers = {'User-Agent': "Custom"}
    myTa = requests.get("https://www.googleapis.com/books/v1/volumes/tzreDgAAQBAJ", headers=headers)
    myTs = myTa.json();
    print(myTs.get("kind"))

if __name__ == "__main__":
    number_of_subscribers()
