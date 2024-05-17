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
#
# class SimpleHashTableTask1:
#     def __init__(self, capacity=100):
#         self.capacity = capacity
#         self.size = 0
#         self.buckets = [[] for _ in range(capacity)]
#
#     def _hash(self, key):
#         return hash(key) % self.capacity
#
#     def __setitem__(self, key, value):
#         hash_key = self._hash(key)
#         bucket = self.buckets[hash_key]
#         for i, (k, _) in enumerate(bucket):
#             if k == key:
#                 bucket[i] = (key, value)
#                 return
#         bucket.append((key, value))
#         self.size += 1
#
#     def __getitem__(self, key):
#         hash_key = self._hash(key)
#         bucket = self.buckets[hash_key]
#         for k, v in bucket:
#             if k == key:
#                 return v
#         raise KeyError(f'Key {key} not found')
#
#     def __len__(self):
#         return self.size
#
# # Создание экземпляра хэш-таблицы
# ht = SimpleHashTableTask1()
#
# # Добавление элементов
# ht["apple"] = 150
# ht["banana"] = 300
# ht["orange"] = 200
# ht["kiwi"] = 450
#
# # Получение и вывод значения по ключу
#
# # Ключ, который хотим проверить
# key_to_check = "banana"
#
# # Попытка получения значения по ключу с обработкой исключения, если ключ не найден
# try:
#     value = ht[key_to_check]
#     print(f"Значение по ключу '{key_to_check}':", value)
# except KeyError:
#     print(f"Ключ '{key_to_check}' не найден в хэш-таблице.")
#
# # Вывод размера хэш-таблицы
# print("Количество элементов в хэш-таблице:", len(ht))
#
# print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n"
#       "/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
#
# #2.2
#
# class SimpleHashTableTask1:
#     def __init__(self, capacity=100):
#         self.capacity = capacity
#         self.size = 0
#         self.buckets = [[] for _ in range(capacity)]
#
#     def _hash(self, key):
#         return hash(key) % self.capacity
#
#     def __setitem__(self, key, value):
#         hash_key = self._hash(key)
#         bucket = self.buckets[hash_key]
#         for i, (k, _) in enumerate(bucket):
#             if k == key:
#                 bucket[i] = (key, value)
#                 return
#         bucket.append((key, value))
#         self.size += 1
#
#     def __getitem__(self, key):
#         hash_key = self._hash(key)
#         bucket = self.buckets[hash_key]
#         for k, v in bucket:
#             if k == key:
#                 return v
#         raise KeyError(f'Key {key} not found')
#
#     def __len__(self):
#         return self.size
#
# class SimpleHashTableTask2(SimpleHashTableTask1):
#     def __delitem__(self, key):
#         hash_key = self._hash(key)
#         bucket = self.buckets[hash_key]
#         for i, (k, _) in enumerate(bucket):
#             if k == key:
#                 del bucket[i]
#                 self.size -= 1
#                 return
#         raise KeyError(f'Key {key} not found')
#
#     def keys(self):
#         return [key for key, _ in self.items()]
#
#     def values(self):
#         return [value for _, value in self.items()]
#
#     def items(self):
#         for bucket in self.buckets:
#             for item in bucket:
#                 yield item
#
#     def __iter__(self):
#         return iter(self.keys())
#
#     def __contains__(self, key):
#         try:
#             self.__getitem__(key)
#             return True
#         except KeyError:
#             return False
#
# # Создание экземпляра хэш-таблицы
# ht2 = SimpleHashTableTask2()
#
# # Добавление элементов
# ht2["apple"] = 150
# ht2["banana"] = 300
# ht2["orange"] = 200
# ht2["kiwi"] = 450
#
#
# # Вывод значения по ключу
# print("Значение для 'apple':", ht2["apple"])
#
# # Вывод всех ключей
# print("Все ключи:", list(ht2.keys()))
#
# # Вывод всех значений
# print("Все значения:", list(ht2.values()))
#
# # Вывод всех пар ключ-значение
# print("Все пары ключ-значение:", list(ht2.items()))
#
# # Проверка наличия ключа
# if "banana" in ht2:
#     print("'banana' находится в таблице")
#
# # Удаление элемента
# del ht2["banana"]
# print("После удаления 'banana', ключи:", list(ht2.keys()))
#
# # Попытка доступа к удаленному элементу
# try:
#     print(ht2["banana"])
# except KeyError:
#     print("'banana' больше не существует в таблице")
#
#
# print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n"
#       "/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
#
#
# #2.3
#
#
# class SimpleHashTableTask3:
#     def __init__(self, capacity=100):
#         self.capacity = capacity
#         self.size = 0
#         self.buckets = [[] for _ in range(capacity)]
#
#     def _hash(self, key):
#         return hash(key) % self.capacity
#
#     def __setitem__(self, key, value):
#         hash_key = self._hash(key)
#         bucket = self.buckets[hash_key]
#         for i, (k, _) in enumerate(bucket):
#             if k == key:
#                 bucket[i] = (key, value)
#                 return
#         bucket.append((key, value))
#         self.size += 1
#
#     def __getitem__(self, key):
#         hash_key = self._hash(key)
#         bucket = self.buckets[hash_key]
#         for k, v in bucket:
#             if k == key:
#                 return v
#         raise KeyError(f'Key {key} not found')
#
#     def __delitem__(self, key):
#         hash_key = self._hash(key)
#         bucket = self.buckets[hash_key]
#         for i, (k, _) in enumerate(bucket):
#             if k == key:
#                 del bucket[i]
#                 self.size -= 1
#                 return
#         raise KeyError(f'Key {key} not found')
#
#     def keys(self):
#         for bucket in self.buckets:
#             for key, _ in bucket:
#                 yield key
#
#     def values(self):
#         for bucket in self.buckets:
#             for _, value in bucket:
#                 yield value
#
#     def items(self):
#         for bucket in self.buckets:
#             for item in bucket:
#                 yield item
#
#     def __iter__(self):
#         return iter(self.keys())
#
#     def __contains__(self, key):
#         try:
#             self.__getitem__(key)
#             return True
#         except KeyError:
#             return False
#
#     def __len__(self):
#         return self.size
#
# # Создание экземпляра хэш-таблицы
# ht3 = SimpleHashTableTask3()
#
# # Добавление элементов
# ht3["apple"] = 150
# ht3["banana"] = 300
# ht3["orange"] = 200
# ht3["kiwi"] = 450
#
#
# # Вывод всех ключей
# print("Ключи:")
# for key in ht3:
#     print(key)
#
# # Вывод всех значений
# print("Значения:")
# for value in ht3.values():
#     print(value)
#
# # Вывод всех пар ключ-значение
# print("Пары ключ-значение:")
# for key, value in ht3.items():
#     print(f"{key}: {value}")
#
# # Пример вложенного цикла
# print("Вложенные циклы (каждый ключ с каждым значением):")
# for key in ht3:
#     for value in ht3.values():
#         print(f"Ключ {key}, Значение {value}")
#
#
#
# print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n"
#       "/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
# print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n"
#       "/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
#3
#3.1
#
# class ExprNode:
#     """ Базовый класс для всех узлов выражения. """
#
#     def print(self):
#         pass
#
#
# class Num(ExprNode):
#     def __init__(self, value):
#         self.value = value
#
#     def print(self):
#         return str(self.value)
#
#
# class Add(ExprNode):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#
#     def print(self):
#         return f"({self.left.print()} + {self.right.print()})"
#
#
# class Mul(ExprNode):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#
#     def print(self):
#         return f"({self.left.print()} * {self.right.print()})"
#
#
# # Создание и использование дерева выражений
# ast = Add(Num(7), Mul(Num(3), Num(2)))
# print(ast.print())  # Выводит: (7 + (3 * 2))
#
#
#
# print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n"
#       "/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
#3.2
#
# class ExprNode:
#     """ Базовый класс для всех узлов выражения. """
#     def accept(self, visitor):
#         method_name = 'visit_' + type(self).__name__
#         visitor_method = getattr(visitor, method_name, self.generic_visit)
#         return visitor_method(self)
#
#     def generic_visit(self, visitor):
#         raise Exception('No visit_{} method'.format(type(self).__name__))
#
# class Num(ExprNode):
#     def __init__(self, value):
#         self.value = value
#
# class Add(ExprNode):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#
# class Mul(ExprNode):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#
# class PrintVisitor:
#     def visit(self, node):
#         return node.accept(self)
#
#     def visit_Num(self, node):
#         return str(node.value)
#
#     def visit_Add(self, node):
#         return f"({self.visit(node.left)} + {self.visit(node.right)})"
#
#     def visit_Mul(self, node):
#         return f"({self.visit(node.left)} * {self.visit(node.right)})"
#
# # Создание и использование дерева выражений
# ast = Add(Num(7), Mul(Num(3), Num(2)))
# pv = PrintVisitor()
# output = pv.visit(ast)
# print(output)  # Выводит: (7 + (3 * 2))


#
# #3.3
#
# class ExprNode:
#
#     def accept(self, visitor):
#         pass
#
# class Num(ExprNode):
#     def __init__(self, value):
#         self.value = value
#
#     def accept(self, visitor):
#         return visitor.visit_num(self)
#
# class Add(ExprNode):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#
#     def accept(self, visitor):
#         return visitor.visit_add(self)
#
# class Mul(ExprNode):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#
#     def accept(self, visitor):
#         return visitor.visit_mul(self)
#
# class PrintVisitor:
#     def visit(self, node):
#         return node.accept(self)
#
#     def visit_num(self, num):
#         return str(num.value)
#
#     def visit_add(self, add):
#         return f"({self.visit(add.left)} + {self.visit(add.right)})"
#
#     def visit_mul(self, mul):
#         return f"({self.visit(mul.left)} * {self.visit(mul.right)})"
#
# class CalcVisitor:
#     def visit(self, node):
#         return node.accept(self)
#
#     def visit_num(self, num):
#         return num.value
#
#     def visit_add(self, add):
#         return self.visit(add.left) + self.visit(add.right)
#
#     def visit_mul(self, mul):
#         return self.visit(mul.left) * self.visit(mul.right)
#
# class StackVisitor:
#     def __init__(self):
#         self.instructions = []
#
#     def visit(self, node):
#         node.accept(self)
#         return "\n".join(self.instructions)
#
#     def visit_num(self, num):
#         self.instructions.append(f"PUSH {num.value}")
#
#     def visit_add(self, add):
#         self.visit(add.left)
#         self.visit(add.right)
#         self.instructions.append("ADD")
#
#     def visit_mul(self, mul):
#         self.visit(mul.left)
#         self.visit(mul.right)
#         self.instructions.append("MUL")
#
# # Пример использования
# ast = Add(Num(7), Mul(Num(3), Num(2)))
#
# pv = PrintVisitor()
# print(pv.visit(ast))  # Выводит: (7 + (3 * 2))
#
# cv = CalcVisitor()
# print(cv.visit(ast))  # Выводит: 13
#
# sv = StackVisitor()
# print(sv.visit(ast))
#
#
#
# #3.4
# class ExprNode:
#     def accept(self, visitor):
#         pass
#
# class Num(ExprNode):
#     def __init__(self, value):
#         self.value = value
#
#     def accept(self, visitor):
#         return visitor.visit_num(self)
#
# class Add(ExprNode):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#
#     def accept(self, visitor):
#         return visitor.visit_add(self)
#
# class Mul(ExprNode):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#
#     def accept(self, visitor):
#         return visitor.visit_mul(self)
#
# class StackVisitor:
#     def __init__(self):
#         self.instructions = []
#
#     def visit(self, node):
#         node.accept(self)
#         return "\n".join(self.instructions)
#
#     def visit_num(self, num):
#         self.instructions.append(f"PUSH {num.value}")
#
#     def visit_add(self, add):
#         self.visit(add.left)
#         self.visit(add.right)
#         self.instructions.append("ADD")
#
#     def visit_mul(self, mul):
#         self.visit(mul.left)
#         self.visit(mul.right)
#         self.instructions.append("MUL")
#
# # Пример использования
# ast = Add(Num(7), Mul(Num(3), Num(2)))
#
# sv = StackVisitor()
# print(sv.visit(ast))
#
#
#
#
# #4
# #4.1
#
# class HTML:
#     def __init__(self):
#         self.code = ""
#         self.indentation_level = 0
#
#     def _add_code(self, line):
#         self.code += ' ' * self.indentation_level + line + '\n'
#
#     def _open_tag(self, tag):
#         self._add_code(f"<{tag}>")
#         self.indentation_level += 4
#
#     def _close_tag(self, tag):
#         self.indentation_level -= 4
#         self._add_code(f"</{tag}>")
#
#     def get_code(self):
#         return self.code.strip()
#
#     class Tag:
#         def __init__(self, html, tag):
#             self.html = html
#             self.tag = tag
#
#         def __enter__(self):
#             self.html._open_tag(self.tag)
#             return self
#
#         def __exit__(self, exc_type, exc_val, exc_tb):
#             self.html._close_tag(self.tag)
#
#     def body(self):
#         return self.Tag(self, "body")
#
#     def div(self):
#         return self.Tag(self, "div")
#
#     def p(self, text):
#         self._add_code(f"<p>{text}</p>")
#
# html = HTML()
# with html.body():
#     with html.div():
#         with html.div():
#             html.p('Первая строка.')
#             html.p('Вторая строка.')
#         with html.div():
#             html.p('Третья строка.')
#
# print(html.get_code())



#5
#5.1
class SVG:
    def __init__(self):
        self.elements = []

    def line(self, x1, y1, x2, y2, color='black'):
        line_svg = f'<line x1="{x1:.6f}" y1="{y1:.6f}" x2="{x2:.6f}" y2="{y2:.6f}" stroke="{color}" />\n'
        self.elements.append(line_svg)

    def circle(self, cx, cy, r, color='black'):
        circle_svg = f'<circle cx="{cx:.6f}" cy="{cy:.6f}" r="{r:.6f}" fill="{color}" />\n'
        self.elements.append(circle_svg)

    def save(self, filename, width, height):
        with open(filename, 'w') as f:
            f.write(
                f'<svg version="1.1" width="{width:.6f}" height="{height:.6f}" xmlns="http://www.w3.org/2000/svg">\n')
            for element in self.elements:
                f.write(element)
            f.write('</svg>')


# Пример использования:
svg = SVG()
svg.line(10, 10, 60, 10, color='black')
svg.line(60, 10, 60, 60, color='black')
svg.line(60, 60, 10, 60, color='black')
svg.line(10, 60, 10, 10, color='black')

svg.circle(10, 10, r=5, color='red')
svg.circle(60, 10, r=5, color='red')
svg.circle(60, 60, r=5, color='red')
svg.circle(10, 60, r=5, color='red')

svg.save('pic.svg', 100, 100)