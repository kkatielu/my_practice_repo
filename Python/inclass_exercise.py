for i in range(1,20):
    if i % 3 == 0:
        print(i)

counter = 0
sum = 0
while counter <= 50:
    if counter % 2 == 0:
        sum += counter
    counter +=1
print(sum)

numbers = [5, 8, 2, 15, 10, 3, 7]
for val in numbers:
    if val > 5:
        print(val, end = " ")