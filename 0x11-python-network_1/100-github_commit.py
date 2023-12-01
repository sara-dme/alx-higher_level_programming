#!/usr/bin/python3
""" Access the Github API and uses the information """
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"
    resp = requests.get(url.format(argv[2], argv[1]))
    res = resp.json()
    try:
        for j in range(0, 10):
            print(f"{res[j].get('sha)}:\
                    {res[j].get('commit').get('author').get('name')}")
    except IndexError:
        pass
