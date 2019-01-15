# override.py

# 此示例示意覆盖的语法
class A:
    def work(self):
        print("A.work被调用!")

class B(A):
    def work(self):
        '''此方法会覆盖父类中同名的方法'''
        print("B.work被调用")
    pass

b = B()
b.work()  # 请问调用谁?


