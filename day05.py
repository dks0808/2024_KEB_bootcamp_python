def squares(*n)->list:
    """

    :param n:
    :return:
    """
    return [i**2 for i in n]


    # return n**2

def rum_function(f, *number)-> list:
    return f(*number)

print(squares(7,5,2))
print(rum_function(squares,9,10))
#
#
