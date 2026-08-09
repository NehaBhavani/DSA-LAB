def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
n = int(input("Enter the number of elements:"))
arr = []
print("Enter elements in order:")
for i in range(n):
    arr.append(int(input()))
key = int(input("Enter the element to search:"))
result = linear_search(arr,key)
if result!=-1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
