#"""Магические методы - dunder методы"""

# class Work:
#     def __init__(self, position, graphicks):
#         self.positon = position
#         self.graphicks = graphicks
    
#     def info(self):
#         print(f"Позиция - {self.positon}, график - {self.graphicks}")
        
#     def __repr__(self):
#         return f"Позиция - {self.positon}, график - {self.graphicks}"
     
#     def __str__(self):
#         return f"Позиция - {self.positon}, график - {self.graphicks}"
    
#     def __call__(self):
#         print("Это магический метод __call__")
         
        
# work = Work("Бухгалтер", "8/5")
# print(work)
# work.info()
# work()


# def work():
#     print ("hello")

# print(work())

class Math:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
        
    def __str__(self):
        return f'Первое значение: {self.number_1} \nВторое значение: {self.number_2}'
    
    def __add__(self, other): 
        """Создать новый объект как сумму координат 'self' и 'other'."""
        print(f'Результат сложения {self.number_1} и {self.number_2}')
        return Math(self.number_1 + other.number_1, self.number_2)

    def __sub__(self, other): 
        print(f'Результат вычитание {self.number_1} и {self.number_2}')
        return Math(self.number_1 - other.number_1, self.number_2)

    def __mul__(self, other): 
        print(f'Результат умножение {self.number_1} и {self.number_2}')
        return Math(self.number_1 * other.number_1, self.number_2)
    
    def __truediv__(self, other): 
        print(f'Результат деленин {self.number_1} и {self.number_2}')
        return Math(self.number_1 / other.number_1, self.number_2)
    
    
    def __gt__(self, other):
        return self.number_1 > other.number_1
    
    def __lt__(self, other):
        return self.number_1 < other.number_1
    
    def __eq__(self, other):
        return self.number_1 == other.number_1
    
    def __ne__(self, other):
        return self.number_1 != other.number_1
    
    def __ge__(self, other):
        return self.number_1 >= other.number_1
    
    def __le__(self, other):
        return self.number_1 <= other.number_1
    
math_number_1 = int(input("Введите первое число: "))
math_number_2 = int(input("Введите второе число: "))
math = Math(math_number_1, 2)
math_2 = Math(math_number_2, 2)
print(math)
print(math_2)

print("Сложение:", math + math_2)
print("Вычитание:", math - math_2)
print("Умножение:", math * math_2)
print("Деление:", math / math_2)
# print("Целочисленное деление:", math // math_2)


print(math > math_2)
print(math < math_2)
print(math == math_2)
print(math != math_2)
print(math >= math_2)
print(math <= math_2)
class MagicCalculator:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
    
    def __add__(self, other):
        return self.number_1 + other.number_1, self.number_2 + other.number_2
    
    def __sub__(self, other):
        return self.number_1 - other.number_1, self.number_2 - other.number_2
    
    def __mul__(self, other):
        return self.number_1 * other.number_1, self.number_2 * other.number_2
    
    def __truediv__(self, other):
        return self.number_1 / other.number_1, self.number_2 / other.number_2
    
    def __floordiv__(self, other):
        return self.number_1 // other.number_1, self.number_2 // other.number_2
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __lt__(self, other):
        return self.year < other.year

    def __le__(self, other):
        return self.year <= other.year

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __lt__(self, other):
        return self.year < other.year

    def __le__(self, other):
        return self.year <= other.year

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year

    def __str__(self):
        return f"Называние: {self.title}, Автор: {self.author}, год: {self.year}"

