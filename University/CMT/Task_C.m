clear all
close all
clc

maxI=1000;
tol=1e-8;
c=4;
x=-3; y=-3; z=-3;%Initial guess

error=sum(abs(x*exp(y)+z+1)+abs(y*z-x^3-pi())+abs(x*y^2*z-(3+(c/10))));
i=1;
while error(i)>tol & i<maxI
    J(1,1)=exp(y(i)); %du/dx
    J(1,2)=x(i)*exp(y(i)); %du/dy
    J(1,3)=1; %du/dz
    J(2,1)=-3*x(i)^2; %dv/dx
    J(2,2)=z(i); %dv/dy
    J(2,3)=y(i); %dv/dz
    J(3,1)=y(i)^2*z(i); %dw/dx
    J(3,2)=2*x(i)*y(i)*z(i); %dw/dy
    J(3,3)=x(i)*y(i)^2; %dw/dz

    F(1,1)=x(i)*exp(y(i))+z(i)+1;   % u(x(i),y(i),z(i))
    F(2,1)=y(i)*z(i)-x(i)^3-pi();   % v(x(i),y(i),z(i))
    F(3,1)=x(i)*y(i)^2*z(i)-(3+(c/10));    % w(x(i),y(i),z(i))

    X(1,1)=x(i); X(2,1)=y(i); X(3,1)=z(i);

    X=J\(-F+J*X);
    x(i+1)=X(1); y(i+1)=X(2); z(i+1)=X(3);  %New guesses

    F(1)=x(i+1)*exp(y(i+1))+z(i+1)+1;
    F(2)=y(i+1)*z(i+1)-x(i+1)^3-pi();
    F(3)=x(i+1)*y(i+1)^2*z(i+1)-(3+(c/10));

    error(i+1)=sum(abs(F));
    i=i+1;
end

figure
plot(x,'o-'); grid on; hold on
plot(y,'o-'); plot(z,'o-')
legend('x','y','z')
xlabel('Iterations'); ylabel('Solution')

figure
semilogy(error,'o-')
xlabel('Iterations'); ylabel('Error')


