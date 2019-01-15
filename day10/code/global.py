# global.py


# 此示例示意global语句的语法和用法
v = 100
def f1():
    global v  # global声明v为全局变量
    v = 200  # 想让此赋值语句去修改全局变量v

f1()
print('v=', v)  # 200