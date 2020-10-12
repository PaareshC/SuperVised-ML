v=zeros(10,1)
for i=1:10,
  v(i)=2^i;
endfor
v
indicies=1:10;
for i=indicies,
  disp(i);
endfor
v
i=1;
while i<=5,
  v(i)=100;
  i=i+1;
endwhile
v
i=1;
while true,
  v(i)=999
  i=i+1
  if i==6,
    break;
  endif
endwhile
v(1)=99
v(1)=2;
if v(1)==1.
  disp('The value is 1');
elseif v(1)=2,
  disp("The Value is 2");
else
  disp("The value is neither 2 nor 1")
endif
pwd
cd 'E:\Octave'
pwd
squarethisnumber(5)
[a,b]=squareandcubethisnumber(5)
% Let us def a function for COST
X=[1 1;1 2;1 3]
y=[1;2;3]
theta=[0;1]
j=costfunction(X,y,theta)
theta=[0;0]
j=costfunction(X,y,theta)