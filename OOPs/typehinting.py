
from typing import List

#provide the type of argument and the output: avg_list(sequence: list) -> float: 
#However, using the list object as a type hinting is usually not recommended
#Ideally you should be using < from typing import List >

def avg_list(sequence: list) -> float:  #The sequence is a list of elements and returns a float
    return sum(sequence)/len(sequence)

list_avg = avg_list(123)
