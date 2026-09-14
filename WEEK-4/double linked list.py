class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 1:
            self.insert_begin(data)
            return

        temp = self.head
        count = 1

        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        if temp.next is None:
            self.head = None
            return

        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None

    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            self.delete_begin()
            return

        temp = self.head
        count = 1

        while temp is not None and count < position:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid position")
            return

        if temp.next is not None:
            temp.next.prev = temp.prev

        if temp.prev is not None:
            temp.prev.next = temp.next

    def count(self):
        temp = self.head
        count = 0

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        print("Doubly Linked List:", end=" ")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("END")

dll = DoublyLinkedList()
while True:
    print("\n--- DOUBLY LINKED LIST ---")
    print("1. Insert Begin")
    print("2. Insert End")
    print("3. Insert at Specific Position")
    print("4. Delete Begin")
    print("5. Delete End")
    print("6. Delete at Specific Position")
    print("7. Count")
    print("8. Display")
    print("9. End")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        dll.insert_begin(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        dll.insert_end(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        position = int(input("Enter position: "))
        dll.insert_at_position(data, position)

    elif choice == 4:
        dll.delete_begin()

    elif choice == 5:
        dll.delete_end()

    elif choice == 6:
        position = int(input("Enter position: "))
        dll.delete_at_position(position)

    elif choice == 7:
        dll.count()

    elif choice == 8:
        dll.display()

    elif choice == 9:
        print("Program ended")
        break

    else:
        print("Invalid choice")
