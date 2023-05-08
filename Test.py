class Test :
    def __init__(self,empid,name):
        self.empid = empid
        self.name = name

    def func1(self):
        return f'I am in normal function'

    @classmethod
    def func2(cls):
        return f'I am in classmethod'

    @staticmethod
    def func3():
        return 'I am in staticmethod'


obj = Test('123','Ravi')
print(obj.func1())
print(Test.func2())
print(Test.func3())