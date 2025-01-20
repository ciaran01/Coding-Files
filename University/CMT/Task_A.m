clear all
close all
clc

L=0.5;
lamda=100; n=51;
qa=5000; Tb=350;
c=4;
Sc=10; Sp=-20*(1+c);

% Generate Grid
x0=linspace(0,L,n);
dx=L/(n-1); DxB=dx/2;
Dx=dx;

% Matrices
A=zeros(n,n);
B=zeros(n,1);

% BCs
A(1,1)=(lamda/dx)-Sp*DxB; A(1,2)=-lamda/dx; B(1)=Sc*DxB+qa;

A(n,n)=1; B(n)=Tb;

% Fill A and B
for i=2:n-1
    A(i,i-1)=-lamda/dx; 
    A(i,i)=(2*lamda/dx)-Sp*Dx;
    A(i,i+1)=-lamda/dx;
    B(i)=Sc*Dx;
end

T=A\B;
plot(x0,T,'rs'); xlabel('x (m)'); ylabel('T (K)'); grid on
hold on

mu1=sqrt(-(Sp/lamda));
mu2=-mu1;
c1=(Tb+(qa/(lamda*mu2))*exp(mu2*L)+(Sc/Sp))/(exp(mu1*L)-(mu1/mu2)*exp(mu2*L));
c2=(-(qa/lamda)-c1*mu1)/mu2;
Tteo=c1*exp(mu1*x0)+c2*exp(mu2*x0)-(Sc/Sp);

plot(x0,Tteo,'k-'); legend('Backslash','Exact')

error=mean(abs(T-Tteo'))

% Calculating Error for different values of n
n=[11 21 51 101 201 501 1001];

for j=1:numel(n)
    x0=linspace(0,L,n(j));
    dx=L/(n(j)-1); Dx=dx; DxB=Dx/2;
    A=zeros(n(j),n(j));
    B=zeros(n(j),1);
    A(1,1)=(lamda/dx)-Sp*DxB; A(1,2)=-lamda/dx;
    A(n(j),n(j))=1;
    B(1)=Sc*DxB+qa;
    B(n(j))=Tb;
    for i=2:n(j)-1
        A(i,i-1)=-lamda/dx; 
        A(i,i)=(2*lamda/dx)-Sp*Dx;
        A(i,i+1)=-lamda/dx;
        B(i)=Sc*Dx;
    end
    T=A\B;
    Tteo=c1*exp(mu1*x0)+c2*exp(mu2*x0)-(Sc/Sp);
    error(j)=mean(abs(T-Tteo'));
end
dx=L./(n-1);
figure
loglog(dx,error,'o-');
xlabel('\deltax (m)'); ylabel('Error (K)'); grid on
