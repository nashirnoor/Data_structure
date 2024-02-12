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
