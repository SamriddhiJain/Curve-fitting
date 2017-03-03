import numpy as np
import fit_poly
import fit_curve
import matplotlib.pyplot as plt
import argparse

def sin(x):
	temp = np.zeros(len(x))
	for i,j in enumerate(x):
		temp[i] = np.sin(2*np.pi*j)

	return temp

def exp(x):
	temp = np.zeros(len(x))
	for i,j in enumerate(x):
		temp[i] = np.exp(j)

	return temp

#parsing command line arguments
ap = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
ap.add_argument("-N", default=10,
	help="Number of points to be sampled")
ap.add_argument("-M", default=10,
	help="Degree of polynomial to be estimated")
ap.add_argument("-reg", default=0,
	help="regulariser lambda value")
ap.add_argument("-r", default=0.3,
	help="ratio of test data")
ap.add_argument("-opt", required='true', 
	help="Select options: \n"
	"Keeping N fixed and effect with M(1)\n"
	"Keeping M fixed and effect with N(2) \n"
	"Effect of regularisation, keeping N and M fixed (3)\n"
	"Single demo (4)")
args = vars(ap.parse_args())

n=int(args['N'])
m=int(args['M'])
reg=float(args['reg'])
r=float(args['r'])
val=int(args['opt'])

if(val==1):
	fit_curve.evaluateN(sin,n,r,reg)
elif(val == 2):
	fit_curve.evaluateM(sin,m,r,reg)
elif(val == 3):
	fit_curve.evaluateReg(sin,n,m,r)
elif(val==4):
	#single demo
	xdata = np.linspace(0, 4, n)
	np.random.shuffle(xdata)
	ydata = sin(xdata)
	ydata = ydata + 0.2 * np.random.normal(size=len(xdata)) #add error

	#fit func into the xy data passed and plot the values
	w1,_,_ = fit_curve.fitPlot_poly(sin, xdata, ydata, m, r, reg)
	print w1
else:
	print "Unknown option"

# fit_curve.evaluateM(sin,10,0.3)
# fit_curve.evaluateN(sin,10,0.3)
# fit_curve.evaluateReg(sin,100,10,0.3)

# #single demo
# xdata = np.linspace(0, 4, 100)
# np.random.shuffle(xdata)
# ydata = sin(xdata)
# ydata = ydata + 0.2 * np.random.normal(size=len(xdata)) #add error

# #fit func into the xy data passed and plot the values
# w1,_,_ = fit_curve.fitPlot_poly(sin, xdata, ydata, 15, 0.3,np.exp(-18))
# # w2,_,_  = fit_curve.fitPlot_poly(sin, xdata, ydata, 9, 0.3,1)
# w3,_,_  = fit_curve.fitPlot_poly(sin, xdata, ydata, 15, 0.3)
# print w1
# print w3