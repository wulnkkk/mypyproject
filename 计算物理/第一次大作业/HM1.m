clc;clear ;
X0=[0.1 0.1 -0.1]';
err=1e-5;
%雅可比迭代
n1=1 ;
X_old=X0;
X=cir1(X_old);
X_list1(:,n1)=X;
while norm(creatF(X))>err
    n1=n1+1;
    X_old=X;
    X=cir1(X_old);
    X_list1(:,n1)=X;
end
%高斯迭代
n2=1 ;
X_old=X0;
X=cir2(X_old);
X_list2(:,n2)=X;
while norm(creatF(X))>err
    n2=n2+1;
    X_old=X;
    X=cir2(X_old);
    X_list2(:,n2)=X;
end
%牛顿迭代
n3=1;
X_old=X0;
X=cir3(X_old);
X_list3(:,n3)=X;
while norm(creatF(X))>err
    n3=n3+1;
    X_old=X;
    X=cir3(X_old);
    X_list3(:,n3)=X;
end
function an=cir1(x)  %雅可比迭代式
    x1=x(1);x2=x(2);x3=x(3);
    x_1=1/6*(1+2*cos(x2*x3));
    x_2=1/9*(x1^2+sin(x3)+1.06)^(0.5)-0.1;
    x_3=-exp(-x1*x2)/20-(10*pi-3)/60;
    an=[x_1,x_2,x_3]';
end

function an=cir2(x)  %高斯迭代式 
    x2=x(2);x3=x(3);
    x1=1/6*(1+2*cos(x2*x3));
    x2=1/9*(x1^2+sin(x3)+1.06)^(0.5)-0.1; %与雅可比不同，赋值等号右边可以使用本次计算的结果x1
    x3=-exp(-x1*x2)/20-(10*pi-3)/60; 
    an=[x1,x2,x3]';
end

function F=creatF(x) %创建F向量
    x1=x(1);x2=x(2);x3=x(3);
    F1=3*x1-cos(x2*x3)-0.5;
    F2=x1^2-81*(x2+0.1)^2+sin(x3)+1.06;
    F3=exp(-x1*x2)+20*x3+(10*pi-3)/3;
    F=[F1,F2,F3]';
end
function J=creatJ(x) %创建雅可比矩阵
    x1=x(1);x2=x(2);x3=x(3);
    J=[3, -sin(x2*x3)*x3 ,-sin(x2*x3)*x2;2*x1,-81*2*(x2+0.1),cos(x3);-x2*exp(-x1*x2) ,-x1*exp(-x1*x2),20];
end
function an=cir3(x)  %牛顿迭代式
    J=creatJ(x);
    F=creatF(x);
    an=x-J^(-1)*F;
end
