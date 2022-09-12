# exo6
from functools import lru_cache


@lru_cache(maxsize=None)
def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


# exo 7

a = 3
b = 4
c = 5
l = [a, b, c]
d, e, f = l


# exo 8

def decorate(arg1, arg2, arg3):
    print('Je suis dans la fonction "decorate".')

    def decorated(func):
        print('Je suis dans la fonction "decorated".')

        def wrapper(*args, **kwargs):
            print('Je suis dans la fonction "wrapper".')
            print("Les arguments du décorateurs sont : %s, %s, %s." % (arg1, arg2, arg3))
            print("Pré-traitement.")
            print("Exécution de la fonction %s" % func.__name__)
            response = func(*args, **kwargs)
            print("Post-traitement.")
            return response

        return wrapper

    return decorated


@decorate("Arg 1", "Arg 2", "Arg 3")
def foobar():
    print("Je suis foobar, je vous reçois 5 sur 5")


foobar()


#exo 9

def singleton(classe_definie):
    instances = {}

    # Dictionnaire de nos instances singletons
    def get_instance(*args, **kwargs):
        if classe_definie not in instances:
            # On crée notre premier objet de classe_define
            instances[classe_definie] = classe_definie(*args, **kwargs)
        return instances[classe_definie]

    return get_instance


@singleton
class Test:
    def __init__(self, val):
        self.val = val


a = Test("truc")
b = Test("machin")
print(a.val, id(a))
print(b.val, id(b))
print(a is b)


# exo 10

class P:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if x < 0:
            self._x = 0
        elif x > 1000:
            self._x = 1000
        else:
            self._x = x


class P2:
    def __init__(self, x):
        self.setX(x)
        self._x = None

    def getX(self):
        return self._x

    def setX(self, x):
        if x < 0:
            self._x = 0
        elif x > 1000:
            self._x = 1000
        else:
            self._x = x

    x = property(getX, setX)


print(P.__doc__)
p1 = P(2000)
print(p1.x)
p1.x = 500
print(p1.x)
p1.x = -12
print(p1.x)

print(P2.__doc__)
p1 = P2(2000)
print(p1.x)
p1.x = 500
print(p1.x)
p1.x = -12
print(p1.x)

print(p1.__dict__['_P2_x'])
print(p1._P2_x)
print(p1._x)
