class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    # Insert at specific position
    def insert_at_position(self, data, position):
        if position == 1:
            self.insert_begin(data)
            return

        new_node = Node(data)
        temp = self.head
        count = 1

        while temp.next != self.head and count < position - 1:
            temp = temp.next
            count += 1

        if count != position - 1:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        self.head = self.head.next
        temp.next = self.head

    # Delete end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head

    # Delete at specific position
    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            self.delete_begin()
            return

        temp = self.head
        count = 1

        while temp.next != self.head and count < position - 1:
            temp = temp.next
            count += 1

        if temp.next == self.head:
            print("Invalid position")
            return

        temp.next = temp.next.next

    # Count
    def count(self):
        if self.head is None:
            print("Number of nodes: 0")
            return

        temp = self.head
        count = 0

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes:", count)

    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        print("Circular Linked List:", end=" ")

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("HEAD")


# Main program
cll = CircularLinkedList()
while True:
    print("\n--- CIRCULAR LINKED LIST ---")
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
        cll.insert_begin(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        cll.insert_end(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        position = int(input("Enter position: "))
        cll.insert_at_position(data, position)

    elif choice == 4:
        cll.delete_begin()

    elif choice == 5:
        cll.delete_end()

    elif choice == 6:
        position = int(input("Enter position: "))
        cll.delete_at_position(position)

    elif choice == 7:
        cll.count()

    elif choice == 8:
        cll.display()

    elif choice == 9:
        print("Program ended")
        break
    else:
        print("Invalid choice")
