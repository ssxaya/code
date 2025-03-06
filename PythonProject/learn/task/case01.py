"""
    案例: 计算圆面积
    技术：输入输出、异常捕获
    日期: 2025-03-05
"""
# 定义PI常量
PI= 3.1415926
# 输入圆半径
str= input(":")
# 打印圆半径
print(f"r={str}")

# 异常
try:
    # 转换数据类型为float
    r = float(str)
except ValueError:
    # 如果报错
    print("数值不合法")
else:
    # 如果未报错
    # 计算并打印
    area = PI * r * r
    print(f"\ns={area}")

input()