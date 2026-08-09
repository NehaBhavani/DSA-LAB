def search(emp, key, index):
    if index == len(emp):
        return False
    if emp[index] == key:
        return True
    return search(emp, key, index + 1)

emp = [101, 102, 103, 104, 105]

key = int(input("Enter Employee ID to search: "))

if search(emp, key, 0):
    print("Employee ID Found")
else:
    print("Employee ID Not Found")
