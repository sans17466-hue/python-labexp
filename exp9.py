EXPERIMENT 9
Write a MATLAB program to find a root of the equation
f(2)=2x^2-5x+3= 0
using the Newton-Raphson method.
· Take the initial guess as co = 0
Use a tolerance of 10-7
Perform iterations until convergence or up to 100 iterations
Display the root and number of iterations

PROGRAM :
f=@(x)x-(2*×个2-5*×+3)/(4*×-5):
0=X
tol=1e-7:
for iteration=1:100
xnew=f(x):
if abs(xnew-x)>tol x=xnew;
else
break
end
end
fprintf(“Root=%f at iteration no.%dln', xnew, iteration)
