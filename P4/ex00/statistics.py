class functions():
    @classmethod
    def mean(*args):
        i = 0
        y = 0
        for x in args:
            print("x : ", x)
            # i = i + x
            # y += 1
        # print("mean =", i / y)

    @classmethod
    def median():
        pass

    @classmethod
    def quartile():
        pass
    
    @classmethod
    def std():
        pass
    
    @classmethod
    def var():
        pass


dict = {
    "mean" : functions.mean(),
    # "median" : functions.median(),
    # "quartile" : functions.quartile(),
    # "std" : functions.std(),
    # "var" : functions.var()
}


def ft_statistics(*args: any, **kwargs: any) -> None:
    for x in args:
        if not isinstance(x, int):
            raise TypeError("args must be int")
    for x in kwargs:
        if not isinstance(x, str):
            raise TypeError("kwargs must be str")
    print("kwargs :", kwargs)
    for key, value in kwargs.items():
        dict[value](args)