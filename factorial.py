

def fact(num: int) -> int:
    res :int = 1
    for n in range(1, num+1):
        res = res * n
    return res

print(fact(5))