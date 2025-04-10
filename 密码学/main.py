from  solver import encrypt_data_ecb,decrypt_data_ecb
from generate import key_generate
import base64,sys
##密钥##
if __name__ =='__main__':
    _pw=b'1415926571828183'
else:
    sys.exit(0)

##主程序
x=input("创建密码请按1，查询密码请按2，删除密码请按3")
if x=="1":
    yn=0
    number=0
    while (yn!='1')and (number<20)and (yn !='quit'):
        note=input("请输入您的提示语（由小写字母构成的字符串）")
        if note.islower() and note.isalpha() :
            key=key_generate(note)
            yn=input("您的提示语和密码是{:} : {:},是否满意（是=1，不是=2，退出=quit）".format(note,key))
        else :
            print('您输入的提示语有误')
    if yn=='1':
        dit={}
        dit={note:key}
        f=open(r"PL.txt",'r',encoding='utf-8') 
        n=f.read(4)
        if n.isdigit() !=True:
            if n=="":
                n=0
            else:
                print("密码库地址有误，或出现数据遗失损坏")
                sys.exit(0)
        else:
            n=int(n)
        if n>=1:
            encrypt_data=base64.b64decode(f.read().encode("utf-8"))
            data=decrypt_data_ecb(encrypt_data,_pw)
            old=eval(data)
            f.close()
        else:
            old={}
        old.update(dit)
        new=old
        new=base64.b64encode(encrypt_data_ecb(str(new),_pw)).decode('utf-8')
        n+=1
        f=open(r"PL.txt",'w',encoding='utf-8')
        f.write("{:0>4}".format(str(n)))
        f.write(new)
        f.close()
        print("您的第{:}个密码已经存入密码库".format(n))
elif x=='2' :
    f=open(r"PL.txt",'r',encoding='utf-8')
    n=f.read(4)
    if n.isdigit() !=True:
        if n=="":
            n=0
        else:
            print("密码库地址有误，或出现数据遗失损坏")
            sys.exit(0)
    elif n=='0000':
        print("您的密码库中无密码，请重启程序创建密码")
        sys.exit(0)
    else:
        n=int(n)
    encrypt_data=base64.b64decode(f.read().encode("utf-8"))
    f.close()
    data=decrypt_data_ecb(encrypt_data,_pw)
    old=eval(data)
    yn=0
    number=0
    while (yn!='1') and (number <20)and (yn !='quit'):
        note=input("请输入您的提示语（由小写字母构成的字符串）")
        number+=1
        if note in old.keys():
            print("您的提示语和密码是{:} : {:}".format(note,old[note]))
            yn=input("密码是否正确(是=1，不是=2，退出=quit)")
        else :
            print("您输入的提示语有误")
elif x=="3":
    f=open(r"PL.txt",'r',encoding='utf-8')
    n=f.read(4)
    if n.isdigit() !=True:
        if n=="":
            n=0
        else:
            print("密码库地址有误，或出现数据遗失损坏")
            sys.exit(0)
    elif n=='0000':
        print("您的密码库中无密码，请重启程序创建密码")
        sys.exit(0)
    else:
        n=int(n)
    encrypt_data=base64.b64decode(f.read().encode("utf-8"))
    f.close()
    data=decrypt_data_ecb(encrypt_data,_pw)
    old=eval(data)
    yn=0
    number=0
    while (yn!='1') and (number <20) and (yn !='quit'):
        note=input("请输入您想删除密码的提示语（由小写字母构成的字符串）or所有密码 （all）")
        number+=1
        if note in old.keys():
            n-=1
            print("您的提示语和密码{:} : {:}已经删除".format(note,old[note]))
            del old[note]
            new=old
            new=base64.b64encode(encrypt_data_ecb(str(new),_pw)).decode('utf-8')
            f=open(r"PL.txt",'w',encoding='utf-8')
            f.write("{:0>4}".format(str(n)))
            f.write(new)
            f.close()
            yn=input("是否继续删除密码(是=1，退出=quit)")
        elif note == "all":
            yn=input("您是否确定删除所有密码（是=1，不是=2，退出=quit）")
            if yn=='1':
                n=0
                old={}
                new=''
                f=open(r"PL.txt",'w',encoding='utf-8')
                f.write("{:0>4}".format(str(n)))
                f.write(new)
                f.close()
                print("您的所有提示语和密码已经删除")
        else :
            print("您输入的提示语有误")