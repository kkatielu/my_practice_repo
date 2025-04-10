# list
cart = ["apples", "bananas", "cherries"]
print(cart)

cart.append("donuts")
cart.append("eggs")
cart.append("flour")
print(cart)

cart.remove("cherries")
if "cherry" in cart:
    cart.remove("cherry")
print(cart)

cart.pop(2)
print(cart)
cart.pop()
print(cart)

cart.reverse()
print(cart)

cart.sort()
print(cart)

cart.append("bananas")
cart.append("grapes")
cart.append("oranges")
print(cart)

fruit_basket = cart[3:]
print(fruit_basket)
print(cart)

squares = []
for i in range (1,11):
    squares.append(i * i)
print(squares)

squares = [i * i for i in range (1,11)]
print(squares)

print(cart)
b_items = [string for string in cart if string.startswith('b')]
print(b_items)

lst = ["1", "10", "190"]
print(lst)
num_lst = [int(x) for x in lst]
print(num_lst)

inventory = [0] * len(cart)
inventory[0] = 1
print(inventory)

# sets
empty = set()
nums_set = {1, 1, 3, 4}
print(nums_set)
lst = [1, 2, 2, 3, 3, 4]
unique = set(lst)
print(unique)
unique = list(unique)
print(unique)

st = {4, 10., 3, 7, 8}
print(st)
sorted(st)
print(st)

# dictionaries
fav_snacks = {}
fav_snacks = {"kathleen" : "tortilla chips",
               "ava" : "chex mix", 
              "emily" : "buffalo chicken dip", 
              "wade" : "popcorn"}
print(fav_snacks)
fav_snacks["lucas"] = "chocolate"
print(fav_snacks)

for key in fav_snacks:
    print(f"{key}'s favorite snack is {fav_snacks[key]}")
    print(key + "'s favorite snack is " + fav_snacks[key])

for key, value in fav_snacks.items():
    print(key, value)

if "bob" in fav_snacks:
    print("bob's fav snack is " + fav_snacks["bob"])
else: 
    fav_snacks["bob"] = "chips"
    print("bob's fav snack is " + fav_snacks["bob"])

keys = fav_snacks.keys()
values = fav_snacks.values()
print(sorted(keys))
print(sorted(values))

fav_snacks["alice"] = ["chips", "nuts"]
print(fav_snacks)