import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        bmi = np.array(weight) / (np.array(height) ** 2)
        return bmi
    except:
        raise AssertionError("problème")
    

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return list(np.array(bmi) > limit)