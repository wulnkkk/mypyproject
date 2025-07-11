import os

def read_and_split(file_path, chunk_size=5):
    """
    读取文件内容并按指定长度分割成块
    :param file_path: 文件路径
    :param chunk_size: 每个块的长度
    :return: 分割后的块列表
    """
    if not os.path.exists(file_path):
        print(f"文件 {file_path} 不存在，请检查文件路径。")
        return []  # 返回空列表或抛出异常，根据需求选择
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()  # 读取文件内容并去除首尾空格
    return [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]

# 读取并分割 Constant1.txt 和 Constant2.txt
a = read_and_split(r"Constant1.txt")
b = read_and_split(r"Constant2.txt")
if not a or not b:
    print("由于文件读取失败，程序将退出。")
    exit()  # 如果文件不存在，退出程序
_Constant = [a, b]

def key_generate(astr: str) -> str:
    '''
    astr: 小写英文字母组成的字符串
    '''
    _alist = 'abcdefghijklmnopqrstuvwxyz'  # 使用标准的字母表
    half_len = len(astr) // 2  # 计算字符串的中点位置
    tstr = [astr[:half_len], astr[half_len:]]  # 分割字符串为两部分
    key1 = tstr[0][0] + tstr[1][0]  # 取每部分的第一个字符作为 key1

    key2 = []
    key3 = []
    for x in range(2):
        num = sum(_alist.index(i) for i in tstr[x])  # 计算每部分的字母索引和
        key2.append(_alist[num // len(tstr[x])])  # 计算 key2 的字符
        key3.append(_Constant[x][num // len(tstr[x])])  # 计算 key3 的字符

    # 组合最终的密码
    key = key1.capitalize() + "@" + key2[0].capitalize() + key2[1] + '#' + key3[0] + key3[1]
    return key
