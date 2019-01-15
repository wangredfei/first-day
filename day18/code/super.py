# super.py

# 此示例示意用super函数 调用父类的被覆盖方法
class A:
    def work(self):
        print("A.work被调用!")

class B(A):
    def work(self):
        '''此方法会覆盖父类中同名的方法'''
        print("B.work被调用")

    def mywork(self):
        ''''''
        # 1. 调用B 类的work
        self.work()
        # 2. 调用父类的work
        super(B, self).work()
        super().work()  # 无参调用只能用在方法内

b = B()
b.work()  # B.work被调用
super(B, b).work()

b.mywork()





