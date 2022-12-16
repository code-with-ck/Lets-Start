# # 1. Mean, Median, mode: -


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
#    # print(array)
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


# #2. Buble sort: -
# def len_of_array(a):
#    l = 0
#    for i in a:
#        l+=1
#    return l
 
# array = [-2, 45, 0, 11, -9]
# l = len_of_array(array)
 
# for i in range(l):
#        for j in range(0, l-1):
#            if array[i] < array[j]:
#                t = array[i]
#                array[i] = array[j]
#                array[j] = t
# print(array)

# #3. Merge two sorted arrays into a single sorted array 

# arr1 = [1,2,3,4,5,6]
# arr2 = [7,8,9,10]
# arr1+=arr2
# print(arr1)



# #5. Find duplicate elements in an array
# def len_of_arr(arr):
#    c = 0
#    for i in arr:
#        c+=1
#    return c
 
 
# array = [1,2,3,4,5,3,2,24,6,4]
# l = len_of_arr(array)
 
# def duplicate(array):
#    for i in range(l):
#        for j in range(i+1,l):
#            if array[j] == array[i] :
#                print(array[i])
# duplicate(array)





# #6. Given an unsorted array of size N that contains only non-negative integers, find a contiguous subarray that adds to a given number S. In case of multiple subarrays, return the subarray which comes first on moving from left to right. Eg, let us say the array is - 3, 6, 7, 5, 10. And the value of S = 12. The output should be - 7, 5
 
# def len_of_arr(arr):
#   c = 0
#   for i in arr:
#       c+=1
#   return c
# def sum_from_arr(arr,k,l):
#   em_list =[]
#   for i in range(l-1):
#       for j in range(i+1,l):
#           if arr[i]+arr[j] == k:
#               li=[arr[i],arr[j]]
#               em_list+=li
#   return em_list
# arr = [1,2,3,4,5,6,7,8]
# l = len_of_arr(arr)
# k = int(input("Enter the number__: "))
# a = sum_from_arr(arr,k,l)
# print(a)
 


# #7 Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# def len_of_array(a):
#    l = 0
#    for i in a:
#        l+=1
#    return l
 
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
# arr2 = [9,-4,-2,7,4,5,8]
 
 
# arr3 = arr1+arr2
# l = len_of_array(arr3)
# for i in range(l):
#        for j in range(0, l-1):
#            if arr3[i] < arr3[j]:
#                t = arr3[i]
#                arr3[i] = arr3[j]
#                arr3[j] = t
# result = Solution(arr3,l)
# print("MEDIAN = ",result)
 



# # Find the number of position using binary search : - 

# def len_of_array(a):
#   l = 0
#   for i in a:
#       l+=1
#   return l
 
# def bubbleSort(array,l):
#    for i in range(l):
#        for j in range(0, l-1):
#            if array[i] < array[j]:
#                t = array[i]
#                array[i] = array[j]
#                array[j] = t
#    return array
 
# post = 0
# # def Bin_search(arr,nA



def fun1(i):
    if i> 10 :
        return 0 
    else:
        print(i)
        fun1(i+1)
fun1(1)