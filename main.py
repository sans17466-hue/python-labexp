EXPERIMENT 1
Write a MATLAB program to generate two sinusoidal signals using the equation:
y(t) = sin(2πft)
where the frequencies are f₁ = 2 Hz and f₂ = 10 Hz. Consider the time range from t = 0 to t = 1 seconds with a step size of 0.01. Perform the following operations and plot the results using the subplot command:
Plot both sinusoidal signals
Addition of the two signals
Subtraction of the two signals
Multiplication of the two signals
Label the axes as time and amplitude, and give suitable titles for each plot.

PROGRAM:
clc; clear all; close all;
t=0:0.01:1
y1=sin(2*pi*2*t)
y2=sin(2*pi*10*t)
a=y1+y2;
s=y1-y2;
m=y1.*y2;
subplot(2,2,1);
plot(t,y1,t,y2);
xlabel('time -->');
ylabel('amplitude -->');
title('sinosoidal signal');
subplot(2,2,2);
plot(t,a);
xlabel('time -->');
ylabel('amplitude -->');
title('addition');
subplot(2,2,3);
plot(t,s);
xlabel('time -->');
ylabel('amplitude -->');
title('subtraction');
subplot(2,2,4);
plot(t,m);
xlabel('time -->');
ylabel('amplitude -->');
title('multiplication');
