# dict1 = {"Age":11}
# dict2 = dict1
# dict2["Age"] = 20
# print(dict1,dict2)    



# head = {
#     "value":"Nashir",
#         "next":{
#             "value":'Ajmal',
#               "next":{
#                   "value":'Rayees',
#                   "next":None
#             }
#         }
#     }

# print(head['next']['next']['next'])


# def reverse(s):
#     if len(s)<=1:
#         return s
#     else:
#         return reverse(s[1:]) + (s[0])
    
# d = reverse("hello")
# print(d)



# def fabinocci(n):
#     if n<=1:
#         return n
#     else:
#         return fabinocci(n-1) + fabinocci(n - 2)
    
# d = fabinocci(11)
# print(d)


# from collections import Counter

# def char_count(n):
#     d = Counter(n)
#     new = []
#     for key,count in d.items():
#         if count==1:
#             new.append(key)
#     return new

# a = char_count("jandrewq")
# print(a)


arr = []
arr2 = []
for i in range(5):
    for j in range(1,3):
        arr.append(j)
    arr2.append(arr)

print(arr2)


