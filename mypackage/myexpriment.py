# ##有效数字运算的实现
# def exactdigit(a):




















#     '''
#     a为科学计数法的数据,标准为1.345e10或1.465e-5,且输入字符串
#     必须含e,不一定有点.返回最小有效位,以个位为零
#     如1.654e3,4为个位,返回0,以及有效位数
#     '''
#     if '-'in a:
#         a=a[1:]
#     if '.' in a:
#         edot=a.find('e')
#         x=a[:edot]   #数据值
#         y=eval(a[edot+1:]) #数量级
#         exactlen=len(x)-1 #有效位数
#         s=-(edot-2)+y        #有效位的在值中的序
#     else:
#         edot=a.find('e')
#         x=a[:edot]   #数据值
#         y=eval(a[edot+1:]) #数量级
#         exactlen=1 #有效位数
#         s=y      #有效位的在值中的序 
#     return s,exactlen
# def maxdigit(a):
#     """
#     a为任意实数,形式为一般数且为float,返回a的最高位数
#     如165.33,返回2
#     """
#     a=str(a)
#     if '-'in a:
#         a=a[1:]
#     dot=a.find('.')
#     x=a[:dot]   #整数值
#     y=a[dot+1:] #小数值
#     if x !='0':
#         s=len(x)-1  #整数部分最高位
#     else:
#         s=0         #小数部分最高位
#         for i in y:
#             if i == '0':
#                 s-=1
#             else:
#                 s-=1
#                 break
#     return s        
# def exactadd(a,b,*args):
#     '''
#     a,b为科学计数法的数据,标准为1.345e10或1.465e-5,且输入字符串
#     '''
#     if args==():
#         a1,a2=exactdigit(a)
#         b1,b2=exactdigit(b)
#         if a1>b1:
#             all=eval(a)+eval(b)#运算
#             digit=maxdigit(sum)-a1+1
#             return '{:e}'.format(all,precision=digit-1)
#         if b1>a1:
#             all=eval(a)+eval(b)#运算
#             digit=maxdigit(sum)-b1+1
#             s='{:e}'.format(all,precision=digit-1)
#             return s
# 
