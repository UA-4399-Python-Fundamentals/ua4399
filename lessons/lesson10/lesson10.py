
# class MyClass:
#     """A simple example class."""
#     a = 1
#     pass

# print(MyClass.__doc__)
# print(type(MyClass))
# m = MyClass()
# print(type(m))

# # print(a)
# print(MyClass.a)
# print(m.a)

# class MyClass:
#     print("Class variable")
#     cm = [1, 2, 3]  # class variable
#     ci = 0  # class variable

#     def __init__(self):
#         print("Constructor called")
#         self.im = [10,20,30]  # instance variable
#         self.ii = "inst"  # instance variable

# m1 = MyClass()
# m2 = MyClass()
# print(m1.cm, m1.ci, m1.im, m1.ii)
# print(m2.cm, m2.ci, m2.im, m2.ii)
# m1.cm[0] = 100
# m2.im[0] = 200
# m1.ci = 10
# m2.ii = 20
# print(m1.cm, m1.ci, m1.im, m1.ii)
# print(m2.cm, m2.ci, m2.im, m2.ii)
# print(MyClass.cm, MyClass.ci)

# class Animal:
#     """A base class for all animals."""
#     count = 0  # class variable to keep track of the number of animals
#     def __init__(self, name, age=10):
#         self.name = name
#         self.age = age
#         Animal.count += 1

#     def speak(self):
#         print(f"{self.name} makes a sound.")
    
# animal_1 = Animal("Lion", 5)
# animal_2 = Animal(age=7, name="Tiger")
# animal_3 = Animal("Elephant")
# print(animal_1.name, animal_1.age, animal_1.count)  # Output: Lion
# print(animal_2.name)  # Output: Tiger
# print(animal_3.name)  # Output: Tiger
# print(Animal.count)  # Output: 0 (class variable, not yet incremented)

# animal_1.speak()  # Output: Lion makes a sound.
# animal_2.speak()  # Output: Tiger makes a sound.
# animal_3.speak()  # Output: Elephant makes a sound.
# print(dir(animal_1))
# print(animal_1.__dict__)
# print(animal_2.__dict__)
# print(animal_3.__dict__)
# print(Animal.__dict__)
# # Animal.speak()#TypeError: Animal.speak() missing 1 required positional argument: 'self'
# Animal.speak(animal_1)  # Output: Lion makes a sound.
# my_f = Animal.speak
# my_f(animal_2)  # Output: Lion makes a sound.
# def my_f2(obj):
#     print(dir(obj))


# my_f2(animal_1)
# my_f2(Animal)
# Animal.my_ff = my_f2  # Adding a method to the class
# animal_1.my_ff()  # Output: Lion makes a sound.