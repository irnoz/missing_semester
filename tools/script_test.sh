#!/bin/bash

count=0
while [[ $? -eq 0 ]];
do
	count=$((count+1))
	./script.sh
done
echo "It ran $count times"


