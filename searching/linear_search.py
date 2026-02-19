arr = [10, 4, 7, 2, 9]
key = 7

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index:", i)
        break
else:
    print("Element not found")
