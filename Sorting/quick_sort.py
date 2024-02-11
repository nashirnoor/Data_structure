# def pivot(my_list, pivot_index, end_index):
#     swap_index = pivot_index

#     for i in range(pivot_index + 1, end_index):  
#         if my_list[i] < my_list[pivot_index]:
#             swap_index += 1
#             my_list[swap_index], my_list[i] = my_list[i], my_list[swap_index]

#     my_list[pivot_index], my_list[swap_index] = my_list[swap_index], my_list[pivot_index]
#     return swap_index

# my_list = [5, 3, 7, 8, 11, 10, 234, 1]
# a = pivot(my_list, 0, 7)
# print(my_list)

def pivot_place(list1,first,last):
    pivot = list1[first]
    l = first + 1
    r = last 
    while True:
        while l<=r and list1[l] <= pivot:
            l = l + 1
        while l<=r and list1[r] >= pivot:
            r = r -1
        if r<l:
            break
        else:
            list1[l],list1[r] = list1[r],list1[l]
    list1[first],list1[r] = list1[r],list1[first]
    return r
    

def quick_sort(list1,first,last):
    if first<last:
        p = pivot_place(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)

list1 = [56,34,21,76,54,90,65,12]
n = len(list1)
quick_sort(list1,0,n-1)
print(list1)
