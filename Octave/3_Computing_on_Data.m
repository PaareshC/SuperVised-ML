pwd
A=[1 2;3 4;5 6]
B=[ 11 12;13 14;15 16]
C=[1 1;2 2]
A*C
A.*B
A
A.^2
v=[1;2;3]
1./v
log(v)
exp(v)
v
abs(v)
abs([-1;2;-3])
-v %same as -1*V
v+ones(length(v),1)
v+1
A
A'
(A')'
a=[1 15 2 0.5]
val=max(a)
a
[val,ind]=max(a) %returns maximum value of a and it's index
max(A) % Gives column wise maximum
a<3
find(a<3)
A=magic(3)
[r,c]=find(A>=7)
% to read documentation = help find
a
sum(a)
prod(a)
floor(a)
ceil(a)
rand(3)
max(rand(3),rand(3))
A
max(A,[],1) %col wise maximum
max(A,[],2) %Per row
max(max(A)) %For entire matrix_type
% or 
% turn into vector
A(:)
max(A(:))
A=magic(9)
sum(A,1)
sum(A,2)
eye(9)
A.*eye(9)
sum(sum(A.*eye(9)))
sum(sum(A.*flipud(eye(9))))
eye(9)
flipud(eye(9))
A=magic(3)
pinv(A)
temp=pinv(A)
temp*A %Gives identity matrix_type
