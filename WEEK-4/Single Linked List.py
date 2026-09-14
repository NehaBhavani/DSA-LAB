class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def deleteAtBeg(self):
        if self.head is None:
            print("No Data to delete")
        else:
            temp = self.head
            self.head = temp.next
            print("Deleted Value =", temp.data)

    def deleteAtEnd(self):
        if self.head is None:
            print("No Data to delete")

        elif self.head.next is None:
            print("Deleted Value =", self.head.data)
            self.head = None

        else:
            temp = self.head

            while temp.next.next:
                temp = temp.next

            print("Deleted Value =", temp.next.data)
            temp.next = None

    def delete(self, value):
        if self.head is None:
            print("No Data to delete")
            return

        temp = self.head

        if temp.data == value:
            self.head = temp.next
            print("Value deleted")
            return

        while temp.next and temp.next.data != value:
            temp = temp.next

        if temp.next is None:
            print("Value not present")
        else:
            temp.next = temp.next.next
            print("Value deleted")

    def count(self):
        if self.head is None:
            print("No Linked List")
        else:
            c = 0
            temp = self.head

            while temp:
                c += 1
                temp = temp.next

            print(f"Number of nodes = {c}")

    def display(self):
        if self.head is None:
            print("No Linked List")
        else:
            temp = self.head

            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next

            print("None")

ll = LinkedList()

while True:
    print("\n--- Singly Linked List ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete at Beginning")
    print("4. Delete at End")
    print("5. Delete a Value")
    print("6. Count Nodes")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        ll.insert_begin(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        ll.insert_end(data)

    elif choice == 3:
        ll.deleteAtBeg()

    elif choice == 4:
        ll.deleteAtEnd()

    elif choice == 5:
        value = int(input("Enter value to delete: "))
        ll.delete(value)

    elif choice == 6:
        ll.count()

    elif choice == 7:
        ll.display()

    elif choice == 8:
        print("Program ended")
        break

    else:
        print("Invalid choice")
