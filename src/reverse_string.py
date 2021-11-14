import sys

def reverse_string(val:list[chr])->bool:
    """
    This function will loop through half of the list and swap index position with last-index position.
    """
    for index in range(int(len(val)/2)): #loop through half list
        print(index)
        print(val)
        val[index],val[len(val)-1-index] = val[len(val)-1-index],val[index] #swap by using multiple assignment
        print(val)
    return val


