# ооп - Наследование

#class Transport:
 #   def__init__(self,model,year,color):
    #self.model = modul
    #self.year = year
    #self.color = color
    
   
    #def info(self) :
     #   print(f'Брен транспорта - {self.model},Год выпуска - {self.year,Цвет - {self.color}}') 

#class Car (Transport):#Дочерний класс
    #def__init__(self,model,year,color,penalties = 2000):
        # Transpor.__init__(self,model,year,color # первый # способ (Напрямую к класс)
    #super().__init__(self,model,year,color) #Втарой спасоб(с помощю метода super())
    #self.penalties = penalties

    #lexus = Car("1x 300,2003,(white)")
   # lexus.info()
#print(lexus.penaltinemees)



class Animals:
    def _init_(self, name, bread, age):
        self.name = name 
        self.bread = bread
        self.age = age
        ['kl;']
    def speak(self):
        pass
    
class Dog(Animals):
    def _init_(self, name, bread, age):
        super()._init_(name, bread, age)
        
    def speak(self):
        print(f"woof - {self.name} - {self.bread} - {self.age}")
        
class Cat(Animals):
    def _init_(self, name, bread, age):
        super()._init_(name, bread, age)
        
    def speak(self):
        print(f"Meow - {self.name} - {self.bread} - {self.age}")

class Cow(Animals):
    def _init_(self, name, bread, age, milk):
        super()._init_(name, bread, age)
        self.milk = milk
        
    def speak(self):
        print(f"moo - {self.name} - {self.bread} - {self.age} - {self.milk}")
        
dog = Dog("Ak-tosh", "Alabai", 2)
cat = Cat("Muska", "swinks", 1)
cow = Cow("Tamara", "Angust", 6, 'white')
dog.speak()
cat.speak()
cow.speak()
