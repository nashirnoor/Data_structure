def swap(my_list, index1, index2):
    my_list[index1],my_list[index2] = my_list[index2],my_list[index1]


def pivot(my_list,pivot_index,end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1,end_index+1):
        if my_list[i]<my_list[pivot_index]:
            swap_index+=1
            swap(my_list,swap_index,i)
    swap(my_list,pivot_index,swap_index)
    return swap_index

my_list = [5,3,7,8,11,10,234,1]
a = pivot(my_list,0,7)
print(a)
print(my_list)












































# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[0] 
#     left = []
#     right = []
    
#     for i in range(1, len(arr)):
#         if arr[i] < pivot:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
    
#     return quicksort(left) + [pivot] + quicksort(right)


# arr = [6, 2, 8, 1, 5, 10, 120, 22, 23]
# print("Original array:", arr)
# sorted_arr = quicksort(arr)
# print("Sorted array:", sorted_arr)
