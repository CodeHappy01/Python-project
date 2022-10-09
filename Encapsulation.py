class Protected:
    #Protected Variable
    def __init__(self):
        self._protectedVar = 0
    
    #Private Variable
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

#Protected Variable outcome
obj = Protected()
obj._protectedVar = 123
print(obj._protectedVar)

#Private Variable outcome
obj.getPrivate()
obj.setPrivate(3)
obj.getPrivate()