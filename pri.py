class myclass:
    def __init__(self,var):
        self.var=var

    _a=1
    __b=2

    def _dis(self):
        print(self.var)
        print("did",self.__b)
        print("did", self._a)

    def __chumma(self):
        print("chumma",self.var)
        print("chumma",self.__b)


class myclass2(myclass):
    def __init__(self,var):
        self.var=var

myobj1=myclass(5)

myobj1._dis()


print(dir(myclass))