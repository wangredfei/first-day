#   1. 输入一个整数n代表结束的数值,求下列表达式的和
#     1 + 2 + 3 + 4 + .... + (n-1) + n的和
#     如:
#       请输入: 100
#     打印:
#        5050

n = int(input('请输入整数: '))
s = 0  # 用于累加计数

i = 1
while i <= n:
    s += i  # 累加
    i += 1  # 改变循环变量

print("和是:", s)

# s += 1
# s += 2
# s += 3
# ...
# s += n