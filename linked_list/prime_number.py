class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" ")
                n = n.ref

    def add_begin(self, data):
        new_data = Node(data)
        new_data.ref = self.head
        self.head = new_data

    def add_end(self, data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_data

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, (n //2) + 1):
            if n % i == 0:
                return False
        return True

    def find_primes(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                if self.is_prime(n.data):
                    print(n.data, end=" ")
                n = n.ref

# Example usage:
a1 = LinkedList()
a1.add_begin(3)
a1.add_begin(99)
a1.add_end(11)
a1.add_end(5)
a1.add_begin(1)

print("Prime numbers in the linked list:")
a1.find_primes() 
