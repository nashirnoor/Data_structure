# def count_elements(arr):
#     element_counts = {}
#     for element in arr:
#         if element in element_counts:
#             element_counts[element] += 1
#         else:
#             element_counts[element] = 1
#     return element_counts

# arr = [1, 2, 3, 4, 2, 3, 2, 1, 2, 4, 5]
# result = count_elements(arr)
# print(result) 


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

hash_table = HashTable(10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 7)
hash_table.insert("orange", 3)
hash_table.insert("grape", 2)

print(hash_table.get("apple"))  
print(hash_table.get("banana"))  
print(hash_table.get("orange"))  
print(hash_table.get("grape"))  

hash_table.remove("banana")
print(hash_table.get("banana"))  
