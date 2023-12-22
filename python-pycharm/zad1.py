list1 = []
for i in range(6):
    n = int(input("Enter number: "))
    list1.append(n)

minNumber = min(list1)
print(f"Minimum number is: {min(list1)}")
print(f"Index of minimum number is: {list1.index(minNumber)}")
