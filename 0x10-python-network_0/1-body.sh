#!/bin/bash
# take in a URL, sends a GET request to the URL, and displays the body of the response
curl -slf "$1" -X GET
