numbers = [2,4,5,13,3]
largest = numbers[0]                                               
for n in numbers:
    if n > largest:
        largest = n
print(f"the largest number form the list is : {largest}")