import numpy as np
import fit_poly
import matplotlib.pyplot as plt

# Fits polynomial and plots all the comparitive graphs
# input: function to generate points
# n: no. of points, m: degree of polynomial
# reg: regulisar lambda
# returns: polynomial parameters, training error, testing error
def fitPlot_poly(func,xdata,ydata,m,r,reg=0):
	n = len(xdata)
	nTest = int(np.floor(n*r))
	nTrain = n-nTest

	xTrain = xdata[:nTrain]
	yObs = ydata[:nTrain]

	# print "Number of Training pts: " + str(len(xTrain))
	w = fit_poly.fit_data(xTrain,yObs,m,reg)
	poly = np.poly1d(np.fliplr([w])[0])

	# plot
	xp = np.linspace(0, 4, 1000)
	y = func(xp)
	plt.figure()
	plt.plot(xp, y, '-',label='original function') #sinx function
	plt.plot(xTrain,yObs,'o') #training pts
	plt.plot(xp, poly(xp), '--',label='fitted polynomial') #fitted polynomial
	plt.legend(loc='upper left')
	plt.title('m='+str(m)+' n='+str(n)+' reg='+str(reg))
	plt.ylim(-2,2)
	# plt.savefig("first.ps")
	plt.show()

	#errors: RMSE
	trainErr = np.sqrt(np.sum((ydata[:nTrain]-poly(xdata[:nTrain]))**2)/nTrain)
	testErr = np.sqrt(np.sum((ydata[nTrain:]-poly(xdata[nTrain:]))**2)/nTest)
	return w,trainErr,testErr

# check for different values of m, keeping n same
# Input: func: function to be plotted/sampled from
# n: No. of points to be sampled
# r: Proportion of test samples
# reg: lambda value for regression, default zero
def evaluateN(func,n,r,reg=0):
	xdata = np.linspace(0, 4, n)
	np.random.shuffle(xdata)
	ydata = func(xdata)
	ydata = ydata + 0.2 * np.random.normal(size=len(xdata)) #add error

	#plot data and errors

	#fit func into the xy data passed and plot the values
	M = [0,1,2,3,4,5,6,7,8,9,10]
	trainErr = np.zeros(len(M))
	testErr = np.zeros(len(M))
	for i,j in enumerate(M):
		_,err1,err2 = fitPlot_poly(func, xdata, ydata, j, r,reg)
		trainErr[i] = err1
		testErr[i] = err2

	plt.figure()
	plt.plot(M,trainErr,'-o',label='training error')
	plt.plot(M,testErr,'-x',linewidth=2.0,label='test error')
	plt.legend(loc='upper left')
	plt.title('training and testing error with n='+str(n))
	plt.xlabel('M')
	plt.ylabel('ERMS')
	plt.show()

# check for different values of n, keeping m same
# Input: func: function to be plotted/sampled from
# m: Degree of polynomial to be used
# r: Proportion of test samples
# reg: lambda value for regression, default zero
def evaluateM(func,m,r,reg=0):

	#fit func into the xy data passed and plot the values
	N = [10,50,100,200,300,400,500]
	trainErr = np.zeros(len(N))
	testErr = np.zeros(len(N))
	for i,n in enumerate(N):
		xdata = np.linspace(0, 4, n)
		np.random.shuffle(xdata)
		ydata = func(xdata)
		ydata = ydata + 0.2 * np.random.normal(size=len(xdata)) #add error

		_,err1,err2 = fitPlot_poly(func, xdata, ydata, m, r,reg)
		trainErr[i] = err1
		testErr[i] = err2

	plt.figure()
	plt.plot(N,trainErr,'-o',label='training error')
	plt.plot(N,testErr,'-x',linewidth=2.0,label='test error')
	plt.legend(loc='upper left')
	plt.title('training and testing error with m='+str(m))
	plt.xlabel('N')
	plt.ylabel('ERMS')
	plt.show()

# check for different values of n, keeping m same
# Input: func: function to be plotted/sampled from
# n: No. of points to be sampled
# m: Degree of polynomial to be used
# r: Proportion of test samples
def evaluateReg(func,n,m,r):

	#fit func into the xy data passed and plot the values
	N = [-50,-35,-30,-25,-20,-15]
	trainErr = np.zeros(len(N))
	testErr = np.zeros(len(N))
	for i,reg in enumerate(N):
		xdata = np.linspace(0, 4, n)
		np.random.shuffle(xdata)
		ydata = func(xdata)
		ydata = ydata + 0.2 * np.random.normal(size=len(xdata)) #add error

		_,err1,err2 = fitPlot_poly(func, xdata, ydata, m, r, np.exp(reg))
		trainErr[i] = err1
		testErr[i] = err2

	plt.figure()
	plt.plot(N,trainErr,'-o',label='training error')
	plt.plot(N,testErr,'-x',linewidth=2.0,label='test error')
	plt.legend(loc='upper left')
	plt.title('training and testing error with m='+str(m)+' n='+str(n))
	plt.xlabel('ln lambda')
	plt.ylabel('ERMS')
	plt.show()
