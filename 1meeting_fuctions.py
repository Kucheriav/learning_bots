def my_decorator(my_func):

    def wrapper(arg1, arg2):
        print('hello')
        my_func(arg1, arg2)
        print('bye')

    return wrapper

@my_decorator
def translation(x, n):
    ost = list()
    while x != 0:
        a = x % n
        ost.append(a)
        x = x // n
    ost.reverse()
    print(ost)
    return ost



translation(42, 2)





