class Person:
    "Person base class"
    wants_to_hack=True
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    
    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age=age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age=age

    @age.deleter
    def age(self):
        del self.__age

    @classmethod
    def wants_to(cls):
        return cls.wants_to_hack

    @classmethod
    def bob_factory(cls):
        return("bob",30)

    @staticmethod
    def static_print():
        print("I am the same!")
    
    def print_name(self):
        print("My name is {}".format(self.name))

    def print_age(self):
        print("My age is {}".format(self.age))

    def birthday(self):
        self.__age+=1

bob=Person("bob",30)
print(bob.age)

bob.age=50
print(bob.age)

del bob.age
#print(bob.age)

print(Person.wants_to_hack)

bob1=Person.bob_factory()
bob2=Person.bob_factory()
bob3=Person.bob_factory()
bob1.print_name()
bob2.print_name()
bob3.print_name()

Person.static_print()
bob1.static_print()
bob2.static_print()
bob3.static_print()



