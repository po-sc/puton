# #1.1
# import math
# def distance(x1, y1, x2, y2):
#
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#
# if __name__ == "__main__":
#     import doctest
#
#     result = doctest.testmod()
#     print(result)
#
#     if result.failed == 0:
#         print("Все тесты пройдены успешно!")
#     else:
#         print(f"Количество ошибок: {result.failed}")
#
# #1.2
# import random
#
#
# def bucketsort(arr, k):
#     counts = [0] * k
#     for x in arr:
#         counts[x] += 1
#
#     sorted_arr = []
#     for i in range(k):
#         sorted_arr.extend([i] * counts[i])
#
#     return sorted_arr
#
#
# def test_bucketsort():
#     assert bucketsort([3, 2, 1, 0], 4) == [0, 1, 2, 3]
#     assert bucketsort([1, 0, 1, 0], 2) == [0, 0, 1, 1]
#     assert bucketsort([], 4) == []
#     assert bucketsort([1, 2, 3, 1], 4) == [1, 1, 2, 3]
#
#     for _ in range(10):
#         arr = [random.randint(0, 9) for _ in range(20)]
#         assert bucketsort(arr, 10) == sorted(arr)
#
#
# if __name__ == "__main__":
#     test_bucketsort()
#     print("All tests passed!")
#
#
# #1.3
# class raises:
#     def __init__(self, exception):
#         self.exception = exception
#
#     def __enter__(self):
#         pass
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type is None:
#             raise AssertionError(f"Expected exception {self.exception} was not raised")
#         if not issubclass(exc_type, self.exception):
#             raise AssertionError(f"Expected exception {self.exception}, but {exc_type} was raised")
#         return True
#
# class MealyError(Exception):
#     pass
#
# def faulty_function():
#     raise MealyError("An error occurred")
#
# if __name__ == "__main__":
#     try:
#         with raises(MealyError):
#             faulty_function()
#         print("Test passed!")
#     except AssertionError as e:
#         print(f"Test failed: {e}")
#
#
#



#3.1

import inspect
from mutator import mutate_code
import ast

def make_mutants(func, size):
    mutant = src = ast.unparse(ast.parse(inspect.getsource(func)))
    mutants = [src]
    while len(mutants) < size + 1:
        while mutant in mutants:
            mutant = mutate_code(src)
        mutants.append(mutant)
    return mutants[1:]

def mut_test(func, test, size=20):
    survived = []
    mutants = make_mutants(func, size)
    for mutant in mutants:
        try:
            exec(mutant, globals())
            test()
            survived.append(mutant)
        except:
            pass
    return survived

#3.2

import inspect
from mutator import mutate_code
import ast

def make_mutants(func, size):
    mutant = src = ast.unparse(ast.parse(inspect.getsource(func)))
    mutants = [src]
    while len(mutants) < size + 1:
        while mutant in mutants:
            mutant = mutate_code(src)
        mutants.append(mutant)
    return mutants[1:]

def mut_test(func, test, size=20):
    survived = []
    mutants = make_mutants(func, size)
    for mutant in mutants:
        try:
            exec(mutant, globals())
            test()
            survived.append(mutant)
        except:
            pass
    return survived



#4.1
import deal


@deal.pre(lambda a, b: b != 0)
@deal.ensure(lambda a, b, result: abs(result * b - a) < 1e-6)
def divide(a, b):
    return a / b


#4.2


import deal


class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self._invariant()

    @deal.inv(lambda self: self.balance >= 0)
    def _invariant(self):
        pass

    @deal.pre(lambda self, amount: amount > 0)
    @deal.post(lambda self, amount, result: result == self.balance - amount)
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    @deal.pre(lambda self, amount: amount > 0)
    @deal.post(lambda self, amount, result: result == self.balance + amount)
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    @deal.ensure(lambda self, amount, result: result >= amount)
    def get_balance(self):
        return self.balance


#4.3

import deal


@deal.has()
class MyClass:
    def __init__(self, x):
        self.x = x

    @deal.ensure(lambda self, result: result > 0)
    def double(self):
        return self.x * 2