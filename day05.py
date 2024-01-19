# Open closed principle

def test(f):
    """
    decorator,
    :param f: function
    :return: closure function
    """
    def test_in(*args,**kwargs):
        print('start')
        f()
        # result = f(*args,**kwargs)
        print('end')

        # return result
    return test_in # closure니까 ()dksqnxdla


@test
def greeting():
    print("Hello")

greeting()