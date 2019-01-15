# mydeco.py

# 此示例示意装饰器函数的定义方式及装饰器来装饰另一个函数
# 的语法

def mydeco(fn):
    def fx():
        print("++++++++++++++++")
        fn()  # 调用以前的被装饰函数
        print('----------------')
    return fx

@mydeco
def myfunc():
    '''此函数将作为被装饰函数'''
    print("myfunc被调用")

myfunc()
myfunc()
myfunc()
