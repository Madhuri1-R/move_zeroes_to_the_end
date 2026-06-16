def move_zeroes(arr):
    result = []
    for x in arr:
        if x != 0:
           result.append(x)
    zero_count = arr.count(0)
    for i in range(zero_count):
        result.append(0)
    return result
n = int(input("Enter number of elements:"))
arr = []
for i in range(n):
    num = int(input("Enter elements:"))
    arr.append(num)
    result = move_zeroes(arr)
print("Array after moving zeroes:",result)            


    
