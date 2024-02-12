# arr = [5,3,2,7,8,9,1,23,21]
# print("Before sorting:",arr)
# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if arr[j]<arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]

# print("AFter sorting:",arr)

# def pivot(list1,first,last):
#     pivot = list1[first]
#     l = first + 1
#     r = last
#     while True:
#         while l<=r and list[]



# def quicksort(list1,first,last):
#     if first<last:
#         p = pivot(list1,first,last)
#         quicksort(list1,last,p-1)
#         quicksort(list1,p+1,last)


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self,val):
        self.top = None
        new_node = Node(val)
        self.top = new_node

    def push(self,val):
        new_node = Node(val)
        if self.top is None:
            self.top = new_node

        else:
            new_node.next = self.top
            self.top =  new_node

    def pop(self,data):
        n = self.top
        while n is not None:
            if n.val == data:
                self.top = self


    def print(self):
        n = self.top
        while n is not None:
            print(n.val)
            n = n.next

a1 = Stack(10)
a1.push(10)
a1.push(31)
a1.push(99)
a1.print()
a1.pop(31)
        