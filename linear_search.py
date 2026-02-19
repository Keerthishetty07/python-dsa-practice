arr = [5, 3, 8, 1, 9]
key = 8

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index:", i)
        break
else:
    print("Element not found")
