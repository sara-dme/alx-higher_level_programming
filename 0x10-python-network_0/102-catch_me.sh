#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me
curl -sX PUT -L "0.0.0.0:5000/catch_me" -d "user_id=98" -H "origin: School"
