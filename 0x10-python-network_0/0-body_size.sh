#!/bin/bash
# Get the content lenght of a giving ip
curl -sI "$1" | awk '/Content-length/{print $2}'
