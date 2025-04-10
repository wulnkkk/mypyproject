##进行一些高等数学相关的计算，导数，定积分，不定积分，行列式矩阵运算。
import sympy as sy    #导入符号运算库
import numpy
##设置未知量对象与代数表达式
x, y, z = sy.symbols("x y z") 
#设置变量未知数，在此对象中，其运算与打印的方法与普通的变量不同，而是符合数学中的符号代数运算的
expr=x+y+z+sy.cos(x)    #此时我们可以像数学中一样写出代数表达式，其同样有类似的打印与运算方法。

##替代&代入 代数运算中的一个基本技巧，以变量代替数值，以一个变量代替另一个较复杂的表达式，运算后再代回得出答案。

expr.subs(x,sy.cos(x)) #方法subs将x=y代入表达式并返回一个代入后的表达式

expr.subs([(x,30),(y,50)])  #可以一次替代多个变量


##浮点数值计算
(expr.subs([(x,20),(y,50),(z,20)])).evalf(10) #方法evalf可以将数值表达式转化为浮点值并返回，可指定精度
expr.evalf(10,subs={x:20,y:50,z:20})      #为上式的等价，即通过参数subs对表达式参数进行替代

##函数式计算
f = sy.lambdify([x,y,z], expr, "math")  #该函数可以将一个表达式作为函数输出，并指定库函数用以替代表达式中的同名函数
f = sy.lambdify([x,y,z], expr, {"cos":numpy.cos})  #也可以这样的方式替代


##打印
#SymPy 中提供了多种打印机。最常见的是
'''
str srepr; ASCII pretty printer; Unicode pretty printer; LaTeX;MathML;Dot;
'''

#设置最好的打印
sy.init_printing() #将自动启用最佳打印机的环境。

#设置一般运行环境
sy.init_session()  # 该函数将自动导入 SymPy 中的所有内容， 创建一些常用符号，设置绘图
#其等价于下面代码
'''
>>> from __future__ import division
>>> from sympy import *
>>> x, y, z, t = sy.symbols('x y z t')
>>> k, m, n = sy.symbols('k m n', integer=True)
>>> f, g, h = sy.symbols('f g h', cls=Function)
>>> sy.init_printing() 

'''
#sy.init_printing()设置打印环境的依据是根据编辑器而不同的。在一般的终端交互式窗口中，将适用Unicode pretty printer或 ASCII pretty printer

#主动选择打印形式并打印
#str式打印，可以使用str()将表达式变为代码字符串，直接使用print打印表达式就打印出此形式。
'''
>>> x, y, z = sy.symbols('x y z')
>>> str(Integral(sqrt(1/x), x))
 'Integral(sqrt(1/x), x)'
>>> print(Integral(sqrt(1/x), x))
 Integral(sqrt(1/x), x)
'''
#srepr形式，旨在显示表达式的确切形式，表明了表达式的数学含义，使用srepr()可直接打印出此形式
'''
>>> srepr(Integral(sqrt(1/x), x))
"Integral(Pow(Pow(Symbol('x'), Integer(-1)), Rational(1, 2)), Tuple(Symbol('x')))"
'''
#ASCII Pretty Printer与Unicode Pretty Printer
#使用pprint()可以打印出上两种形式的表达式通过传递参数use_unicode决定是否使用unicode形式
'''
>>> pprint(Integral(sqrt(1/x), x), use_unicode=False)
  /
 |
 |     ___
 |    / 1
 |   /  -  dx
 | \/   x
 |
/
>>> pprint(Integral(sqrt(1/x), x), use_unicode=True)
⌠
⎮     ___
⎮    ╱ 1
⎮   ╱  ─  dx
⎮ ╲╱   x
⌡
'''
#使用pretty()可以将上述两种形式的打印以其字符串形式打印
'''
>>> pretty(Integral(sqrt(1/x), x), use_unicode=False)
'  /          \n |           \n |     ___   \n |    / 1    \n |   /  -  dx\n | \\/   x    \n |           \n/            '

'''
#latex形式，在latex中表达式的编码形式，使用函数latex()可以将表达式转化为latex形式的编码字符串
'''
>>> print(latex(Integral(sqrt(1/x), x)))
\int \sqrt{\frac{1}{x}}\, dx
'''
#MathHL形式，网页中数学表达式的编码形式，使用ympy.printing.mathml中print_mathml函数可以打印出网页版表达式的编码字符串
'''
>>> from sympy.printing.mathml import print_mathml
>>> print_mathml(Integral(sqrt(1/x), x))
<apply>
    <int/>
    <bvar>
        <ci>x</ci>
    </bvar>
    <apply>
        <root/>
        <apply>
            <power/>
            <ci>x</ci>
            <cn>-1</cn>
        </apply>
    </apply>
</apply>
'''
#Dot形式，Graphviz中数学表达式的编辑形式，使用sympy.printing.dot中的dotprint()可以将表达式装转化为相应形式的编码字符串
'''
>>> from sympy.printing.dot import dotprint
>>> from sympy.abc import x
>>> print(dotprint(x+2))
digraph{

# Graph style
"ordering"="out"
"rankdir"="TD"

#########
# Nodes #
#########

"Add(Integer(2), Symbol('x'))_()" ["color"="black", "label"="Add", "shape"="ellipse"];
"Integer(2)_(0,)" ["color"="black", "label"="2", "shape"="ellipse"];
"Symbol('x')_(1,)" ["color"="black", "label"="x", "shape"="ellipse"];

#########
# Edges #
#########

"Add(Integer(2), Symbol('x'))_()" -> "Integer(2)_(0,)";
"Add(Integer(2), Symbol('x'))_()" -> "Symbol('x')_(1,)";
'''
##化简

#通用简化函数  
sy.simplify() #可以对表达式进行一些通用的简化
'''
>>> sy.simplify(sin(x)**2 + cos(x)**2)
1
>>> sy.simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))
x - 1
>>> sy.simplify(gamma(x)/gamma(x - 2))
(x - 2)⋅(x - 1)
'''
#多项式/有理函数简化
sy.expand() #可以将有理多项式展开为单项式
'''
>>> expand((x + 1)**2)
 2
x  + 2⋅x + 1
>>> expand((x + 2)*(x - 3))
 2
x  - x - 6
'''
#因式分解
sy.factor()  #可以将式子因式分解到不可约有理式，即分子分母不含相同因式
'''
>>> sy.factor(x**3 - x**2 + x - 1)
        / 2    \
(x - 1)*\x  + 1/
>>> sy.factor(x**2*z + 4*x*y*z + 4*y**2*z)
           2
z⋅(x + 2⋅y)
'''
sy.factor_list()  #可以将简化后的式子的因式以列表形式列出,具体返回形式如下
'''
>>> factor_list(x**2*z + 4*x*y*z + 4*y**2*z)
(1, [(z, 1), (x + 2⋅y, 2)])
'''
#合并同类项
sy.collect()  #可以将多项式中的同类型合并
'''
>>> expr = x*y + x - 3 + 2*x**2 - z*x**2 + x**3
>>> expr
 3    2        2
x  - x ⋅z + 2⋅x  + x⋅y + x - 3
>>> collected_expr = collect(expr, x)
>>> collected_expr
 3    2
x  + x ⋅(2 - z) + x⋅(y + 1) - 3
'''
expr.coeff() #该方法可以给出某一项的系数
'''
>>> collected_expr.coeff(x, 2)
2 - z
'''
#约分cancel
sy.cancel() #可以将有理式化为最简有理分式，即只有一个分式，分子分母不含相同同因式，各自为展开后的形式
'''
>>> sy.cancel((x**2 + 2*x + 1)/(x**2 + x))
x + 1
─────
  x
>>> expr = 1/x + (3*x/2 - 2)/(x - 4)
>>> expr
3⋅x
─── - 2
 2        1
─────── + ─
 x - 4    x
>>> sy.cancel(expr)
   2
3⋅x  - 2⋅x - 8
──────────────
     2
  2⋅x  - 8⋅x
>>> expr = (x*y**2 - 2*x*y*z + x*z**2 + y**2 - 2*y*z + z**2)/(x**2 - 1)
>>> expr
   2                2    2            2
x⋅y  - 2⋅x⋅y⋅z + x⋅z  + y  - 2⋅y⋅z + z
───────────────────────────────────────
                  2
                 x  - 1
>>> sy.cancel(expr)
 2            2
y  - 2⋅y⋅z + z
───────────────
     x - 1
'''
#请注意，由于将完全分解表达式的分子和分母，factor()也可以用来做同样的事情：
'''
>>> sy.factor(expr)
       2
(y - z)
────────
 x - 1
'''
#但是，如果您只想确保表达式处于cancel的形式，cancel()比factor()更有效
#裂项or部分分数分解
sy.apart() #可以将有理分式拆分为真分式的和
'''
>>> expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
>>> expr
   3       2
4⋅x  + 21⋅x  + 10⋅x + 12
────────────────────────
  4      3      2
 x  + 5⋅x  + 5⋅x  + 4⋅x
>>> sy.apart(expr)
 2⋅x - 1       1     3
────────── - ───── + ─
 2           x + 4   x
x  + x + 1
'''
#三角函数简化
sy.trigsimp()#使用三角恒等式简化表达式.
'''
>>> sy.trigsimp(sin(x)**2 + cos(x)**2)
1
>>> trigsimp(sin(x)**4 - 2*cos(x)**2*sin(x)**2 + cos(x)**4)
cos(4⋅x)   1
──────── + ─
   2       2
>>> trigsimp(sin(x)*tan(x)/sec(x))
   2
sin (x)
'''
# trigsimp()也适用于双曲三角函数。
'''
>>> sy.trigsimp(cosh(x)**2 + sinh(x)**2)
cosh(2⋅x)
>>> sy.trigsimp(sinh(x)/tanh(x))
cosh(x)
'''
#trigsimp()和simplify()很像,trigsimp()将各种三角恒等式应用于 输入表达式,simplify()使用启发式返回“最佳”表达式。
sy.expand_trig() #可以使用三角函数的和差公式与倍角公式将三角式展开
'''
>>> expand_trig(sin(x + y))
sin(x)⋅cos(y) + sin(y)⋅cos(x)
>>> expand_trig(tan(2*x))
  2⋅tan(x)
───────────
       2
1 - tan (x)
'''
#幂运算化简
'''
三条幂运算律在复数域上并不完全成立，其有成立条件
通常限定
x, y = symbols('x y', positive=True) 正值
a, b = symbols('a b', real=True)     实值 
z, t, c = symbols('z t c')           任意值
'''
sy.powsimp() #将同底的幂的乘积化为指数的和，或将同指数的幂的乘积先乘积再取幂。
'''
>>> sy.powsimp(x**a*x**b)
  a + b
 x
>>> sy.powsimp(x**a*y**a)
     a
(x⋅y)
'''
#请注意，如果输入表达式无效，powsimp()则拒绝进行简化。
'''
>>> powsimp(t**c*z**c)
 c  c
t ⋅z
'''
#如果您知道要应用此简化，但又不想改变假设，你可以传递旗帜force=True。这将迫使 无论假设如何，都要进行简化。
'''
>>> sy.powsimp(t**c*z**c, force=True)
     c
(t⋅z)
'''
#请注意，在某些情况下，特别是当幂指数为整数或有理数和恒等式时，积的幂将自动展开。
'''
(z*t)**2
  2  2
 t ⋅z
sqrt(x*y)
 √x⋅√y
'''
#这意味着不可能用撤消这种过程，因为即使将基础放在一起， 它们将再次自动分开。powsimp()powsimp()
'''
>>> sy.powsimp(z**2*t**2)
  2  2
 t ⋅z
>>> sy.powsimp(sqrt(x)*sqrt(y))
 √x⋅√y
'''

sy.expand_power_exp()#将展开“幂中指数和”为“幂的积”
sy.expand_power_base()#将展开“积的幂”为“幂的积”
'''
>>> expand_power_exp(x**(a + b))
 a  b
x ⋅x
>>> expand_power_base((x*y)**a)
 a  a
x ⋅y
'''
#与powsimp() 一样，如果输入无效，则不应用它。
'''
>>> sy.expand_power_base((z*t)**c)
     c
(t⋅z)
'''
#和powsimp()一样，你可以通过使用参数force=True强制扩展发生。
'''
>>> sy.expand_power_base((z*t)**c, force=True)
  c  c
 t ⋅z
'''
#注意幂为数字，同底幂的积将自动合并，并且不能用 expand_power_exp()撤消。
'''
>>> x**2*x**3
  5
 x
>>> sy.expand_power_exp(x**5)
  5
 x
''' 
sy.powdenest() #将“幂的幂”化为指数的积
'''
>>> sy.powdenest((x**a)**b)
 a⋅b
x
'''
#如前所述，如果恒等式在给定的条件下不为真，则不应用该恒等式 假设。
'''
>>> sy.powdenest((z**a)**b)
    b
⎛ a⎞
⎝z ⎠
'''
#和以前一样，这可以强制进行。使用参数force=True
'''
>>> sy.powdenest((z**a)**b, force=True)
 a⋅b
z
'''
#对数运算简化
pass

##微积分
#导数
sy.diff()#可以获得表达式的导数
'''
>>> sy.diff(cos(x), x)
-sin(x)
>>> sy.diff(exp(x**2), x)

     ⎛ 2⎞
     ⎝x ⎠
2⋅x⋅ℯ
'''
#diff()可以进行多次求导，即高阶导数,下面两种调用方式结果相同
'''
>>> sy.diff(x**4, x, x, x)
24⋅x
>>> sy.diff(x**4, x, 3)
24⋅x
'''
#diff()也可以对多个变量求导，即偏导数，下面几种调用方式结果相同
'''
>>> expr = exp(x*y*z)
>>> diff(expr, x, y, y, z, z, z, z)
 
 3  2 ⎛ 3  3  3       2  2  2                ⎞  x⋅y⋅z
x ⋅y ⋅⎝x ⋅y ⋅z  + 14⋅x ⋅y ⋅z  + 52⋅x⋅y⋅z + 48⎠⋅ℯ

>>> sy.diff(expr, x, y, 2, z, 4)

 3  2 ⎛ 3  3  3       2  2  2                ⎞  x⋅y⋅z
x ⋅y ⋅⎝x ⋅y ⋅z  + 14⋅x ⋅y ⋅z  + 52⋅x⋅y⋅z + 48⎠⋅ℯ

>>> sy.diff(expr, x, y, y, z, 4)

 3  2 ⎛ 3  3  3       2  2  2                ⎞  x⋅y⋅z
x ⋅y ⋅⎝x ⋅y ⋅z  + 14⋅x ⋅y ⋅z  + 52⋅x⋅y⋅z + 48⎠⋅ℯ
'''
#diff也可以作为表达式的方法使用，语法不变。
'''
>>> expr.diff(x, y, y, z, 4)

 3  2 ⎛ 3  3  3       2  2  2                ⎞  x⋅y⋅z
x ⋅y ⋅⎝x ⋅y ⋅z  + 14⋅x ⋅y ⋅z  + 52⋅x⋅y⋅z + 48⎠⋅ℯ
'''
sy.Derivative() #可以创建不进行计算的导数表达式 ，语法与diff相同
'''
>>> deriv = sy.Derivative(expr, x, y, y, z, 4)
>>> deriv
     7
    ∂     ⎛ x⋅y⋅z⎞
──────────⎝ℯ     ⎠
  4   2
∂z  ∂y  ∂x
'''
#要计算未计算的导数，请使用该方法doit。
'''
>>> deriv.doit()

 3  2 ⎛ 3  3  3       2  2  2                ⎞  x⋅y⋅z
x ⋅y ⋅⎝x ⋅y ⋅z  + 14⋅x ⋅y ⋅z  + 52⋅x⋅y⋅z + 48⎠⋅ℯ
'''
#可以通过传递元组参数，创建未知阶数的导数。
'''
>>> m, n, a, b = sy.symbols('m n a b')
>>> expr = (a*x + b)**m
>>> expr.diff((x, n))
  n
 ∂ ⎛         m⎞
───⎝(a⋅x + b) ⎠
  n
∂x
'''
#积分
sy.integrate()#可以对表达式进行积分，返回其不定积分or原函数or反导数;
'''
>>> sy.integrate(cos(x), x)
-sin(x)
'''
#可以通过传递参数(integration_variable, lower_limit, upper_limit)来计算定积分
'''
>>> sy.integrate(exp(-x), (x, 0, oo))   #sympy中将oo视为无穷大
1
'''
#可以传递多个元组来执行多重积分。
'''
>>> sy.integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))
π
'''
#如果无法计算积分，则返回未计算的表达式对象；
'''
>>> expr = integrate(x**x, x)
>>> print(expr)
Integral(x**x, x)
>>> expr
⌠
⎮  x
⎮ x  dx
⌡
'''
sy.Integral()#可以创建不计算的积分表达式，语法同integrate;同样使用方法doit计算表达式
'''
>>> expr = Integral(log(x)**2, x)
>>> expr
⌠
⎮    2
⎮ log (x) dx
⌡
>>> expr.doit()
         2
x⋅log (x) - 2⋅x⋅log(x) + 2⋅x
'''