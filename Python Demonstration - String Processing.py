# String Manipulation

# Methods isalpha,isdecimal and isalnum()

# Imagine that you are working in the HR Department for a large company.

# You are responsible for creating a new profile in the system.

# The new employee has a name, a salary and password for the system.

new_employees_dictionary = {}

num_of_employees = 1 #auxiliiary variable for the keys in the dictionary.

while True:


    user_input_name = input('Enter the name here: ')
    user_input_salary = input('Enter the salary here: ')
    user_input_password = input('Enter the password here: ')

    if user_input_name.isalpha(): #this if-statement checks, if user_input_name only consists of letters.
        new_employees_dictionary["Name_%i" %num_of_employees] = user_input_name #adds user_input_name to the dictionary (Key: Name_%i).

    if user_input_salary.isdecimal(): #this if-statement checks, if user_input_salary only consists of numeric characters.
        new_employees_dictionary["Salary_%i" %num_of_employees] = user_input_salary #adds user_input_salary to the dictionary (Key: Salary_%i).

    if user_input_password.isalnum(): #this if-statement checks, if user_input_password only consists letters and numeric characters.
        new_employees_dictionary["Password_%i" %num_of_employees] = user_input_password #adds user_input_password to the dictionary (Key: Password_%i).


    if user_input_name.isalpha() and user_input_salary.isdecimal() and user_input_password.isalnum(): #if all three inputs match the corporate requirements, it will leave the endless loop.
        print ("Thank you for following our corporate standards regarding new profiles")
        break #It's up to you, if you want leave the loop or not.

    else: #if one or more inputs dont match the corüorate requirements, then it will tell the user to follow the corporate requirements.
        print("Please follow our corporate standards about creating a new profile. ")

    num_of_employees += 1 # auxilliary variable is increased by 1 every time, so that you can add new key-pair values.
                         #If you wouldn't do this, then the new inputs would overwrite the old inputs. The keys need to be unique!

    print(new_employees_dictionary)

#---------------------------------------------------------------------------------------------------------------------------

# Methods islower,isupper,startswith,endswith()

name = 'linus'

if name.islower(): # this if-statement checks, if the variable only consists of small letters. Now capitalize a letter in the string --> the print in the statement will not be executed.
    print ("Worked")

name_again = 'LINUS'

if name_again.isupper(): #this if-statement checks, if the variable only consists of capitalized letters. Now make a letter small and you'll see that it wont print "Worked again1".
    print ("Worked again!")

telefon_number = "+46 771 793 336"

#If you want to make sure that the number starts with +46, then you can use the startswith() method. If you change it to +44, then it wont work!

if telefon_number.startswith("+46"):
    print ("It starts with +46")

#If you know want to make sure that the number has the right two ending digits, then you could use the endswith() method.

# The telefon number should end with 37.

telefon_number_again = "+46 771 793 337"

if telefon_number_again.endswith("37"):
    print ("Yes, the number ends with 37")

#----------------------------------------------------------------------------------------------------------------------------

# Other string methods

# methods join,split,lower and upper ()

# Imagine that we have a list with names and unique id's of all employees in your company.

# The list looks like this:

list_of_employees_and_ids = ['Linus','23','Kevin','24','Emiliano','25']


# join

# Now you want to join the the names with the unique id's together to create usernames for the new system.

# The elements that were separated by commas before were now joined together with underscores.

print("_".join(list_of_employees_and_ids)) # I joined them together with an underscore.

# Now you can copy the name with respective unique id number.


# split

# If you now want to split a string, then you can use the split method ().

random_string = "I love food"

print (random_string.split(" "))

# You can see that the string was split based on the whitespaces in the random_string variable.


# lower

# if you want to convert a string into small letters, then you can use the method lower ()

string = 'HIGH'

print(string.lower()) #every letter in string is now small --> string = "high".

#upper

# if you want to capitalize all letters in your string, then you can use the method upper ()

string_new = 'low'

print(string_new.upper()) #the letters in string_new are now all capitalized.


#---------------------------------------------------------------------------------------------------------------------

# Cool tricks when working with strings

# You can comment out several lines of code with """ """

""" This will not be read by the interpreter.
    I am able to write several lines of code
    with this beautiful method. """

# With double quotation marks you can solve the problem of adding an apostrophe 's to a word.

print ("This is Kevin's computer")

# If I wouldn't add double quotation marks, then Python would throw an error!

# print ('This is Kevin's computer') #Comment it in to see the effect.

















