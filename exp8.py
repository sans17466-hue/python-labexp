EXPERIMENT 8
Solve the following system of linear algebraic equations using Gauss Elimination Method and obtain the solution vector using MATLAB:
6x +3y+2z=6
6x+4y+3z=0
20x+ 15y +12z=0

PROGRAM 
clc; clear;
A=[632; 643; 201512];
b= [6;0;0];Aug= [Ab];n = size(A, 1);
for i= 1:n-1
for j= i+1n
factor = Aug(j,i)/Aug(i, i);
Aug(,)= Aug(j,)- factor*Aug
end
end
x = Zeros(n, I);
for i=n:-1:1
sum_val = Aug(i,i+ 1:n)*x(i+1:n);
x(i)= (Aug(i, end) - sum_val)/Aug(i, );
end
disp('Solution is:")
disp(x)
