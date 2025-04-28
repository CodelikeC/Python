print("Set of the Python")

# find the unique elements in the list // 
array = [1,2,2,3,2,1,2]
set_1 = set([1,2,2,3,2,1,2])
print("The set 1 is:")
print(set_1)

# find the unique elements in the tuple // 
tuple = (2,4,6,5,2)
set_2 = set((2,4,6,5,2))
print("The set 2 is:")
print (set_2)

# find the unique character in string "Banana"
set("Banana")

# get the union of set1_ and set2_
set_1.union(set_2)
print(set_1.union)

# get the intersection of set_1 and set_2 
set_1.intersection(set_2)
print(set_2.intersection)

#get the subset of (1,2,3,4,5)
set_1.issubset((1,2,3,4,5))
print(set_1.issubset)

