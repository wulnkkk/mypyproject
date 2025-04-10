f = open(r"C:\Users\86151\OneDrive\桌面\新建 文本文档.txt" ,"r",encoding='utf-8')
print("".join(f.read().split("\n")))