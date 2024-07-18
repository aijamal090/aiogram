# Практика
#class Car:
 #   def __init__(self, brend, model, year):
  #      self.brend=brend
   #     self.model=model
    #    self.year=year
#def displey_info(self):
 #   print (f"Марка:{self.brend}.{self.year}")
  

#  car = Car("Tayoto", "Camri", 2023)
   # car. displey_info()


#class ElectricCar(Car):
 #   def __init__(self, brand, model, year, battery_capacity):
  #      super().__init__(brand, model, year)
   #     self.battery_capacity = battery_capacity

    #def display_battery_info(self):
     #   print(f"Емкость батареи: {self.battery_capacity} kWh")
#electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
#electric_car.display_info()
#electric_car.display_battery_info()



#class Car:
 #   def __init__(self, brand, model, year):
  #      self.brand = brand
   #     self.model = model
    #    self.year = year
     #   self.__mileage = 0  
    #def display_info(self):
     #   print(f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}")

    #def set_mileage(self, mileage):
     #   if mileage >= 0:
      #      self.__mileage = mileage
       # print("Пробег не может быть отрицательным")

    #def get_mileage(self):
     #   return self.__mileage


car = Car("Toyota", "Camry", 2020)
car.set_mileage(15000)
print(f"Пробег: {car.get_mileage()} км")


class Animals:
    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

class Dog(Animals):
    def make_sound(self):
        print("Woof")

class Cat(Animals):
    def make_sound(self):
        print("Meow")
       # гитхап
       #библатека
       