def checkio(numbers_array: tuple) -> list:

    absolut_list = []
    for el in numbers_array:
        a =(sorted(numbers_array, key=lambda el: abs(el)))
    return a




checkio((-20, -5, 10, 15))