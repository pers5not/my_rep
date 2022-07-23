#!/usr/bin/env python3

def firs_test():
    print("Test - 1")


def second_test():
    print("Test - 2")


firs_test()
second_test()


# Принцип работы декоратора
def simple_decor(fn):
    def wrapper():
        print("Run Test.....")
        fn()
        print("Stop Test.....")
    return wrapper()


simple_decor(firs_test)
simple_decor(second_test)


# Декоратор функции
@simple_decor
def first_test():
    print("Test function 1")


def param_transfer(fn):
    def wrapper(arg):
        print("Run function: " + str(fn.__name__) +
              "(), with param: " + str(arg))
        fn(arg)
    return wrapper


@param_transfer
def print_sqrt(num):
    print(num**0.5)


print_sqrt(4)


def method_decor(fn):
    def wrapper(self):
        print("Run method: " + str(fn.__name__))
        fn(self)
    return wrapper


class Vector():
    def __init__(self, px=0, py=0):
        self.px = px
        self.py = py

    @method_decor
    def norm(self):
        print((self.px**2 + self.py**2)**0.5)


vc = Vector(px=10, py=5)
vc.norm()


def decor_with_return(fn):
    def wrapper(*args, **kwargs):
        print("Run method: " + str(fn.__name__))
        return fn(*args, **kwargs)
    return wrapper


@decor_with_return
def calc_sqrt(val):
    return val**0.5


tmp = calc_sqrt(16)
print(tmp)