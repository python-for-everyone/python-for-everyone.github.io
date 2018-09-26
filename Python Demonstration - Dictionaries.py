#Dictionaries

# Key value pairs

#Imagine we are keeping track of all the football players in the club.

# We want to store their name and age in a dictionary.

football_club_fc = {
                    "Kevin":22,
                    "Paduk":21,
                    "Bastian":20,
                    "Leonard":23,
                    "Maximilian":19,
                    "Tobias":22,
                    "Ahmed":24,
                    "Andreas":21,
                    "Mattias":22,
                    "Toni":23,
                    "Thomas":21
                    }
# All the names (e.g. Kevin and Paduk) are the keys of the dictionary.
# All the ages (e.g. 21 and 22) are the values of the dictionary.

#----------------------------------------------------------------------------------------------------------------------

# Methods

# We will stick to the same example as above.

#  Method values()

# Let's say we want to have the age of all players in the football club.

# We do it as written below:

for x in football_club_fc.values():
    print(x)

# The above written code will print all the values in the football_club_fc dictionary (iterate over the values).




# Method keys()

# Now we want to have the name of all players in the football club.

# We do it as written below:

for x in football_club_fc.keys():
    print(x)

# The above written code will print all the keys in the football_club_fc dictionary (iterate over the keys).



# Method items()

# We are not satisfied with the output yet. Instead we want to have a "list" with the names of the players and their respective age.

# We do it as written below:

for x,v in football_club_fc.items():
    print(x, end=",")
    print(v)

# The above written code will print all the items in the football_club_fc dictionary (iterate over the items).



# Method get()

# On the internet you've read that Cristiano Ronaldo might be joining your football club.

# Now you want to check in your dictionary, if there's a player called "Cristiano".

print(football_club_fc.get("Cristiano",'Its just a rumour'))

# Unfortunately there is no player called Cristiano in our keys.

# Therefore "Its just a rumor" will be returned.

# If Cristiano would be in our dictionary, then Python would return his age (value).



# Method setdefault()

# Your football club just signed Kevin Artenga.

# You want to check, if he already exists in the dictionary.

# We can do this by using setdefault.

print (football_club_fc.setdefault("Kevin Artenga","24"))

# Now lets iterate over our dictionary.

for x,v in football_club_fc.items():
    print(x,v)

# At the very end of our "list" we can see that Kevin Artenga has been added (He didn't exist before, otherwise his value in this his age would have been returned)


#--------------------------------------------------------------------------------------------------------------------------

# Add and remove key-value pairs from your dictionary.

# Add a key-value pair(add a player with an age to the dictionary)

football_club_fc["Kenneth Zimbabwe"] = 24

# Now lets iterate over our dictionary

for x,v in football_club_fc.items():
    print(x,v)

# As you can see Kenneth Zimbabwe has been added to our dictionary.

# Delete a key-value pair

del football_club_fc["Kenneth Zimbabwe"]

# Now lets iterate over our dictionary

for x,v in football_club_fc.items():
    print(x,v)

# Kenneth Zimbabwe has been deleted from our dictionary.

















