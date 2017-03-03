CS671 - Deep Learning and its Applications
Assignment 1
Submitted by: Samriddhi Jain (B13136)

Steps to run the code
The code is completely generalised in nature, user can change various parameters from the command-line itself.
The code in fit_poly file fits a M degree polynomial into randomly sampled N points. Various effects of different parameters have been coded with wrappers in file fit_curve.py, which calls the functions in above mentioned file and plots the curve.

Currently, by default, sin x is used to sample and plot the data, but it can also be changed in the main function. The curve fitting functions are independent of any underlying function.

To see the effect of various parameters, run main.py by passing a parameter 'opt'.
python main.py -opt [val]
Here [val] can take values from {1,2,3,4}.
Meaning of various select options: 
	Keeping N fixed and effect with M(1)
	Keeping M fixed and effect with N(2)
	Effect of regularisation, keeping N and M fixed(3)
	Single demo(4)

Other parameters which can be changed and their default values:
-N N        Number of points to be sampled, default 10
-M M        Degree of polynomial to be estimated, default 10
-reg REG    regulariser lambda value, default 0
-r R        ratio of test data to N, default 0.3

For example to see effect of different degrees of polynomial run with 100 sampled points,
python main.py -opt 1 -N 100
This will give series of plots and will plot a graph on training v/s test error at the end. Close each window in order to see the next.

python main.py -h
This will give list and details of all the parameters that can be changed according to need.
