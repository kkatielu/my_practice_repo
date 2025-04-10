# Katie Lu

def highest_avg(nums):
    """
    Returns the average of the two largest numbers in the list. 
    List will have at least two values
    """
    first_max = max(nums)
    nums.remove(first_max)
    second_max = max(nums)
    
    total = first_max + second_max
    average = total / 2
    return average

def divide(list, num):
    """
    Returns the original list divided by the input number. 
    """
    divided = [x/num for x in list]
    return divided

print(highest_avg([3, 4, 5, 6, 7]))
print(highest_avg([2, 9, 4, 2, 9, 3, 6]))
print(highest_avg([2, 3]))

print(divide([3, 4, 5, 6, 7], 2))
print(divide([2, 9, 4, 2, 9, 3, 6], 7))
print(divide([2, 3], 1))

