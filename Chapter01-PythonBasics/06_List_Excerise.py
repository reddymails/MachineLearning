#
# Assignment
#
# You are a Marvel fan and created a list of superheroes.
#
# avengers  = ["Iron Man", "Captain America", "Black Widow", "Hulk", "Thor", "Hawkeye"]
# Using this list, do the following:
#
# Calculate how many members are in the Avengers team?
# Iron Man made Spider-Man a new member of the Avengers, add him to your list.
# Captain America is the leader of the Avengers, you need to add him before Iron Man, so remove him from the list and add him before Iron Man.
# You don’t like Thor and Hulk together because they get angry easily and fight with each other. So you have to separate them from each other. To separate them, either move “Black Widow” or “Hawkeye” in between them.
# After Avengers: End Game the original six avengers are retired, now you need to remove them from your list and add new superheroes like Doctor Strange, Vision, Wanda, Kate Bishop, and Ant-Man.
# As “Captain America” is also retired and now currently, no one is the leader, so sort the list in alphabetical order. Whoever will come at the 0th index will become the Leader. (BONUS: can you guess who will become the leader)

avengers  = ["Iron Man", "Captain America", "Black Widow", "Hulk", "Thor", "Hawkeye"]

# Calculate how many members are in the Avengers team?
print(len(avengers))

# Iron Man made Spider-Man a new member of the Avengers, add him to your list.
avengers.append("Spider-Man")

# Captain America is the leader of the Avengers, you need to add him before Iron Man, so remove him from the list and add him before Iron Man.
avengers.remove("Captain America")
avengers.insert(0,"Captain America")
print(avengers)

# You don’t like Thor and Hulk together because they get angry easily and fight with each other. So you have to separate them from each other.
# To separate them, either move “Black Widow” or “Hawkeye” in between them.
avengers.remove("Hawkeye")
avengers.insert(4,"Hawkeye")
print(avengers)

# After Avengers: End Game the original six avengers are retired, now you need to remove them from your list
# and add new superheroes like Doctor Strange, Vision, Wanda, Kate Bishop, and Ant-Man.
print(dir(avengers))
avengers.clear()
avengers = ["Doctor Strange","Vision","Wanda","Kate Bishop","Ant-Man"]
print(avengers)

#As “Captain America” is also retired and now currently, no one is the leader, so sort the list in alphabetical order.
# Whoever will come at the 0th index will become the Leader. (BONUS: can you guess who will become the leader)
avengers.sort()
print(avengers[0])


