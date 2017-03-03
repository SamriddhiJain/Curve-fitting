# Author: riddle
# Polynomial curve fitting
import numpy as np

# fits univariate data to polynomial of degree m
# Input: x: Input points
# t: Observed Values
# m: Degree of polynomial to be fitted
# reg: lambda value for regression, default zero
def fit_data(x, t, m, reg=0):
	n = len(x)

	#intialise c vector
	c = np.zeros(m+1)
	ctemp = np.ones(n)
	for i in range(0,m+1):
		c[i] = np.dot(t,ctemp)
		ctemp = np.multiply(x,ctemp)

	#intialise a matrix
	#aTemp contains sigma (x^i) | i --> 0:2m
	aTemp = np.zeros(2*m+1)
	temp = np.ones(n)
	for i in range(0,len(aTemp)):
		aTemp[i] = np.sum(temp) # summation over all m
		temp = np.multiply(x,temp) #element wise multipliction: raises power by one every time

	a = np.zeros(shape=(m+1,m+1))
	for i in range(0,m+1):
		for j in range(0,m+1):
			a[i][j] = aTemp[i+j]

	# add regulariser if passed
	if(reg):
		regMatrix = reg*np.eye(m+1,m+1)
		a = a + regMatrix

	# solve linear equations [a][w] = [c]
	w = np.linalg.solve(a, c)
	
	return w

# fits multivariate data to polynomial of degree m: generalised case
# Input: Input points x: N*(M+1), Observed Values: N, Degree: M
def fit_dataMulti(x, t, m, reg=0):
	n,_ = size(x)

	#intialise c vector
	c = np.transpose(x)*t

	#intialise a matrix
	a = np.transpose(x)*x

	if(reg):
		regMatrix = reg*np.eye(m+1,m+1)
		a = a + regMatrix

	# solve linear equations
	w = np.linalg.solve(a, c)
	
	return w