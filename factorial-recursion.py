
# res = 1

# def fact(a: int) -> None:
#     if(a==0):
#         return
#     global res
#     res = res * a
#     a = a - 1
#     fact(a)

# fact(5)

    
# print(res)


def fact(a: int) -> int:
    if a == 1:
        return 1
    return a * fact( a - 1)

print(fact(5))