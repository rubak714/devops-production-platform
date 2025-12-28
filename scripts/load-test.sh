#!/bin/bash

URL=$1

for i in {1..200}
do
  curl $URL/work &
done
wait
