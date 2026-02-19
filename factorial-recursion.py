
res = 1

def fact(a: int) -> None:
    if(a==0):
        return
    global res
    res = res * a
    a = a - 1
    fact(a)

fact(5)

    
print(res)