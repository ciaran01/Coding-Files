%Gauss-Seidel function w/ over-relaxation
function [x,res,m]=GaussSeidelw(A,B,x,tol,Imax,omega)
m=0;
n=numel(x);
res=sum(abs(B-A*x))/sum(abs(diag(A).*x));

while (res>tol & m<Imax)
    m=m+1;
    for i=1:n
        x(i)=x(i)+omega*((B(i)/A(i,i)-(A(i,:)/A(i,i))*x));
    end
    res(m)=sum(abs(B-A*x))/sum(abs(diag(A).*x));
end

