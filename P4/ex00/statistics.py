class functions():
    @classmethod
    def mean(*args):
        i = 0
        liste = list(args[1])
        y = len(liste)
        for x in liste:
            x = int(x)
            i = i + x
        print("mean :", i / y)

    @classmethod
    def median(*args):
        liste = list(args[1])
        liste.sort()
        if len(liste) % 2:
            y = (len(liste) - 1) / 2
            print("median :", liste[int(y)])
        else:
            index = (len(liste) - 1) // 2
            y = (liste[index] + liste[index + 1]) / 2
            print("median :", y)

    @classmethod
    def quartile(*args):
        liste = list(args[1])
        liste.sort()
        y = (1 / 4) * (len(liste) - 1)
        x = (3 / 4) * (len(liste) - 1)
        quartileList = [liste[int(y)], liste[int(x)]]
        print("quartile :", quartileList)
    
    @classmethod
    def std(*args):
        values = list(args[1])
        # the lenth of the value is the total population
        N = len(values)
        #mean is nothing but adding all values and divide by total numbers
        mean = sum(values)/N
        # finding (x-µ)² part- create a list with each value subtracted by mean and squared
        NrSqr = [(x-mean)**2 for x in values]
        # finding Σ portion which is nothing but all values sum
        Sigma = sum(NrSqr)
        #Square root to be taken for the sum
        Nr = Sigma ** (1/2)
        #taking square root to N for denominator
        Dr = N ** (1/2)
        #Find out standard deviation
        sd = Nr/Dr
        #Get output
        print("std :", sd)
    
    @classmethod
    def var():
        pass


dict = {
    "mean" : functions.mean,
    "median" : functions.median,
    "quartile" : functions.quartile,
    "std" : functions.std,
    # "var" : functions.var
}


def ft_statistics(*args: any, **kwargs: any) -> None:
    for x in args:
        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("args must be int or float")
    for x in kwargs:
        if not isinstance(x, str):
            raise TypeError("kwargs must be str")
    print("kwargs :", kwargs)
    for key, value in kwargs.items():
        dict[value](args)