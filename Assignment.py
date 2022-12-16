# 1 .Reverse an array
# l = [1,2,3,4,5,6,7]
# n = 7
# f = 0
# s = n-1
# while f<=s:
#     t = l[f]
#     l[f] = l[s]
#     l[s] = t
#     f+=1
#     s-=1
# print(l)

# 2 Find the mean, median, and mode in an array

# def mmm(array):
#    l = 0
#    sum = 0

#    for i in array:
#        l += 1
#        sum += i
#    print("Mean of array")
#    mi = sum//l
#    print(array[sum//l])

#    for i in range(l):
#        for j in range(0, l-1):
#            if array[i] < array[j]:
#                t = array[i]
#                array[i] = array[j]
#                array[j] = t

#    print("Median of array : - ")
#    if l % 2 != 0:
#        print((l+1)//2)
#        me = (l+1)//2
#    else:
#        me = l//2+(l//2+1)//2
#        print(l//2+(l//2+1)//2)

#    print("Mode of array")
#    print(3*me-2*mi)

# array = [2, 3, 4, 5, 6, 7, 2, 8, 7, 8, 9]
# mmm(array)

# 3 Find duplicate elements in an array

# def duplicate(array,l):
#    for i in range(l):
#        for j in range(i+1,l):
#            if array[j] == array[i] :
#                print(array[i])

# arr = [1,2,4,5,6,2,1]
# n = 7
# duplicate(arr,n)

# 4 .Merge two sorted arrays into a single sorted array

# arr1 = [1,2,3,4]
# arr2 = [5,6,7,8]
# arr1+=arr2
# print(arr1)


# 5 Given an unsorted array of size N that contains only non-negative integers,
# find a contiguous subarray that adds to a given number S. In case of multiple subarrays, 
# return the subarray which comes first on moving from left to right. Eg, let us say the array is - 3, 6, 7, 5, 10. And 
# the value of S = 12. The output should be - 7, 5


# def sum_from_arr(arr, k, l):
#     tup = tuple()
#     for i in range(l-1):
#         for j in range(i+1, l):
#             if arr[i]+arr[j] == k:
#                 li = [tuple([arr[i], arr[j]])]
#                 tup += tuple(li)
#     return tup 


# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# n = 8
# k = int(input("Enter the number__: "))
# a = sum_from_arr(arr, k, n)
# print(a)


# 6 Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.

# def Solution(arr,n):
#    # If length of array is even
#    if n % 2 == 0:
#        z = n // 2
#        e = arr[z]
#        q = arr[z - 1]
#        ans = (e + q) // 2
#        return ans
       
#    # If length of array is odd
#    else:
#        z = n// 2
#        ans = arr[z]
#        return ans
 
# arr1 = [1,-2,-5,3,6,9]
# l1 = 6
# arr2 = [9,-4,-2,7,4,5,8]
# l2 = 7 
 
 
# arr3 = arr1+arr2
# bothLength = l1+l2
# # sorting the array 
# for i in range(bothLength):
#        for j in range(0, bothLength-1):
#            if arr3[i] < arr3[j]:
#                t = arr3[i]
#                arr3[i] = arr3[j]
#                arr3[j] = t
# result = Solution(arr3,bothLength)
# print("MEDIAN = ",result)

# 7. Find a number using Binary Search in a sorted array 

# def sorting(Sorted,l):
#     for i in range(l):
#         for j in range(0,l-1):
#             if Sorted[i] > Sorted[j] :
#                 t = Sorted[i]
#                 Sorted[i] = Sorted[j]
#                 Sorted[j] = t 
#     return Sorted

# position = 0
# def Binary_search(arr,l,number):
#     global position
#     u = 0 
#     last = l-1 
#     while u<= last:
#         midIndex = (u+l)//2 
#         if arr[midIndex] == number:
#             position = midIndex 
#             return True
#         else:
#             if arr[midIndex]> number:
#                 u = midIndex
#             else:
#                 last = midIndex

# arr = [10,7,3,5,30,45]
# n = 6
# number = int(input("enter the number__:"))

# final_arr = sorting(arr,n)

# if Binary_search(final_arr,n,number):
#     print("The position of number is ",position)
# else:
#     print("Not found")




# bubbleSort  


def sorting(Sorted,l):
    for i in range(l):
        for j in range(0,l-1):
            if Sorted[i] < Sorted[j] :
                t = Sorted[i]
                Sorted[i] = Sorted[j]
                Sorted[j] = t 
    return Sorted

arr = [10,7,3,5,30,45]
n = 6
final_arr = sorting(arr,n)
print("sorted Array : -",final_arr)