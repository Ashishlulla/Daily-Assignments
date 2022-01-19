# 1.Write a Python program to filter a list of integers using lambda funtion:

lst =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even Numbers : ",list(filter(lambda x: x % 2 == 0, lst)))
print("Odd Numbers : ",list(filter(lambda x: x % 2 == 1, lst)))


# 2. .Write a Python program to add to given list using lambda Function:

lst1 = [1,2,3]
lst2 = [4,5,6]
print(list(map(lambda x,y:x+y, lst1, lst2)))

# 3.Write a python to print all the from 1 to 6 except 3 and 6.

for i in range(1,7):
    if i == 3 or i == 6:
        continue
    else:
        print(i, end=" ")
