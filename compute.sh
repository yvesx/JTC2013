#!/bin/bash
N=1000000
FILES=./n1000000stg*.csv
for f in $FILES
do
	python solve.py $f $N
done
