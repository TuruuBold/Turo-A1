#Practical assessment 1:
# task 1

"""
    Creating class named bird, with 2 variables ( names and age).
"""
"""
creating class called bird- __init__ is build in constructor. 
Class bird has two variables ( name and age ) nonono

"""
class Bird:
    def __init__(self, name , age):
# __name is to secure the variables name and age thus user or
# or any cannot modify them.
        self.__name=name
        self.__age=age

        self.set_name(name)
        self.set_age(age)
# defining get name function. it is used to access and retrieve values.
    def get_name(self):
        return self.__name

    def get_age(self):

      return self.__age
# the defining the set function is used to ask user input and validate the
# user input. if the user enters a age that is less than one then the cod will make the
# input value to 1. if more than 20 then it will make it 20 minimum.
    def set_age(self, age):
        if age < 1:
            self.__age = 1
        elif age > 20:
            self.__age = 20
        else:
            self.__age =age
# defining the set name function. this is to validate the user input name
# if the user input name has any space then it will replace the space " " with -.
    def set_name(self, name):
        self.__name = name.replace(" ", "-")

# the print name function is to display the output of the bird name and with text saying can fly
# later this function will be called to display the text along with user input (bird name)
    def print_name(self):
        print(f"Bird- {self.__name} can fly. ")
        print("********************************")
# str() is built in function in Python that is used to convert the value into a string data type
    def __str__(self):
        print(f"The name of the bird is {self.__name} and the age is {self.__age}.")
# creating Cockatoo class which is child class of the Class bird. when creating the class we do not have to
# call all the parameter instead using __init__ and super we can call the parent CLASS bird.
# we just add the one additional variable colour.
class Cockatoo(Bird):
    def __init__(self, name, age, colour):
        super().__init__(name, age,)
        self.set__colour(colour)
# creating the get function and returning the value only the get function must have return function
    def get_colour(self):
        return self.__colour
#defining the colour function- which has 5 allowed colour list. is user input colour is different than
# these colours then the input will be white by default.
    def set__colour(self, colour):
        if colour not in ["black", "orange", "pink", "grey", "white"] :
            self.__colour= "white"
        else:self.colour = colour

#print name func is to display the name of the Cockatoo userinput and it can fly.
    def print_name(self):
        print(f"Cockatoo- {self.get_name()} can fly")
        print("********************************")
    def __str__(self):
        return (f"the Cockatoo colour is {self.get_colour()} named: {self.get_name} and age of {self.set_age} ")
# creating the Class called Ostrich, that has variables with name and age from the
# parent class bird with one additional variable weight
# inside the parentheses parent class bird is called.
class Ostrich(Bird):
    def __init__(self, name, age, weight):
#super is to call the parent class with name and age variables.
        super().__init__(name, age)
# setter is additional variable for Ostrich Class.
        self.set__weight(weight)
# def func get weigth for return its input value
    def get__weight(self):
        return self.__weight
# setter for weight to assign the value to private variable weight with
# user input validation with less than 1 and more than 20.
    def set__weight(self, weight):
        if weight < 1:
            self.__weight= 1
        elif weight > 75:
            self.__weight=75
        else:self.__weight=weight
# def the function print_name to display the Ostrich name (user input) and text.
    def print_name(self):
        print(f"Ostrich- {self.get_name()} can NOT fly ! ")
        print("********************************")
# str function to return user input. name and age.
    def __str__(self):
        return (f"Ostrich name {self.get_name()} and age is {self.get_age()}, the weight of {self.get_weight()}")
# creating the object of Bird and Ostrich and Cockatoos. along with thier
# unique name, age, colour and weight.
bird1=Bird("Coco", 5)
bird2=Bird("Melon", 0)
bird3=Bird("Ozzy", 11)
bird4=Bird("Pax", 11)
bird5=Bird("Phoenix", 22)
# object for Cockatoos with their required input value name, age and colour
Cockatoo1=Cockatoo("Tanner",13, "red")
Cockatoo2=Cockatoo("Ted", 12, "red")
Cockatoo3=Cockatoo("TJ", -1, "red")
Cockatoo4=Cockatoo("TR", 5, "red")
Cockatoo5=Cockatoo("Tucker", 19, "red")
# object for Ostrich with their required input value name, age and weight
Ostrich1=Ostrich("PT", 15, 76)
Ostrich2=Ostrich("Cher", 15, 0)
Ostrich3=Ostrich("Chloe", 12, 74)
Ostrich4=Ostrich("Holly", 11, 73)
Ostrich5=Ostrich("Greta", 11, 100)
# creating a list that contains all objects.
Allbirds=[bird1, bird2, bird3, bird4 , bird5, Cockatoo1, Cockatoo2 , Cockatoo3
    ,Cockatoo4 ,Cockatoo5, Ostrich1,  Ostrich2 , Ostrich3,  Ostrich4,  Ostrich5,]
# using for loop for all 15 object of all parent and child classes.
# for loop is used to repeat the code. the if statement has the validation for age function
# so that the program will go through all the subject and display only object bird age with more that 10 only
for bird in Allbirds:
    if bird.get_age() > 10:
        bird.print_name()



























