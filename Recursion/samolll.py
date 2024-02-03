def binary_search(arr,find,left,right):
    mid = left + (right - left)//2
    if left<right:
        if arr[mid]== find:
            return mid
        elif arr[mid]>left:
            return binary_search(arr,find,mid+1,right)
        else:
            return binary_search(arr,find,left,mid-1)



arr = [1,3,4,5,6,7,19,20]
find = 19
left = 0
d = binary_search(arr,find,0,len(arr))
print(d)