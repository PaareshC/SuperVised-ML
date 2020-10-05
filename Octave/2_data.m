A=[1 2;3 4;5 6]
A
size(A)
sz=size(A)
size(sz)
size(A,1) % First dimension of A (number of Rows)
size(A,2) % Second dimension of A (number of columns)
v=[1 2 3 4 5 6]
length(v)
length(A) % Here A has two dimensions but lenght will return longest dimension
length([1;2;3;4;5;6;7;8])
pwd %for current directory
% cd 'Address Here' to change working directory
%ls to list all files
% load featuresX.dat  
% load('featuresX.dat') 
% who = shows what variables octave has currently in memory
% featuresX=to display features X
% whos= like who but more details
% clear varibla name = to clear variable name
% v=price(1:10) now v has first 10 elements of y
% save hello.mat v; will save v in hello.mat
% clear = all variables in workspace will be cleared
% save hello.txt v -ascii = save as ascii format text
A
A(3,2)
A(2,:) % Every element in second row
A(:,2) %Everything in second columns of A
A([1 3],:) % all columns form 1 and 3 row
A(:,2)=[10;11;12]
A
A=[A,[100;101;102]]; %append another column vector to the right
A
A(:) % all emelents of A in a column vector
A=[1 2;3 4;5 6];
B=[11 12;13 14; 15 16];
C=[A B]
C=[A;B]
[A B]
[A,B]