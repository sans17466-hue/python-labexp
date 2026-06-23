EXPERIMENT 10
Wite a MATLAB program to compute the Discrete Fourier Transform (DFT) of the sequenc.
[n] = [1, 2, 3, 4) using the DFT formula

PROGRAM 
x=[1, 2, 3, 4];N=length(x);X=zeros(1, N);for k=0:N-1
for n=0:N-1
X(k+I)=X(k+1)+x(n+1)*exp(-li*2*pi*k*nN);
end
end
display(X);
