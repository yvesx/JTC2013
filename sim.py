# python sim.py n10stg.csv N
# read the strategy. run simulations. estimate winning probability 
import sys
import os
import string
import time
import random
import numpy
from numpy import genfromtxt
import math
import json
P = 0.37

def readStrategy(filename,N):
	strategy = dict()
	data = genfromtxt(filename,delimiter=',')
	for d in data:
		X = int(d[0])
		B = int(d[1])
		strategy[X] = B # put strategy in lookup hash
		if B > X or B > N - X or B < 1 or X < 1 or X > N -1:
			print "error in strategy!! X %s B %s" % (X,B)
	return strategy

# iterations to simulate, strategy mapping, xo - starting sum
def simBernoulliProcess(itr,strategy,xo,N):
	success = 0.0
	for i in xrange(itr):
		cur_bal = xo
		while cur_bal > 0 and cur_bal < N:
			delta = math.copysign(strategy[cur_bal], P - random.random()) # 63% chance -; 37% chance +
			cur_bal += int(delta)
		if cur_bal == N:
			success += 1.0
	return {"X":xo,"B":strategy[xo],"q":success/itr}

if __name__ == "__main__":
	N = int(sys.argv[2])
	stg = readStrategy(sys.argv[1],N)

	Qs = 0.0
	Ws = 0.0
	for i in xrange(N-1): # i = 0,1,...,N-2
		row = simBernoulliProcess(itr=10000,strategy=stg,xo=i+1,N=N)
		Qs += row["q"]
		Ws += row["B"]
		if (i%100) == 0:
			print json.dumps(row)
	print "Qs %s Ws %s" % (Qs/(N-1) , Ws/(N-1))