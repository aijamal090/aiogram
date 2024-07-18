class Car: 
    def _init_(self, model, year, color, volume):
        self.model = model
        self.year = year
        self.color = color 
        self.volume = volume
    
    def info(self):
        print(f"Модель машины: {self.model}, Год выпуска: {self.year}, Цвет: {self.color}, Объем: {self.volume}")
        
bmw = Car('BMW', 2016, 'black', '2.5')
lexus = Car('Lexus', '2023', 'White', '4')
bmw.info()
lexus.info()

class Calculator:
    def _init_(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self):
        print(f'Ответ: {self.num1 + self.num2}')
        
    def minus(self):
        print(f'Ответ: {self.num1 - self.num2}')
        
    def multiplication(self):
        print(f'Ответ: {self.num1 * self.num2}')
        
    def division(self):
        print(f'Ответ: {self.num1 / self.num2}')
        
num1 = float(input("Введите первое число: "))
operator = input("+, -, *, /: ")
num2 = float(input("Введите вторе число: "))

calc = Calculator(num1, num2)

if operator == '+':
    calc.plus()
elif operator == '-':
    calc.minus()
elif operator == '*':
    calc.multiplication()
elif operator == '/':
    calc.division()
else:
    print("Неверный оператор")
# ООП - Объектно ориентированние программирование 

# class Person: # Класс чертеж
#     def _init(self, name, lastname, age, nationalety): # __init_ : конструктор, self: сам объект 
#         self.name = name 
#         self.lastname = lastname
#         self.age = age
#         self.nationalety = nationalety
        
#     def info(self):
#         print(f"Имя: {self.name}, Фамилия: {self.lastname}, Возраст: {self.age}, Нация: {self.nationalety}")
        
# person = Person("Элиза", "Эркинбек кызы", 18, "Кыргыз")
# person.info()

# class Car: 
#     def _init_(self, model, year, color, volume):
#         self.model = model
#         self.year = year
#         self.color = color 
#         self.volume = volume
    
#     def info(self):
#         print(f"Мо…