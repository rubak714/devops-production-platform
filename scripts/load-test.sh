#!/bin/bash

URL=$1

# Increase from 200 to 1000 requests
for i in {1..1000}
do
  curl $URL/work &
done
wait
