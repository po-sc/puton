import module_a

def function_b():
    print("Function B from module B")

# Попытка использовать функцию из module_a, которая еще не была полностью инициализирована
module_a.function_a()
