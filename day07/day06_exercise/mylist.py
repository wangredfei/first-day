# 2.生成一个列表,求 x 的平方+1的列表,跳过结果能被5整除
# 　　　的数, (注: 0 <= x <= 100)

L = [x**2+1 for x in range(0, 101)
        if (x**2+1) % 5 != 0]

print(L)