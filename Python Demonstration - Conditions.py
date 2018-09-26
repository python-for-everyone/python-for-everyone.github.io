# True and False.

"""
True = 5

print (True)  # This will throw an error. Don't forget to comment this in to see the effect.

"""

Var_x = True

print (Var_x) # This will work.

#-------------------------------------------------------------------------------------------------------------------------------

# and, or & not.

name = 'Linus'
state = 'Happy'

if name == 'Linus' and state == 'Happy': # It will print Great, because both conditions are true (name is Linus and state is happy)
    print ("Great")

if name == 'Linus' and state == 'Sad':  # This will not print Damn, because both conditions are not true (only one is true)
    print ('Damn')

if name == 'Linus' or state == 'Sad': #It will print Okay, because at least one condition is true (name is linus, but state is not sad)
    print ("Okay")

if name == 'Kevin' or state == 'Sad': #It will not print Alright, because both conditions are false.
    print ("Alright")

if name is not "Kevin" and state == 'Happy': #It will print Wohoo, because both conditions are true (name is not Kevin --> name is Linus)
    print ("Wohoo")

#--------------------------------------------------------------------------------------------------------------------------

# If-statements.

# Let's imagine there is a human called "Linus" who just received his math grade.
# He got 51 Points out of 100 possible points.
# As you may have noticed, Linus is not an expert when it comes to math.
# If leave 51 in the Grade variable, then the first condition is true and passed is printed.
# If I change the variable Grade to 100, then the first if-statement will be true (100 is greater equal 50).
# We actually want it to say "full marks".
# Solution: Change the order of the elif and if statements.
# Now change the 100 to 80.
# Change to the Grade variable to 3.14
# The else-statement will be executed, because the Grade variable contains a number with decimal places.


# This order gives the wrong output.

Grade = 3.14

if Grade >= 50:
    print ('Passed')
elif Grade >=60:
    print ("Satisfactory")
elif Grade >=70:
    print ("Good")
elif Grade >=80:
    print ("Very Good")
elif Grade >= 90:
    print ("Excellent")
elif Grade == 100:
    print ("Full marks")
else:
    print ("Please enter an integer")

#Solution to the problem above.
#This order gives the right output.

if Grade == 100:
    print ("Full marks")
elif Grade >= 90:
    print ("Excellent")
elif Grade >=80:
    print ("Very Good")
elif Grade >=70:
    print ("Good")
elif Grade >=60:
    print ("Satisfactory")
elif Grade >= 50:
    print ('Passed')
else:
    print("Please enter an integer")

#--------------------------------------------------------------------------------------------------------------------------

# Loops.


# While loop

# Imagine we have to pay our rent in 10 days. We want a reminder of how many days are left until the rent is due.

days = 1 # We start from today.
days_left = 10  #This how many days we have left from today.


while days < 10: #On the tenth day the condition is not true anymore (days = 10 is not smaller than 10).

    days_left = days_left - 1 # I reduce the value in days_left by 1, because a day has passed.
    days = days + 1          # I increase the value in days, because another day has passed.
    print (days_left)

print ("Rent is due today. ")  # This is printed on the tenth day, because the while loop is not executed.

# For loop.

# Imagine you wanted to print "Never give up" ten times on your terminal before you go to work as a motivational push.

# You can do this with the for loop.

# Every morning you would run this and it would print "Never give up" for you.

# In the range brackets you can add up to three parameters: Start, End, Interval

# For example: (0,10,2) --> i starts at 0 and ends at 9 (The end is always minus 1), and interval 2.

# This would print "Never give up" five times!

# Go ahead and try it.

for i in range (10): # i is a random variable that I chose. You cant put whatever you like there (x,y.z and so forth)
    print ("Never give up")

# You can also solve this problem with a while loop. You need to add an auxilliary variable.

cycle = 0

while cycle < 10:
    cycle = cycle + 1
    print ("Never give up")


# Break statement.

# Let's say we are an employee trying to login to our system with our credentials.
# The backend system would look like this (very simplified!!!)
# Your name Linus and password hello123 are saved in the database.

user_input_name = input('What is your name? ')
user_input_password = input('What is your password? ')

while True:
    if user_input_name == 'Linus' and user_input_password == 'hello123':
        break #If the user enters the right name and password, then it leaves the loop and prints "Access granted".
    else:
        print ('Wrong name or password! ')

        # We need to add the inputs again, because it would otherwise end up in an infinite loop.

        user_input_name = input('Please enter your name again: ') #User enters name again.
        user_input_password = input('Please enter your password again: ') # User enters password again.

print ("Access granted")


# Continue statement.

while True:
    user_input_name = input('What is your name? ')
    user_input_password = input('What is your password? ')

    if user_input_name != 'Linus' or user_input_password != 'hello123': #If the user enters a wrong name or password, then he's brought back to the beginning of the loop (continue)
        print("Please enter the name and password again! ")
        continue
    else:
        break

print("Access granted")
















