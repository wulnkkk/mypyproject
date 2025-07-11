from solver import encrypt_data_ecb, decrypt_data_ecb
from generate import key_generate
import base64
import sys

##过程函数
def load_passwords(password_file, password):
    '''
    加载密码库
    '''
    try:
        with open(password_file, 'r', encoding='utf-8') as f:
            count_str = f.read(4)
            if not count_str.isdigit():
                if count_str == "":
                    count = 0
                else:
                    print("密码库地址有误，或出现数据遗失损坏")
                    sys.exit(0)
            else:
                count = int(count_str)
            if count > 0:
                encrypt_data = base64.b64decode(f.read().encode("utf-8"))
                data = decrypt_data_ecb(encrypt_data, password)
                return eval(data), count
            else:
                return {}, 0
    except Exception as e:
        print(f"加载密码库时出错: {e}")
        sys.exit(0)


def save_passwords(password_file, password, passwords, count):
    '''
    保存密码库
    '''
    try:
        new_data = base64.b64encode(encrypt_data_ecb(str(passwords), password)).decode('utf-8')
        with open(password_file, 'w', encoding='utf-8') as f:
            f.write(f"{count:04}")
            f.write(new_data)
    except Exception as e:
        print(f"保存密码库时出错: {e}")
        sys.exit(0)

##流程函数
def create_password(password_file, password):
    '''
    创建密码
    '''
    passwords, count = load_passwords(password_file, password)
    while True:
        note = input("请输入您的提示语（由小写字母构成的字符串）: ").strip()
        if not note.islower() or not note.isalpha():
            print("提示语必须是小写字母。")
            if input("是否重新输入提示语（是=1，退出=其它任意键）: ").strip().lower() == '1':
                continue
            else:
                print("操作已取消。")
                return  # 提前退出函数
        if note in passwords:
            print(f"提示语 '{note}' 已经存在。")
            if input("是否重新输入提示语（是=1，退出=其它任意键）: ").strip().lower() == '1':
                continue
            else:
                print("操作已取消。")
                return  # 提前退出函数

        key = key_generate(note)
        print(f"您的提示语和密码是 {note} : {key}")
        while True:
            choice = input("是否满意（是=1，不是=2，退出=其它任意键）: ").strip().lower()
            if choice == '1':  # 满意并保存
                passwords[note] = key
                save_passwords(password_file, password, passwords, count + 1)
                print(f"您的第{count + 1}个密码已经存入密码库")
                return  # 保存成功后退出函数
            elif choice == '2':  # 不满意，重新创建
                break  # 跳出内层循环，重新开始外层循环
            elif choice == 'quit':  # 直接退出
                print("操作已取消。")
                return  # 提前退出函数
            else:
                print("无效的选项，请重新输入。")

def query_password(password_file, password):
    '''
    查询密码
    '''
    passwords, count = load_passwords(password_file, password)
    if count == 0:
        print("密码库为空，请先创建密码。")
        return
    
    print(f"密码库中共有 {count} 个密码。")
    
    while True:
        note = input("请输入您的提示语（由小写字母构成的字符串）: ").strip()
        if not note.islower() or not note.isalpha():
            print("提示语必须是小写字母。")
            if input("是否重新输入提示语（是=1，退出=其它任意键）: ").strip().lower() == '1':
                continue
            else:
                print("操作已取消。")
                return
        if note in passwords:
            print(f"您的提示语和密码是 {note} : {passwords[note]}")
            while True:
                choice = input("密码是否正确（是=1，不是=2，退出=其它任意键）: ").strip().lower()
                if choice == '1':
                    print("查询成功。")
                    return
                elif choice == '2':
                    print("密码不正确。")
                    if input("是否继续查询其它密码（是=1，退出=其它任意键）: ").strip().lower() == '1':
                        break
                    else:
                        print("操作已取消。")
                        return
                else:
                    print("操作已取消。")
                    return

        else:
            print("您输入的提示语不存在于密码库中。")
            if input("是否继续查询其它密码（是=1，退出=其它任意键）: ").strip().lower() == '1':
                continue
            else:
                print("操作已取消。")
                return



def delete_password(password_file, password):
    '''
    删除密码功能
    '''
    passwords, count = load_passwords(password_file, password)
    if count == 0:
        print("密码库为空，请先创建密码。")
        return

    print(f"密码库中共有 {count} 个密码。")

    while True:
        note = input("请输入您想删除密码的提示语（由小写字母构成的字符串）或所有密码（all）: ").strip()
        if note == "all":
            if input("您是否确定删除所有密码（是=1，不是=其它任意键）: ").strip().lower() == '1':
                save_passwords(password_file, password, {}, 0)
                print("所有密码已删除。")
                break
            else:
                print("操作已取消。")
                break
        elif note in passwords:
            del passwords[note]
            save_passwords(password_file, password, passwords, count - 1)
            print(f"提示语 '{note}' 及其密码已被删除。")
            if input("是否继续删除密码（是=1，否=其它任意键）: ").strip().lower() == '1':
                continue
            else:
                print("操作已取消。")
                break
        else:
            print("您输入的提示语不存在于密码库中。")
            if input("是否继续删除密码（是=1，否=其它任意键）: ").strip().lower() == '1':
                continue
            else:
                print("操作已取消。")
                break

def save_manual_password(password_file, password):
    """
    手动保存密码功能
    """
    passwords, count = load_passwords(password_file, password)
    print(f"当前密码库中共有 {count} 个密码。")

    while True:
        note = input("请输入您的提示语（由小写字母构成的字符串）: ").strip()
        if not note.islower() or not note.isalpha():
            print("提示语必须是小写字母。")
            if input("是否重新输入提示语（是=1，退出=其它任意键）: ").strip().lower() == '1':
                continue
            else:
                print("操作已取消。")
                return
        if note in passwords:
            print(f"提示语 '{note}' 已经存在。")
            if input("是否重新输入提示语（是=1，退出=其它任意键）: ").strip().lower() == '1':
                continue
            else:
                print("操作已取消。")
                return
        user_password = input(f"请输入您要保存的密码（对应提示语 '{note}'）: ").strip()
        passwords[note] = user_password
        save_passwords(password_file, password, passwords, count + 1)
        print(f"密码已成功保存到密码库，提示语为 '{note}'。")
        if input("是否继续保存其它密码（是=0，否=其它任意键）: ").strip().lower() == '0':
            continue
        else:
            print("操作已完成。")
            break

##主程序
if __name__ == '__main__':
    password_file = r"PL.txt"
    try:
        with open(r"password.txt", "r", encoding="UTF-8") as f:
            password = f.read().strip().encode("UTF-8")
    except FileNotFoundError:
        print("主密钥文件未找到，请确保文件存在。")
        sys.exit(0)
    print("欢迎使用密码管理工具")
    choice = input("创建密码请按1，查询密码请按2，删除密码请按3，手动保存密码请按4: ").strip()
    if choice == "1":
        create_password(password_file, password)
    elif choice == "2":
        query_password(password_file, password)
    elif choice == "3":
        delete_password(password_file, password)
    elif choice == "4":
        save_manual_password(password_file, password)
    else:
        print("无效的选项")

