def NULL_not_found(obj: any) -> int:
    if obj is None:
        print("Nothing:", obj, type(obj))
        return 0
    elif isinstance(obj, float) :#and obj != obj:
        print("Cheese:", obj, type(obj))
        return 0
    elif obj is False:
        print("Fake:", obj, type(obj))
        return 0
    elif obj == 0 and isinstance(obj, int):
        print("Zero:", obj, type(obj))
        return 0
    elif obj == '' and isinstance(obj, str):
        print("Empty:", obj, type(obj))
        return 0
    else:
        print("Type not Found")
        return 1
