
arr = [3,1,7,6,9,10,12,15,22,8,71,43]
for i in range(len(arr)):
    min = arr[i]
    for j in range(i,len(arr)):
        if arr[j]<min:
            min = arr[j]
            arr[i],arr[j] = arr[j],arr[i]

print(arr)