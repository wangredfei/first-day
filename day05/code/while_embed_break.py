
# 此示例示意while语句的嵌套
# 打印 1 ~ 20 的整数，打印在一行内
#    1 2 3 4 5 6 7  ..... 20
# 问题:
#    打印以上的十行?

j = 1
while j <= 10:
    # print("此行语句会执行十次")
    i = 1
    while i <= 20:
        print(i, end=' ')
        if i == 10:
            break
        i += 1
    print()  # 换行

    j += 1





