from solver import encrypt_data_ecb, decrypt_data_ecb
from generate import key_generate
import base64
import sys

def load_passwords(password_file, password):
    try:
        with open(password_file, 'r', encoding='utf-8') as f:
            n = f.read(4)
            if not n.isdigit():
                if n == "":
                    n = 0
                else:
                    print("密码库地址有误，或出现数据遗失损坏")
                    sys.exit(0)
            else:
                n = int(n)
            if n > 0:
                encrypt_data = base64.b64decode(f.read().encode("utf-8"))
                data = decrypt_data_ecb(encrypt_data, password)
                return eval(data), n
            else:
                return {}, 0
    except Exception as e:
        print(f"加载密码库时出错: {e}")
        sys.exit(0)

def save_passwords(password_file, password, passwords, count):
    try:
        new_data = base64.b64encode(encrypt_data_ecb(str(passwords), password)).decode('utf-8')
        with open(password_file, 'w', encoding='utf-8') as f:
            f.write(f"{count:04}")
            f.write(new_data)
    except Exception as e:
        print(f"保存密码库时出错: {e}")
        sys.exit(0)
        
def create_password(password_file, password):
    yn = '2'
    number = 0
    while yn != '1' and number < 20:
        note = input("请输入您的提示语（由小写字母构成的字符串）: ")
        if note.islower() and note.isalpha():
            passwords, count = load_passwords(password_file, password)
            if note in passwords:
                print(f"提示语 '{note}' 已经存在，对应的密码是: {passwords[note]}")
                yn = input("是否重新输入提示语（是=1，退出=quit）: ")
                if yn == '1':
                    continue
                elif yn == 'quit':
                    break
            key = key_generate(note)
            yn = input(f"您的提示语和密码是 {note} : {key}, 是否满意（是=1，不是=2，退出=quit）: ")
            if yn == '1':
                passwords[note] = key
                save_passwords(password_file, password, passwords, count + 1)
                print(f"您的第{count + 1}个密码已经存入密码库")
                break
        else:
            print("您输入的提示语有误")
        number += 1

def display_password_count(password_file, password):
    """
    显示密码库中的密码个数
    """
    passwords, count = load_passwords(password_file, password)
    if count == 0:
        print("密码库为空，无密码可显示。")
    else:
        print(f"密码库中共有 {count} 个密码。")

def query_password(password_file, password):
    """
    查询密码功能
    """
    passwords, count = load_passwords(password_file, password)
    if count == 0:
        print("密码库为空，请先创建密码。")
        return

    # 显示密码库中的密码数量
    display_password_count(password_file, password)

    yn = '2'
    number = 0
    while yn != '1' and number < 20:
        note = input("请输入您的提示语（由小写字母构成的字符串）: ")
        if note in passwords:
            print(f"您的提示语和密码是 {note} : {passwords[note]}")
            yn = input("密码是否正确（是=1，不是=2，退出=quit）: ")
        else:
            print("您输入的提示语不存在于密码库中。")
        number += 1

def delete_password(password_file, password):
    """
    删除密码功能
    """
    passwords, count = load_passwords(password_file, password)
    if count == 0:
        print("密码库为空，请先创建密码。")
        return

    # 显示密码库中的密码数量
    display_password_count(password_file, password)

    yn = '2'
    number = 0
    while yn != '1' and number < 20:
        note = input("请输入您想删除密码的提示语（由小写字母构成的字符串）或所有密码（all）: ")
        if note in passwords:
            del passwords[note]
            save_passwords(password_file, password, passwords, count - 1)
            print(f"提示语 '{note}' 及其密码已被删除。")
            yn = input("是否继续删除密码（是=0，否＝1，退出=quit）: ")
        elif note == "all":
            yn = input("您是否确定删除所有密码（是=1，不是=2，退出=quit）: ")
            if yn == '1':
                save_passwords(password_file, password, {}, 0)
                print("所有密码已删除。")
                break
        else:
            print("您输入的提示语不存在于密码库中。")
        number += 1

if __name__ == '__main__':
    password_file = r"PL.txt"
    f=open(r"password.txt","r",encoding="UTF-8")
    t=f.read()
    password = t.encode("UTF-8")
    print("欢迎使用密码管理工具")
    choice = input("创建密码请按1，查询密码请按2，删除密码请按3: ")
    if choice == "1":
        create_password(password_file, password)
    elif choice == "2":
        query_password(password_file, password)
    elif choice == "3":
        delete_password(password_file, password)
    else:
        print("无效的选项")