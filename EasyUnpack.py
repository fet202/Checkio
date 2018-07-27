def easy_unpack(elements: tuple) -> tuple:
    res = []
    res.append(elements[0])
    res.append(elements[2])
    res.append(elements[-2])
    print(tuple(res))




easy_unpack((1, 2, 3, 4, 5, 6, 7, 9))