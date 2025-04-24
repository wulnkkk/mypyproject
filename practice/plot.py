# 画图模板示例文件 
import numpy as np                
import matplotlib.pyplot as plt   
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号

#绘制简单的折线图
# 准备数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
# 绘制折线图
plt.plot(x, y, label="Line 1", color="blue", marker="o", linestyle="--")
# 添加标题和标签
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
# 添加图例
plt.legend()
# 显示图形
plt.show()

#绘制散点图
# 准备数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
# 绘制散点图
plt.scatter(x, y, color="red", marker="*", s=100)  # s 是点的大小
# 添加标题和标签
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
# 显示图形
plt.show()

#绘制柱状图
# 准备数据
categories = ["A", "B", "C", "D"]
values = [10, 15, 7, 12]
# 绘制柱状图
plt.bar(categories, values, color=["red", "green", "blue", "purple"])
# 添加标题和标签
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
# 显示图形
plt.show()

#绘制饼图
# 准备数据
labels = ["A", "B", "C", "D"]
sizes = [10, 15, 7, 12]
colors = ["red", "green", "blue", "purple"]
# 绘制饼图
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
# 添加标题
plt.title("Pie Chart")
# 显示图形
plt.show()

#绘制多图（子图）
# 准备数据
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 9, 16, 25]
# 创建一个图形和子图
fig, (ax1, ax2) = plt.subplots(2, 1)  # 2 行 1 列的子图
# 在第一个子图中绘制折线图
ax1.plot(x, y1, label="Line 1", color="blue")
ax1.set_title("Line Plot")
ax1.set_xlabel("X-axis")
ax1.set_ylabel("Y-axis")
ax1.legend()
# 在第二个子图中绘制柱状图
ax2.bar(x, y2, color="green")
ax2.set_title("Bar Chart")
ax2.set_xlabel("X-axis")
ax2.set_ylabel("Values")
# 调整子图间距
plt.tight_layout()
# 显示图形
plt.show()

#自定义图形
#添加网格
plt.grid(True)
#设置坐标轴范围
plt.xlim(0, 10)
plt.ylim(0, 20)
#自定义图例位置
plt.legend(loc="upper right")  # 可选位置：best, upper right, upper left, lower left, lower right, right, center left, center right, lower center, upper center, center
#保存图形
plt.savefig("figure.png")  # 保存为 PNG 格式
plt.savefig("figure.pdf")  # 保存为 PDF 格式
