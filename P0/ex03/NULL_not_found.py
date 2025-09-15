def NULL_not_found(obj: any) -> int:
    if obj is None:
        print("Nothing: None <class 'NoneType'>")
        return 0
    elif isinstance(obj, float) and obj != obj:
        print("Cheese: nan <class 'float'>")
        return 0
    elif obj is False:
        print("Fake: False <class 'bool'>")
        return 0
    elif obj == 0 and isinstance(obj, int):
        print("Zero: 0 <class 'int'>")
        return 0
    elif obj == '' and isinstance(obj, str):
        print("Empty: <class 'str'>")
        return 0
    else:
        print("Type not Found")
        return 1
