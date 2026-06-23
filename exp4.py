EXPERIMENT 4
Write a MATLAB program to generate 10 equally spaced points in the interval 0 to 4r. Compute the sine values of these points and obtain a third-degree polynomial approximation using polynomial curve fitting.Evaluate the fitted polynomial over the interval O to 4r and plot the original data points and the approximated curve.

PROGRAM:
clc; clear all; close all;
x = linspace(0,4*pi,10);
y = sin(x);
p = polyfit(x,y,3);
x1 = linspace(0,4*pi);
f = polyval(p,x1);
plot(x,y,'o',x1,f,'-')
legend('data points','cubic fit')
xlabel('X values --->');
ylabel('Y values --->');
title('Polynomial Curve Fitting')
