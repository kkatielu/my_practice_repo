print("Hello World!")

# this is a single line with a comment

'''
multi-line comment
line #2
'''

# highlight + command + /
# to comment multiple
# lines at once

# Variables
x = 10
x = "hello"
x = [1, 2, 3]
print(x)

x = 100
y = 10
result = int(x / y)
result = int(result)
print(result)

x = 105
result = x // y
print(result)

min_val = min(1, 10, 50) 
print(min_val) 
raised = pow(2,3)
print(raised)
raised = 2 ** 3
print(raised)

x = -1
y = 0
if x < 0:
    print("x is negative")
elif x > 0:
    print("x is positive")
else:
    print("x is 0")

start = 10
end = 100

if x >= start and x <= end:
    print("x is within range")

if x < start or x > end:
    print("x is not within range")

counter = 0
while counter < 5:
    print(counter)
    counter += 1

for i in range(1,5):
    print(i)

for i in range(1,5,2):
    print(i, end = " ")
print()

list = [2, 4, 6, 8]
for i in range(len(list)):
    print(i, list[i], end = " ")
print()

for val in list:
    print(val)

for i, val in enumerate(list):
    print(i, val, end = " ")
print()


def hello_world():
    print("Hello World!")
hello_world()

def hello(name):
    print("hello " + name)
hello("Bob")

def hello2(name = "Bob"):
    print("Hello " + name)
hello2()
hello2("Jane")

def swap(list):
    last_index = len(list) - 1
    temp = list[last_index]
    list[last_index] = list[0]
    list[0] = temp
list = [0, 3, 8, 4, 5]
swap(list)
print(list)

hello = "hello"
for c in hello:
    print(c)

course = "Platform Computing"
plat = course[0 : 8]
print(plat)
comp = course[9 : 18]
print(comp)

def string3(string):
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
    The string length will be at least 2.
    """
    last_two = string[len(string) - 2 : len(string)]
    result = last_two * 3
    return result

