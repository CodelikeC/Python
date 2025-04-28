#Name : Nguyen Duc Tri 
#Troy ID : 1677467 
# do problem 1 in page 188 
import numpy as np 
items = [
    "item1", 
    "item2", 
    "item3", 
    "item4", 
    "item5", 
]

file_name = "list_name.txt"

with open(file_name, "w") as file : 
    for item in items : 
        file.write (item + "/n")
        print ("List items have been save to", file_name)
