import time
from collections import Counter


def pain(func):
    def wrapper():
        print(" </' ' ' ' ' '\ >")
        func()
        print(" <\ ______ />")

    return wrapper


def ingredients(func):
    def wrapper():
        print("#tomates#")
        func()
        print("-salade-")

    return wrapper


@pain
@ingredients
def sandwich(nourriture='--jambon--'):
    print(nourriture)


@ingredients
@pain
def sandwich_zarb(nourriture="--jambon--"):
    print(nourriture)


def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        timed = str(int(end - start))
        print("the function takes : " + timed + "s to execute")

    return wrapper


def counter(func):
    def wrapper():
        func()
        wrapper.calls += 1
        print("the function has been called "+str(wrapper.calls)+" times")
    wrapper.calls = 0
    return wrapper


@counter
@timer
@pain
@ingredients
def sandwich(nourriture='--jambon--'):
    time.sleep(2)
    print(nourriture)


sandwich()
sandwich()
