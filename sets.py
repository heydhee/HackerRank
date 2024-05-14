def average(array):
    my_set = set()

    for element in array:
        my_set.add(element)


    length = len(my_set)
    summ = sum(my_set)
    avg = round(summ/length,3)
    return print(avg)

average([161,182,161,154,176,170,167,171,170,174])
