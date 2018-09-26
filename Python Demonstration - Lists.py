# Lists

# Imagine that you are working in a company where you are responsible for the maintenance of employees in a list.

list_a = ['Linus','Osama','Admira','Erik','Stina']

# Linus is the element with the index number 0, whereas Stina is the element with the index number 4.

# If you now want to retrieve Linus from the list, then you need to use the index number 0.
# You can also use -5 as index number to get Linus from the list.

print(list_a[0])
print(list_a[-5])

# If you know want to retrieve Stina from the list, then you need to use the index number 4.
# You can also use -1 as an index number to get Stina from the list.

print(list_a[4])
print(list_a[-1])


# If you want to retrieve Linus from the list with an index number that is an integer, then you will get an error!

# print (list_a[1.0]) # Comment this in to see the effect.

# If you want to retrieve an element with an index number greater than the total number of elements in the list, then you will also get an error!

#print (list_a[5]) #Comment this in to see the effect.

# There are only four index numbers in list_a --> 0,1,2,3,4 (5 doesnt exist and will produce an error)

#-----------------------------------------------------------------------------------------------------------------------------

# List manipulation

# Slicing

# If you now  want to retrieve several elements simultaneously from a list, then you can use slicing.

# In our case we want to fetch the first two elements of list_a (Linus and Osama)

print (list_a[0:2])



# Changing the value of an exisiting element in a list

# It can be done as follows:


list_a[4] = 'Kenneth'

for x in list_a:
    print (x)

# You will see that Stina has been replaced by Kenneth.



# Deleting an element from a list.

# If you want to delete an element from a list, then you can use del.

del list_a[0]

for x in list_a:
    print(x)

# You will see that Linus has been removed from the list.


#--------------------------------------------------------------------------------------------------------------------------

# Methods when working with lists


# index

print(list_a.index('Kenneth'))

# The print-statement will return me the index number of the searched element "Kenneth".

# Now I will add another element called "Kenneth" to list_a.

list_a.append('Kenneth')

# If I now use the index method (), I will get 3 as an answer even though there are two elements with the same name.

print(list_a.index('Kenneth'))

# The first occurring element in the list will be returned!



# append

# If you want to add a new element to the end of the list, then you can use the append method.

list_a.append('Sara')

for x in list_a:
    print(x)


# insert

# If you want to add a new element to a specific place in the list, then you can use the insert method.

list_a.insert(1,'Jessica')

for x in list_a:
    print (x)

# I inserted Jessica at the index position 1.


# remove

# If you want to remove an element from a list, then you can use the remove method.

list_a.remove('Admira')

for x in list_a:
    print(x)

# I removed the element Admira from list_a



# sort

# If you want to sort your list, then you can use the sort method.

list_a.sort()

for x in list_a:
    print(x)

# We can see that list_a has been sorted alphabetically.














