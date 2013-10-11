# python generate.py N
# generate strategy and write it to file. 
import sys
import os
import string
import time
import random
import numpy
from numpy import genfromtxt
import math
import json

def genMaxStg(N): # the max strategy
	arr = list()
	for i in xrange(N-1):
		X = i + 1
		B = min([X,N-X])
		arr.append([X,B])
	return arr

def genMidStg(N): # the mid strategy
	arr = list()
	for i in xrange(N-1):
		X = i + 1
		B = 1
		arr.append([X,B])
	arr[int(math.ceil(N/2.0)) - 1][1] = int(math.floor(N/2.0))
	return arr

def genConStg(N,max_arr): # increasing p=0 prob.
	p = 0
	for i in xrange(N-1):
		p += 1.0/N
		if random.random() < p:
			max_arr[i][1] = 1
	return max_arr


def geBbfStg(N,max_arr, step, p): # back-back-forward strategy
	# step = 3 default
	for i in xrange(N-(step+1)):
		if (i+1)%step == 0 and random.random() < p:
			max_arr[i+1][1] = 1
	return max_arr

def geRdmStg(N,max_arr,p): # random strategy
	for i in xrange(N-4):
		if random.random() < p:
			max_arr[i+1][1] = 1
	return max_arr


def writeStg(filename,arr):
	numpy.savetxt(filename,numpy.asarray(arr),delimiter=',',fmt='%u')

if __name__ == "__main__":
	N = int(sys.argv[1])
	writeStg("n%sstg_mx.csv"%(N),genMaxStg(N))
	writeStg("n%sstg_mid.csv"%(N),genMidStg(N))
	writeStg("n%sstg_bbf.csv"%(N),geBbfStg(N,genMaxStg(N),3,1))
	writeStg("n%sstg_bbf05.csv"%(N),geBbfStg(N,genMaxStg(N),3,0.5))	
	writeStg("n%sstg_con.csv"%(N),genConStg(N,genMaxStg(N)))
	writeStg("n%sstg_rdm37.csv"%(N),geRdmStg(N,genMaxStg(N),0.37))
	writeStg("n%sstg_rdm87.csv"%(N),geRdmStg(N,genMaxStg(N),0.87))