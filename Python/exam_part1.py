# Katie Lu

def repeat_start(s):
    """
    Given a string, return a new string where the first two characters 
    are repeated 
    three times. If the string is shorter than two characters, 
    return the string repeated three times.
    repeat_start("hello") returns "hehehe"
    repeat_start("a") returns "aaa"
    """
    if len(s) > 1:
        first_two = s[0:2]
        result = first_two * 3
    else: 
        result = s * 3
    return result


def shift_left(lst):
    """
    Given a list, rotate its elements to the left by one position. 
    The last element should become the first.
    shift_left([1, 2, 3, 4]) returns [2, 3, 4, 1]
    shift_left([5]) returns [5]
    """
    lst.append(lst[0])
    lst.remove(lst[0])

    return lst
    

def count_digits(s):
    """
    Use a comprehension to count the number of digits in a string.
    *** Important: your code must use comprehensions and should not be more than
    two lines of code including the return statement ***
    count_digits("The year is 2025!") returns 4
    The string function isdigit() returns True if the string is a digit.
    Eg. c='1' c.isdigit() returns True
    """
    count = [num for num in s if num.isdigit()]
    return len(count)

    

def swap(lst):
    """
    Given a list, find the minimum element in the list and swap it with the first
    element in the list. Return the list.
    swap([5,4,3,2,1]) returns [1, 4, 3, 2, 5]
    """
    index = 0
    min1 = lst[0]
    for i in range (0, len(lst)):
        if lst[i] < min1:
            min1 = lst[i]
            index = i

    temp = lst[0]
    lst[0] = min1
    lst[index] = temp
    
    return lst

    

def build_grades_dict():
    '''
    Create a dictionary where the key is a student's name and the value is
    their grade stored as an integer. 
    Read in the file, grades.txt, store the student's first and last name as 
    the key (first and last name should have a space between them) 
    and their grade as the integer value.
    Your output should read:
     {'Alice Brown': 90, 'Bob Smith': 85, 'Charlie Johnson': 78, 
     'Daisy Lee': 92, 'Evelyn Taylor': 88}
    '''
    dict = {}
    with open("grades.txt") as file:
        for line in file:
            info = line.strip().split()
            info[2] = int(info[2])
            dict[info[0] + " " + info[1]] = info[2]

    return dict


    

# Test Cases
print('repeat_start("hello") expected: hehehe')
print('repeat_start("hello") actual:', repeat_start("hello"))

print('shift_left([1, 2, 3, 4]) expected: [2, 3, 4, 1]')
print('shift_left([1, 2, 3, 4]) actual:', shift_left([1, 2, 3, 4]))

print('count_digits("The year is 2025!") expected: 4')
print('count_digits("The year is 2025!") actual:', count_digits("The year is 2025!"))

print('swap([5,4,3,2,1]) expected: [1, 4, 3, 2, 5]')
print('swap([5,4,3,2,1]) actual:',swap([5,4,3,2,1]))

print(build_grades_dict())
