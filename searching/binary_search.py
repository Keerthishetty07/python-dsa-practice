arr = [2, 5, 8, 12, 16, 23, 38]
key = 16

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at index:", mid)
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")
