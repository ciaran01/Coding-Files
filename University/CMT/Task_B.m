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

%Theoretical Solution
mu1=sqrt(-(Sp/lamda));
mu2=-mu1;
c1=(Tb+(qa/(lamda*mu2))*exp(mu2*L)+(Sc/Sp))/(exp(mu1*L)-(mu1/mu2)*exp(mu2*L));
c2=(-(qa/lamda)-c1*mu1)/mu2;
Tteo=c1*exp(mu1*x0)+c2*exp(mu2*x0)-(Sc/Sp);

figure(1); plot(x0,Tteo,'mv'); hold on

% Using Gauss-Seidel Method
Imax=15000;
tol=1e-10;
T_ast=B(n)*ones(n,1); %Initial guess

% [T_gs,res_gs,m_gs]=GaussSeidel(A,B,T_ast,tol,Imax);
% 
% 
% plot(x0,T_gs); hold on
% legend('Exact','Gauss-Seidel')
% xlabel('x (m)'); ylabel('T (K)')
% 
% figure
% semilogy(res_gs)
% xlabel('Iterations'); ylabel('Residuals')
% 
% error=mean(abs(T_gs-Tteo'))


w=(1.1:0.1:2);
for i=1:numel(w)
    [T_gs,res_gs,m_gs]=GaussSeidelw(A,B,T_ast,tol,Imax,w(i));
    figure(1)
    plot(x0,T_gs)
    hold on
    figure(2)
    semilogy(res_gs)
    hold on
end
figure(1)
legend('Exact','\omega=1.1','\omega=1.2','\omega=1.3','\omega=1.4','\omega=1.5','\omega=1.6','\omega=1.7','\omega=1.8','\omega=1.9','\omega=2')

figure(2)
legend('\omega=1.1','\omega=1.2','\omega=1.3','\omega=1.4','\omega=1.5','\omega=1.6','\omega=1.7','\omega=1.8','\omega=1.9','\omega=2')







% w=1.1;
% while w<2.1
% 
%     [T_gs,res_gs,m_gs]=GaussSeidelw(A,B,T_ast,tol,Imax,w);
%     figure(1); plot(x0,T_gs)
%     hold on;
%     w=w+0.1;
% end
% figure(1); legend('Exact','\omega=1.1','\omega=1.2','\omega=1.3','\omega=1.4','\omega=1.5','\omega=1.6','\omega=1.7','\omega=1.8','\omega=1.9','\omega=2')
% xlabel('x (m)'); ylabel('T (K)')
% 
% w=1.1;
% while w<2.1
% 
%     [T_gs,res_gs,m_gs]=GaussSeidelw(A,B,T_ast,tol,Imax,w);
% 
%     figure(2); semilogy(res_gs)
%     res_gs(m_gs);
%     hold on
%     fprintf('w=%d, Niter=%d\n',w,m_gs)
%     w=w+0.1;
% end
% figure(2); legend('\omega=1.1','\omega=1.2','\omega=1.3','\omega=1.4','\omega=1.5','\omega=1.6','\omega=1.7','\omega=1.8','\omega=1.9','\omega=2')
% xlabel('Iterations'); ylabel('Residuals')