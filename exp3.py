EXPERIMENT 3
Write a MATLAB program to generate a set of 50 data points using the linear model:
y = −0.3x + 0.2r
where r is a normally distributed random number. Consider x = 1, 2, 3, …, 50. Use MATLAB commands to determine the best linear fit using polynomial curve fitting.
PROGRAM:
clc;clear all;close all;
x=1:50;
y=-0.3*x+0.2*randn(1,50);
p=polyfit(x,y,1);
f=polyval(p,x)
plot(x,y,'o',x,f,'-')
legend('data','linear fit')
xlabel('X values --->');
ylabel('Y values --->');
title('Linear Curve Fitting');
