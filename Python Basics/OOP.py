"""
class Human:
    name = ""
    length = 0
    def info(self):
        print("hallo")

h1= Human()
h1.name="ali"
h1.length=170
print (h1.name)
print(h1.length)
"""
#self = obj
"""
class Human:
    def info (self ,p_name ,p_length ,p_age):
        self.name=p_name
        self.length=p_length
        self.age=p_age
        print("name = " , self.name)
        print("length = " , self.length)
        print("age = " , self.age)

h1=Human()
h2=Human()
h1.info("ali","170","18")
h2.info("ahmed","18","19")
"""
#Constructor
"""
class Myclass:
    def info(self):
        print("info")
    def __init__(self ,name):
        print("__init__")

my1= Myclass("abdo")"""

#instance , class variable , class method
"""
class Myclass:
    @classmethod
    def info(cls):
        print("info")
    s1= 0 
    """
#every thing is object

#inheritance
"""
class A :
     age : int
     def info(self):
         self.age = 18
         print("age = " , self.age)

class B(A):
    def info2(self):
        super().info()

class C(B):
    def info3(self):
        print("hallo")

a1 = C()
a1.info2()"""

#multi inheritance , override

# import , random
"""
from  filename import  classname"""
"""
import random
value= random.uniform(1,8)
print(value)"""

#nested class , class enter mathod

"""
class A:
    x:int 
    def myfun1(self):
        print(self.x)
    class B:
        y:int
        def myfun2(self):
            print(self.y)
            
b= A.B()
"""
#polymorphism

#enum class
from enum import Enum

class Animal(Enum):
    dog = 1
    cat = 2
    lion = 3
print (Animal.dog.name)
print(Animal.dog.value)
for animal in Animal.__members__:
    print(animal)

