# Classes


# Here we are creating a class called Animal.
# You can add object if you want to. If you don't do it, then Python will do it implicitly.

class Animal (object):


# Here we are defining the constructor. The constructor receives the attribute values when the object is created.
# Self refers to the object that is calling the method.
# Example: Reference variable: "Dog". All the arguments for Dog : 4,"Blue","Black" will passed to the constructor.
# Self would in this case be Dog.
# The constructor would look like this:
# def __init__(self, number_of_legs = 4,color_of_eyes = "Blue",skin_color = "Black"):


    def __init__(self, number_of_legs,color_of_eyes,skin_color):

# The attribute values passed to the constructor above are saved for each and every object that is created.
# Example: Reference Variable: "Dog".
# The values in the constructor (look at last line of comment text inbetween class Animal and def init) will now be stored variables.
# Dog.legs = 4 & Dog.color = "Blue" & Dog.skin = "Black"

        self.legs = number_of_legs
        self.color = color_of_eyes
        self.skin = skin_color

# Here we are defining the methods in our class.
# IMPORTANT: Always add a self in brackets, so that the method can return the attribute value(s) of the object calling the method.

    def get_n_o_legs (self): # Reference variable: Dog. This method will return Dog.legs. We know that in Dog.legs a value is stored.
        return self.legs # This will return 4.

    def get_skin_col (self): # Reference variable: Dog. This method will return Dog.color. We know that in Dog.color a value is stored.
        return self.color # This will return Blue

    def get_color_eyes (self): # Reference variable: Dog. This method will return Dog.skin. We know that in Dog.skin a value is stored.
        return self.skin # This will return Black.

 # Now we have create the structure of our class "Animal"

 # Now we need to instantiate objects (create) in our class.

 # Dog is our reference variable.

 # Here we created an object named Dog with the attributes that we defined in our class.

 # The values in the brackets are called Arguments

 # The values in the brackets are passed to the constructor (def __init__)

Dog = Animal(4,"Blue","Black")

# Cat is our reference variable again.

# See Dog

Cat = Animal(4, "Green","Gray")

# See Dog

Rabbit = Animal(4,"Brown","White")

 # Here the reference variable dog is calling the method get_n_o_legs()
 # The method will return you the attribute value: number_of_legs for your object "Dog"
 # In this case the terminal will print "4"

print (Dog.get_n_o_legs())
print (Dog.get_skin_col())
print (Dog.get_color_eyes())

# Here the reference variable "Dog" called the three methods in our class "Animal".

# You can easily substitute "Dog" with the reference variable "Cat"

print (Cat.get_n_o_legs())
print (Cat.get_skin_col())
print (Cat.get_color_eyes())

