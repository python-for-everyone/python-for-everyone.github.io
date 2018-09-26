# Single Inheritance

# It is is called single inheritance because every class inherits from one class only.

# General Class
class Animal (object):
    def __init__(self, number_of_legs, color_of_eyes, skin_color):
        self.legs = number_of_legs
        self.color = color_of_eyes
        self.skin = skin_color
    def get_n_o_legs (self):
        return self.legs

    def get_skin_col (self):
        return self.color

    def get_color_eyes (self):
        return self.skin


# Specialized Class
# Here we created another constructor, because we extended the class by one additional attribute(color_of_collar).
# super () passes the arguments to the constructor in the Animal class.

class Dog (Animal):
    def __init__(self,number_of_legs,color_of_eyes,skin_color,color_of_collar):
        super().__init__(number_of_legs,color_of_eyes,skin_color)
        self.collar = color_of_collar
    def get_color_of_collar(self):
        return self.collar

# Pass is just there so that class isn't empty. If I wouldnt write pass, it would throw an error.
class Cat(Animal):
    pass


Stani = Dog(4,"Blue","Brown","Gray")

# We are able to call the methods that exist in both the Dog and Animal class.
print (Stani.get_color_of_collar())
print (Stani.get_color_eyes())

# Same as above
Mitsy = Cat (4,"Blue","White")
print (Mitsy.get_n_o_legs())

#---------------------------------------------------------------------------------------------------------------------


# Multi-level Inheritance

# It is called multi-level inheritance because Cat inherits from Dog and Dog inherits from Animal.

class Animal ():

    def __init__(self, number_of_legs, color_of_eyes, skin_color):
        self.legs = number_of_legs
        self.color = color_of_eyes
        self.skin = skin_color
    def get_n_o_legs (self):
        return self.legs

    def get_skin_col (self):
        return self.color

    def get_color_eyes (self):
        return self.skin


# Specialized Class

class Dog (Animal):
    def __init__(self,number_of_legs,color_of_eyes,skin_color,weight):
        super().__init__(number_of_legs,color_of_eyes,skin_color)
        self.weight = weight

    def get_weight (self):
        return self.weight

# Pass is just there so that class isn't empty. If I wouldn't write pass, it would throw an error.
class Cat(Dog):
    pass

Mitsy = Cat(4,"Blue","Brown","5kg")

# I have access to all attributes and methods that exist in both classes.

print (Mitsy.get_n_o_legs())
print (Mitsy.get_weight())

#---------------------------------------------------------------------------------------------------------------------

# Multiple Inheritance

class Grades(object):
    def __init__(self,Math,Science,English):
        self.Math = Math
        self.Science = Science
        self.English = English

    def get_math (self):
        return self.Math
    def get_science (self):
        return self.Science
    def get_english (self):
        return self.English

class Students(object):
    def __init__(self,Grade, Homeroom_Teacher):
        self.grade = Grade
        self.homeroom_teacher = Homeroom_Teacher

    def get_grade (self):
        return self.grade
    def get_homeroom_teacher (self):
        return self.homeroom_teacher


class Persons (Grades,Students):

    # Necessary in order to pass the arguments to the respective classes.
    def __init__(self,Math,Science,English,Grade,Homeroom_Teacher):
        Grades.__init__(self,Math,Science,English)
        Students.__init__(self,Grade,Homeroom_Teacher)

# I always was bad science, so I'll give myself the worst grade possible haha. 7 is the highest grade.

# Voila, I now have access to all the attributes and methods that exist in both classes.

Linus = Persons(5,1,6,12, "Mr.Rasmussen")

print(Linus.get_english())
print (Linus.get_grade())

#----------------------------------------------------------------------------------------------------------

# Polymorphy

class Animal (object):
    def sound(self):
        print ('This Animal makes a generic sound')

class Dog (object):
    def sound (self):
        print ('Wuuuf')

Stani = Dog()

# This is called method overriding which is a form of Polymorphy.
# I created an object in the class Dog which inherits from Animal.
# In the class Dog two identically named methods exist (Sound).
# Python will call the method that was redefined in the Dog class.
# If you create an object in the Animal class, then it will of course call the method in the animal class.
# Remember: Python will always call the redefined method.

Stani.sound()





