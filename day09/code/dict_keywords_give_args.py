
# 此示例示意 字典关键字传参
def myfun(a, b, c):
    '''这是一个函数传参的示例'''
    print('a的值是:', a)
    print('b的值是:', b)
    print('c的值是:', c)

d = {'a':100, 'c':300, 'b':200}

# myfun(a=d['a'], c=d['c'], b=d['b'])
myfun(**d)  # 等同于上面一条语句

# myfun(d)  # 出错



