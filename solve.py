# python solve.py n10stg.csv N
# read the strategy. and solve the optimality of the strategy instead of running simuations.
from __future__ import print_function
import sys
import os
import string
import time
import random
import numpy
from numpy import genfromtxt
import math
import json
import sim
import scipy.sparse
import scipy
import scipy.sparse.linalg

P = 0.37

def solveSparseStrategy(stg,N):
	eqns = scipy.sparse.lil_matrix( ( N+1 , N+1 ) )
	b = numpy.zeros(  N+1  )
	eqns[0,0] = 1.0
	eqns[N,N] = 1.0
	b[0] = 0
	b[N] = 1
	for i in xrange(N-1): # i = 0,1,...,N-2, X = 1,2,...,N-1
		X = i+1
		B = stg[X]
		eqns[X,X - B] = 1.0 - P
		eqns[X,X + B] = P
		eqns[X,X] = -1.0
	eqns = eqns.tocsr() # for efficiency
	x = scipy.sparse.linalg.spsolve(eqns, b)
	return x

def solveStrategy(stg,N):
	eqns = numpy.zeros( ( N+1 , N+1 ) )
	b = numpy.zeros(  N+1  )
	eqns[0][0] = 1.0
	eqns[N][N] = 1.0
	b[0] = 0
	b[N] = 1
	for i in xrange(N-1): # i = 0,1,...,N-2, X = 1,2,...,N-1
		X = i+1
		B = stg[X]
		eqns[X][X - B] = 1.0 - P
		eqns[X][X + B] = P
		eqns[X][X] = -1.0
	x = numpy.linalg.solve(eqns, b)
	return x

def output(stg,q0,N,csv_file):
	with open(csv_file, 'w') as the_file:
		for i in xrange(N-1): # i = 0,1,...,N-2, X = 1,2,...,N-1
			X = i+1
			#stg[X] = [stg[X],q0[i]]
			print("%u,%u,%.9f"%(X,stg[X],q0[i]), file=the_file)



if __name__ == "__main__":
	N = int(sys.argv[2])
	stg = sim.readStrategy(sys.argv[1],N)

	if N > 1000:
		q_vect = solveSparseStrategy(stg,N)
	else:
		q_vect = solveStrategy(stg,N)
	q0 = list(q_vect)
	q0 = q0[1:]
	q0 = q0[:-1]
	output(stg,q0,N,sys.argv[1])
	#print q0
	#print "Qs: %.9f"%((sum(q_vect)-1.0)/(N-1))