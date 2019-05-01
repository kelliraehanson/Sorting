# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    # merged_arr = [0] * elements
    # a = 0
    # b = 0

# In class example:
# def merge(arrA, arrB):

#   elements = len(arrA) + len(arrB)
#   merged_arr = [0] * elements

#   a = 0
#   b = 0



    # TO-DO
    while len(arrA) > 0 and len(arrB) > 0:
      smallest = min(arrA[0], arrB[0])
      if smallest == arrA[0]:
        arrA.pop(0)
        merged_arr.append(smallest)
      else:
        arrB.pop(0)
        merged_arr.append(smallest)
    if len(arrA) > 0:
      for i in arrA:
        merged_arr.append(i)
    else:
      for i in arrB:
        merged_arr.append(i)
    
    # print(merged_arr)
    print(f'The Recursive Sort is: {merged_arr}')
    
    return merged_arr

# In class example:
#    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
#   for i in range( 0, elements ):
#         if a >= len(arrA):    # all elements in arrA have been merged
#             merged_arr[i] = arrB[b]
#             b += 1
#         elif b >= len(arrB):  # all elements in arrB have been merged
#             merged_arr[i] = arrA[a]
#             a += 1
#         elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
#             merged_arr[i] = arrA[a]
#             a += 1
#         else:  # else, next element in arrB must be smaller, so add it to final array
#             merged_arr[i] = arrB[b]
#             b += 1
#   return merged_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        left = merge_sort(arr[0:int(len(arr)/2)])
        right = merge_sort(arr[int(len(arr)/2):])
        arr = merge(left, right)

    return arr

merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])

# In class example:
# def merge_sort(arr):
# # 1. While your data set contains more than one item, split it in half
#   if (len(arr) > 1):
#     left = merge_sort(arr[0: int(len(arr)/2)])
#     right = merge_sort(arr[int(len(arr)/2):])
# # 2. Once you have gotten down to a single element, you have also *sorted* that element 
# #    (a single element cannot be "out of order")
# # 3. Start merging your single lists of one element together into larger, sorted sets
#     arr = merge(left, right)  # haven't defined merge is? 
# # 4. Repeat step 3 until the entire data set has been reassembled
#   return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
