EXPERIMENT 7
Write a MATLAB program to:
1. Find the eigenvalues and eigenvectors of a given matrix A
2. Find the inverse of the matrix
3. Verify that:
4. 
PROGRAM 
clc;
clear;
Close all;
A = input('Enter matrix A: ');
% Eigenvalues and Eigenvectors
[V, D] = eig(A);
disp('Eigenvalues (D):');
disp(D);
disp('Eigenvectors (V):');
disp(V);
% Inverse of matrix
A_inv = inv(A);
disp('Inverse of matrix A:');
disp(A_inv);
% Verification
I = A * A_inv;
disp('Verification (A * A_inv):');
disp(I);
