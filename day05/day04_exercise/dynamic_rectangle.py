#   5. 输入一个整数n,打印一个宽度和高度都为n个字符的长方形
#     如:
#       请输入: 4
#     打印:
#       ####
#       #  #
#       #  #
#       ####
#     如:
#       请输入: 6
#     打印:
#       ######
#       #    #
#       #    #
#       #    #
#       #    #
#       ######

n = int(input('请输入宽度(高度): '))
# 1. 打印第一行
print("#" * n)

# 2. 打印中间的几行
i = 2  # i 代表当前的行数
while i < n:
    # print("=========")
    print("#" + ' ' * (n - 2) + '#')
    i += 1

# 3. 打印最后一行
if n >= 2:
    print("#" * n)