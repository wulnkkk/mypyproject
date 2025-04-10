from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
def encrypt_data_ecb(data, key):
    """使用AES的ECB模式加密数据"""
    # 初始化AES加密器
    cipher = AES.new(key, AES.MODE_ECB)  # 使用ECB模式
    # 对数据进行填充（AES要求数据长度为16的倍数）
    padded_data = pad(data.encode('utf-8'), AES.block_size)
    # 加密数据
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

def decrypt_data_ecb(encrypted_data, key):
    """使用AES的ECB模式解密数据"""
    # 初始化AES解密器
    cipher = AES.new(key, AES.MODE_ECB)  # 使用ECB模式
    # 解密数据
    decrypted_data = cipher.decrypt(encrypted_data)
    # 去除填充
    unpadded_data = unpad(decrypted_data, AES.block_size)
    return unpadded_data.decode('utf-8')

# 示例使用
if __name__ == "__main__":
    #AES密钥
    key = b'1dfd92asdas2sd83'
    print(f"生成的AES密钥（16字节）: {base64.b64encode(key).decode('utf-8')}")

    # 明文数据
    plaintext = "Hello, AES ECB Mode!"
    print(f"明文: {plaintext}")

    # 加密数据
    encrypted_data = encrypt_data_ecb(plaintext, key)
    print(f"加密后的数据（Base64编码）: {base64.b64encode(encrypted_data).decode('utf-8')}")

    # 解密数据
    decrypted_data = decrypt_data_ecb(encrypted_data, key)
    print(f"解密后的数据: {decrypted_data}")