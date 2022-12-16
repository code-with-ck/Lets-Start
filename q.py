def parttition(arr,low,high):
    pivot = arr[high]
    i =low-1
    st = low 
    end = high
    for j in range(st,end):
        if arr[j] < pivot :
            (arr[i],arr[j]) = (arr[j],arr[i])
            print(arr)
    i+=1 
    temp = arr[i]
    arr[i] = pivot
    arr[high] = temp
    # (arr[i],arr[high]) =(arr[high],arr[i])
    return i 
def quicksort(arr,low,high):
    if low < high :
        pidx = parttition(arr,high,low)
        quicksort(arr,low,pidx-1)
        quicksort(arr,pidx+1,high)

arr = [6,3,9,5,2,8]
n = 6
quicksort(arr,0,n-1)
print(arr)