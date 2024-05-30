#1
#1.1


# def deriv(f, h=1e-5):
#     def derivative_at(x):
#         return (f(x + h) - f(x)) / h
#     return derivative_at
#
# # Пример использования
# if __name__ == "__main__":
#     f = lambda x: x ** 3
#     df = deriv(f)
#     result = df(5)
#     print(result)  # Ожидаемый вывод: приближенное значение производной в точке 5
#


#1.2


# def person(**attributes):
#     def accessor(key):
#         return attributes[key]
#     def replacer(key, value):
#         new_attributes = attributes.copy()
#         new_attributes[key] = value
#         return person(**new_attributes)
#     return accessor, replacer
#
# def get(p, key):
#     accessor, _ = p
#     return accessor(key)
#
# def replace(p, key, value):
#     _, replacer = p
#     return replacer(key, value)
#
# # Пример использования
# if __name__ == "__main__":
#     p1 = person(name='Иван', age=20)
#     p2 = replace(replace(p1, 'name', 'Алексей'), 'age', 21)
#     print(get(p1, 'name'), get(p1, 'age'))  # Ожидаемый вывод: ('Иван', 20)
#     print(get(p2, 'name'), get(p2, 'age'))  # Ожидаемый вывод: ('Алексей', 21)


#1.3

#
# fact = (lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda f: lambda n: 1 if n == 0 else n * f(n - 1))
#
# # Пример использования
# print(fact(5))  # Ожидаемый вывод: 120
#



#1.4

#
# import random
#
# def io(*funcs):
#     def decorator(f):
#         def wrapped():
#             inputs = [func() for func in funcs[:-1]]
#             result = f(*inputs)
#             funcs[-1](result)
#             return result
#         return wrapped
#     return decorator
#
# # Пример использования
# @io(input, input, input, print)
# def f1(x, y, z):
#     return x + y + z
#
# @io(lambda: random.random(), lambda: random.random(), print)
# def f2(x, y):
#     return x * y
#
# # Примеры вызова
# if __name__ == "__main__":
#     print("Calling f1:")
#     f1()  # Ожидается ввод трех строк и вывод их конкатенации
#     print("Calling f2:")
#     f2()  # Ожидается вывод произведения двух случайных чисел



#1.5

#
# def collect(cls):
#     cls._objects = []
#
#     original_init = cls.__init__
#
#     def new_init(self, *args, **kwargs):
#         original_init(self, *args, **kwargs)
#         cls._objects.append(self)
#
#     cls.__init__ = new_init
#
#     @classmethod
#     def get_objects(cls):
#         return cls._objects
#
#     cls.get_objects = get_objects
#
#     return cls
#
# @collect
# class C1:
#     def __init__(self):
#         pass
#
# # Пример использования
# a = C1()
# b = C1()
# c = C1()
#
# print(C1.get_objects())  # Ожидаемый вывод: список объектов класса C1




#2
#2.1

#
# def pair(head, tail):
#     return lambda f: f(head, tail)
#
# def head(lst):
#     return lst(lambda h, t: h)
#
# def tail(lst):
#     return lst(lambda h, t: t)
#
# # Пример использования
# lst = pair(1, pair(2, pair(3, None)))
#
# print(head(lst))  # Ожидаемый вывод: 1
# print(head(tail(lst)))  # Ожидаемый вывод: 2
# print(head(tail(tail(lst))))  # Ожидаемый вывод: 3


#2.2

#
# def pair(head, tail):
#     return lambda f: f(head, tail)
#
# def head(lst):
#     return lst(lambda h, t: h)
#
# def tail(lst):
#     return lst(lambda h, t: t)
#
# def make_list(*args):
#     if not args:
#         return None
#     lst = None
#     for element in reversed(args):
#         lst = pair(element, lst)
#     return lst
#
# # Пример использования
# lst = make_list(1, 2, 3)
# print(head(lst))  # Ожидаемый вывод: 1
# print(head(tail(lst)))  # Ожидаемый вывод: 2
# print(head(tail(tail(lst))))  # Ожидаемый вывод: 3



#2.3
#
# def pair(head, tail):
#     return lambda f: f(head, tail)
#
# def head(lst):
#     return lst(lambda h, t: h)
#
# def tail(lst):
#     return lst(lambda h, t: t)
#
# def make_list(*args):
#     if not args:
#         return None
#     lst = None
#     for element in reversed(args):
#         lst = pair(element, lst)
#     return lst
#
# def list_to_string(lst):
#     if lst is None:
#         return ""
#     else:
#         return str(head(lst)) + (" " + list_to_string(tail(lst)) if tail(lst) is not None else "")
#
# # Пример использования
# if __name__ == "__main__":
#     lst = make_list(1, 2, 3)
#     print(head(lst))  # Ожидаемый вывод: 1
#     print(head(tail(lst)))  # Ожидаемый вывод: 2
#     print(head(tail(tail(lst))))  # Ожидаемый вывод: 3
#
#     print(list_to_string(lst))  # Ожидаемый вывод: "1 2 3"
#




#2.4

#
# def pair(head, tail):
#     return lambda f: f(head, tail)
#
# def head(lst):
#     return lst(lambda h, t: h)
#
# def tail(lst):
#     return lst(lambda h, t: t)
#
# def make_list(*args):
#     if not args:
#         return None
#     lst = None
#     for element in reversed(args):
#         lst = pair(element, lst)
#     return lst
#
# def list_range(low, high):
#     if low > high:
#         return None
#     else:
#         return pair(low, list_range(low + 1, high))
#
# # Пример использования
# lst = list_range(1, 5)
# print(list_to_string(lst))  # Ожидаемый вывод: "1 2 3 4 5"
#




#2.5

#
# def pair(head, tail):
#     return lambda f: f(head, tail)
#
# def head(lst):
#     return lst(lambda h, t: h)
#
# def tail(lst):
#     return lst(lambda h, t: t)
#
# def make_list(*args):
#     if not args:
#         return None
#     lst = None
#     for element in reversed(args):
#         lst = pair(element, lst)
#     return lst
#
# def list_to_string(lst):
#     if lst is None:
#         return ""
#     else:
#         return str(head(lst)) + (" " + list_to_string(tail(lst)) if tail(lst) is not None else "")
#
# def list_range(low, high):
#     if low > high:
#         return None
#     else:
#         return pair(low, list_range(low + 1, high))
#
# def foldl(func, lst, acc):
#     if lst is None:
#         return acc
#     else:
#         return foldl(func, tail(lst), func(acc, head(lst)))
#
# # Пример использования
# if __name__ == "__main__":
#     lst = list_range(1, 5)
#     print(list_to_string(lst))  # Ожидаемый вывод: "1 2 3 4 5"
#
#     result = foldl(lambda acc, x: acc + x, lst, 0)
#     print(result)  # Ожидаемый вывод: 15




#2.6


def pair(head, tail):
    return lambda f: f(head, tail)


def head(lst):
    return lst(lambda h, t: h)


def tail(lst):
    return lst(lambda h, t: t)


def make_list(*args):
    if not args:
        return None
    lst = None
    for element in reversed(args):
        lst = pair(element, lst)
    return lst


def list_to_string(lst):
    if lst is None:
        return ""
    else:
        return str(head(lst)) + (" " + list_to_string(tail(lst)) if tail(lst) is not None else "")


def list_range(low, high):
    if low > high:
        return None
    else:
        return pair(low, list_range(low + 1, high))


def foldl(func, lst, acc):
    if lst is None:
        return acc
    else:
        return foldl(func, tail(lst), func(acc, head(lst)))


def list_sum(lst):
    return foldl(lambda acc, x: acc + x, lst, 0)


# Пример использования
if __name__ == "__main__":
    lst = list_range(1, 5)
    print(list_to_string(lst))  # Ожидаемый вывод: "1 2 3 4 5"

    result = list_sum(lst)
    print(result)  # Ожидаемый вывод: 15
