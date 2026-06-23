EXPERIMENT 6
Write a MATLAB program to numerically evaluate the definite integral
|^5^0(x²+2x+1)dx
using the Trapezoidal Rule with 10 equal subintervals.

PROGRAM:
clc;clear all;close all;
f = @(x) x^2 + 2*x + 1; 
a = 0; 
b = 5; 
n = 10; 
h = (b - a)/n;
sum = f(a) + f(b);
for i = 1:n-1
x = a + i*h;
sum = sum + 2*f(x);
end
I= (h/2) * sum;
fprintf ('Integral using Trapezoidal Rule, I = %.6f\n', I);
