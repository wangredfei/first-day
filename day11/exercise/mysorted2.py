
names = ['Tom', 'Jerry', 'Spike', 'Tyke']

def myk(x):
    print("type(x)=", type(x), "x=", x)
    return x[::-1]  # 反回反转后的字符作为排序依据

L = sorted(names, key=myk)
print(L)
# 结果: ['Spike', 'Tyke', 'Tom', 'Jerry']