class C():
    def __init__(self):
            print("1")
    def fun(self):
            print("c")

class B(C):
    def __init__(self):
            print("2")

class A(B):
    def __init__(self):
            print("3")
    def fun(self):
            print("a")

a=A()
b=B()
c=C()
a.fun()
b.fun()
c.fun()
