# Print function


# Let's say we want to print 'Hello' 'My' 'Website' 'Viewers' three times!
# We do it as follows:

# Isn't that annoying as hell? So much code for this little output?
# I have the solution for you!
# If we also wanted to substitute the 'Viewers' to 'People', then we would need to do it at three places!
# I have another solution for you!

print ('Hello')
print ('My')
print ('Website')
print ('Viewers') #Here1
print ('Hello')
print ('My')
print ('Website')
print ('Viewers') #Here2
print ('Hello')
print ('My')
print ('Website')
print ('Viewers') #Here3

# This is the solution to the problem!
# We only need to define 'Hello' 'My' 'Website' 'Viewers' once inside the function!
# We don't need to repeat ourselves like we did up there!
# We only need to change the "Viewers" to People" once!
# The advantages of using functions!


# Def function.


def function ():
    print ('Hello')
    print ('My')
    print ('Website')
    print ('Viewers') # Right here!

print (function())
print (function())
print (function())

#---------------------------------------------------------------------------------------------------------------------

# Parameter, arguments and None.

def function_new(football_team): #(football_team) is the parameter. The parameter receives the argument and saves the received value.
    return  football_team
print(function_new('Bayern Munich')) # ('Bayern Munich') is the argument. The argument is passed to the parameter.


def function_new2():
    print ('Hello')
print (function_new2()) # This will print 'Hello' that is within the function and always return 'None', if there's no return in the function.

#------------------------------------------------------------------------------------------------------------------------

# End and sep in Python 3

print ('Hello') # After the print statement Python adds a line-break
print ('Linus')

# To avoid a line-break from happening use END = ''.

print ('Hello', end='')
print ('Linus')

# We want to separate the three strings with commas. It won't work like this!
print ('Linus','Likes','Bayern Munich')

# This is where SEP = ',' comes in place.
print ('Linus','Likes','Bayern Munich', sep=',')

#------------------------------------------------------------------------------------------------------------------------
# Local and global scope.


a = 5 # This is a global variable.

"""
 def function_new3():
    b = 5
print (b) # This will throw a NameError, because b is defined inside a function which has a local scope.
"""

# COMMENT IN FUNCTION_NEW3 TO SEE EFFECT! """ """ is used to comment out several lines.


def function_new4():  # You can use the global variable a in your function!  #If you print a now, it will show me six, because I modified it in my function.
    global a  # You don't have use global, but it's recommended.
    a = 7    # If you now print a, it'll give you 7.

print(function_new4())

print (a) # This will give 7

def function_new5():
    print(b)             # You are trying to access the local variable b in function_new6. This will throw an error!

def function_new6():
    b = 5


def function_new7():
    a = 5                    # You can use the same variable name for two variables, if they're in different scopes.

#------------------------------------------------------------------------------------------------------------------------

# Try and except

def function_new8(x):
    try:
        return 20/x
    except ZeroDivisionError:
        return ('You cant divide by Zero')

print(function_new8(2))
print(function_new8(0)) #try clause will not be able to divide by zero, thus it will jump to except clause.
print(function_new8(1)) #the division calculation still continues after the error, because we added an except clause.



