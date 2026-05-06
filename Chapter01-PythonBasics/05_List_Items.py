########
# Examples of List items.
#
#########

items = ["bread","butter","jam","fruits","eggs"]
## will print till index 2.
print(items[0:3])
#you can add to existing list to the end.
items.append("banana")
print(items)
# In case you want to add apple immediately after fruits we can add based on position
items.insert(4,"apple")
print(items)
# In case you need to remove "jam"
items.remove("jam")
print(items)
#If you try to remove a non-existent item it may error out.
var = "eggs" in items
if var:
    items.remove("eggs")

# Sort and print
items.sort()
print(items)
#Reverse and print.
items.sort(reverse=True)
print(items)

#Adding two lists...
list1=["INDIA","USA","UK"]
list2=["NETHERLANDS","SWITZERLAND","BRAZIL"]
all_countries = list1 + list2;
print(all_countries)
print(len(all_countries))

# All kinds of data types in same list.
heterogeneous_List = ["oneString",123,13.14,True]
print(heterogeneous_List)
