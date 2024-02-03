# def binary_search(arr,target,right,left):
#         if left>right:
#             return -1
    
#         mid = left + (right - left) // 2
         
#         if arr[mid] == target:
#            return mid
        
#         elif arr[mid]<target:
#             return binary_search(arr,target,right,mid+1)

#         else:
#             return binary_search(arr,target,mid-1,left)




# arr = [2,5,6,7,8,11,15,16,17,20]
# target = 20
# d = binary_search(arr,target,0,len(arr)-1)
# print(d)




def binary_search(arr,target,left,right):
    if left>right:
        return -1
    mid = left + (right - left)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binary_search(arr,target,mid+1,right)
    
    else:
        return binary_search(arr,target,left,mid-1)
    
target = 8
arr = [1,3,4,5,6,8,9,12]
d = binary_search(arr,target,0,len(arr)-1)
print(d)

























