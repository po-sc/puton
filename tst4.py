# #1.1
#
# def print_field_names(obj):
#
#     for name in vars(obj):
#         if not name.startswith('_'):
#             print(name)
#
# class MyObject:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self._hidden = "secret"
#
# obj = MyObject(5, 10)
# print_field_names(obj)
#
#
# #1.2
#
# def callbyname(obj, method_name):
#     getattr(obj, method_name)()
#
# class MyClass:
#     def __init__(self, message):
#         self.message = message
#
#     def display_message(self):
#         print(self.message)
#
# my_obj = MyClass("Hello, world!")
# callbyname(my_obj, 'display_message')
#
#
# #1.3
#
# class A:
#     pass
#
# class B(A):
#     pass
#
# # class C(A, B):
# #     pass
#
# class C(B):
#     pass
#
#
#
# #1.4
#
# def get_inheritance(cls):
#     return ' -> '.join(c.__name__ for c in [cls] + list(cls.__mro__[1:]))
#
# chain = get_inheritance(C)
# print(chain)


#2
#2.1

class SimpleHashTableTask1:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def __setitem__(self, key, value):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

    def __getitem__(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f'Key {key} not found')

    def __len__(self):
        return self.size

# Создание экземпляра хэш-таблицы
ht = SimpleHashTableTask1()

# Добавление элементов
ht["apple"] = 150
ht["banana"] = 300
ht["orange"] = 200
ht["kiwi"] = 450

# Получение и вывод значения по ключу

# Ключ, который хотим проверить
key_to_check = "banana"

# Попытка получения значения по ключу с обработкой исключения, если ключ не найден
try:
    value = ht[key_to_check]
    print(f"Значение по ключу '{key_to_check}':", value)
except KeyError:
    print(f"Ключ '{key_to_check}' не найден в хэш-таблице.")

# Вывод размера хэш-таблицы
print("Количество элементов в хэш-таблице:", len(ht))

print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n"
      "/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")

#2.2

class SimpleHashTableTask1:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def __setitem__(self, key, value):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

    def __getitem__(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f'Key {key} not found')

    def __len__(self):
        return self.size

class SimpleHashTableTask2(SimpleHashTableTask1):
    def __delitem__(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError(f'Key {key} not found')

    def keys(self):
        return [key for key, _ in self.items()]

    def values(self):
        return [value for _, value in self.items()]

    def items(self):
        for bucket in self.buckets:
            for item in bucket:
                yield item

    def __iter__(self):
        return iter(self.keys())

    def __contains__(self, key):
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False

# Создание экземпляра хэш-таблицы
ht2 = SimpleHashTableTask2()

# Добавление элементов
ht2["apple"] = 150
ht2["banana"] = 300
ht2["orange"] = 200

# Вывод значения по ключу
print("Значение для 'apple':", ht2["apple"])

# Вывод всех ключей
print("Все ключи:", list(ht2.keys()))

# Вывод всех значений
print("Все значения:", list(ht2.values()))

# Вывод всех пар ключ-значение
print("Все пары ключ-значение:", list(ht2.items()))

# Проверка наличия ключа
if "banana" in ht2:
    print("'banana' находится в таблице")

# Удаление элемента
del ht2["banana"]
print("После удаления 'banana', ключи:", list(ht2.keys()))

# Попытка доступа к удаленному элементу
try:
    print(ht2["banana"])
except KeyError:
    print("'banana' больше не существует в таблице")


print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n"
      "/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")


#2.3


class SimpleHashTableTask3:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def __setitem__(self, key, value):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

    def __getitem__(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f'Key {key} not found')

    def __delitem__(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError(f'Key {key} not found')

    def keys(self):
        for bucket in self.buckets:
            for key, _ in bucket:
                yield key

    def values(self):
        for bucket in self.buckets:
            for _, value in bucket:
                yield value

    def items(self):
        for bucket in self.buckets:
            for item in bucket:
                yield item

    def __iter__(self):
        return iter(self.keys())

    def __contains__(self, key):
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False

    def __len__(self):
        return self.size

# Создание экземпляра хэш-таблицы
ht3 = SimpleHashTableTask3()

# Добавление элементов
ht3["apple"] = 150
ht3["banana"] = 300
ht3["orange"] = 200

# Вывод всех ключей
print("Ключи:")
for key in ht3:
    print(key)

# Вывод всех значений
print("Значения:")
for value in ht3.values():
    print(value)

# Вывод всех пар ключ-значение
print("Пары ключ-значение:")
for key, value in ht3.items():
    print(f"{key}: {value}")

# Пример вложенного цикла
print("Вложенные циклы (каждый ключ с каждым значением):")
for key in ht3:
    for value in ht3.values():
        print(f"Ключ {key}, Значение {value}")




