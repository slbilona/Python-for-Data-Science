class calculator:
    def __init__(self, vec):
        self.vec = vec

    def __add__(self, object) -> None:
        myList = []
        x = 0
        for x in self.vec:
            myList.append(x + object)
        self.vec = myList
        print(myList)

    def __mul__(self, object) -> None:
        myList = []
        x = 0
        for x in self.vec:
            myList.append(x * object)
        self.vec = myList
        print(myList)

    def __sub__(self, object) -> None:
        myList = []
        x = 0
        for x in self.vec:
            myList.append(x - object)
        self.vec = myList
        print(myList)

    def __truediv__(self, object) -> None:
        if object == 0:
            raise Exception("impossible de diviser par 0")
        myList = []
        x = 0
        for x in self.vec:
            myList.append(x / object)
        self.vec = myList
        print(myList)
