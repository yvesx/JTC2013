#!/bin/bash
N=5
FILES=./n5stg*.csv
for f in $FILES
do
	echo "$f"
	python solve.py $f $N
	echo "--------------------------------------"
done
