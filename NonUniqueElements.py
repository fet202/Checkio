#Your optional code here
#You can import some modules or create additional functions


def checkio(data: list) -> list:
    new_data = []
    for el in data:
       if data.count(el)>1:
           new_data.append(el)
    print(new_data)



    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.

    #replace this for solution
    #return data

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list



checkio([1, 2, 3, 1, 3])