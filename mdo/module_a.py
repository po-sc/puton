import module_b

def function_a():
    print("Function A from module A")

# Попытка использовать функцию из module_b, которая еще не была полностью инициализирована
module_b.function_b()
