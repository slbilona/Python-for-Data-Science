def square(x: int | float) -> int | float:
    """
    Returns the square of a number.

    Parameters:
        x (int | float): The number to square.

    Returns:
        int | float: The square of x.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Returns the number raised to the power of itself.

    Parameters:
        x (int | float): The number to raise to its own power.

    Returns:
        int | float: x raised to the power of x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a function that applies the given function to x each time
    it is called.

    Parameters:
        x (int | float): The initial number to calculate.
        function (callable): The function to apply to x.

    Returns:
        function: A function that, when called, applies 'function' to x
        and returns the result.
    """
    count = 0
    try:
        if not isinstance(x, (int, float)):
            raise TypeError("x must be int or float")
        if not callable(function):
            raise TypeError("function must be callable")

        def inner() -> float:
            """
            Applies the outer function to x, updates x, and increments
            the call count.

            Returns:
                float: The updated value of x after applying the function.
            """
            nonlocal x
            nonlocal count
            x = function(x)
            count += 1
            return x
        return inner
    except AssertionError as e:
        print("AssertionError:", e)
        return None
