#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and
displays the body of the response
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    val = {"email": argv[2]}
    data = urllib.parse.urlencode(val)
    data = data.encode('utf8')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf8"))
    
