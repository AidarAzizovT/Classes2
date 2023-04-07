class Test:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return 'Class with a parametr ' + self.a

tst = Test('Aidar')
print(tst)



