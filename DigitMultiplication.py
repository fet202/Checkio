def checkio(number: int) -> int:
    res = 1
    for each in str(number):
        n = int(each)
        if n !=0:
            res = res * n

    print(res)






checkio(123405)