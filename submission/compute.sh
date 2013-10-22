#!/bin/bash
N=1024
FILES=./n1024stg*.csv
for f in $FILES
do
	echo "$f"
	python solve.py $f $N
	echo "--------------------------------------"
done
