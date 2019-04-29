# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
             


        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp


    return arr

new_arr = [1,7,1,4,2,3,8,5]
# print(selection_sort(new_arr))
print(f'The Selection Sort is: {selection_sort(new_arr)}')
# print(selection_sort([1,7,1,4,2,3,8,5]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
   
    while True is True: 
        swapped = False 
        for i in range(1, len(arr)): 
            if arr[i - 1] > arr[i]: 
                temp = arr[i] 
                arr[i] = arr[i-1] 
                arr[i-1] = temp 
                swapped = True 
        if swapped == False:
            break

    return arr

# print(bubble_sort(new_arr))
print(f'The Bubble Sort is: {bubble_sort(new_arr)}')
# print(bubble_sort([1,7,1,4,2,3,8,5]))


# Insertion Sort from class

# class Book:
#     # """A simple Book class"""
#     # title = "title"
#     # author = "last, first"
#     # genre = "fiction"

#   def __init__(self, title, author, genre):
#     self.title = title
#     self.author = author
#     self.genre = genre

#   def __repr__(self):
#         return str(self.genre) + ": " + str(self.title) + " by " + str(self.author)

# harryPotter = Book('harry Potter', 'jkrowling', 'magic')
# mobydick = Book('Moby Dick', 'Herman Melville', 'fiction')
# awesomebook = Book("Awesome Book", "Awesome Dude", "Romance")
# dirk = Book("Dirk Gently's Holistic Detective Agency", "Adams, Douglas", "fiction")

# books = []

# books.append(harryPotter)
# books.append(mobydick)
# books.append(awesomebook)
# books.append(dirk)

# print(books)

#   # Description of the Insertion Algorithm
#     # Insertion Sort is an in-place algorithm, meaning that it does not require any additional memory to perform the sort operation.

#     # Sorting by Genre
# def insertion_sort_books(books):

#   # It works by conceptually dividing the array into sorted and unsorted pieces.
#     # 1. Consider element at index 0 to be our sorted piece. The rest of the array is our unsorted piece.
#       for i in range(1, len(books)):
#       # 2. Save the 1st element in the unsorted piece in a temp variable.
#         temp = books[i]
#         j = i
#         # 3. Shift elements in the sorted piece over to the right until we find where the element from step 2 should go.
#         while j > 0 and temp.genre < books[j-1].genre:
#         # 4. Insert the element from step 2 into its correct index within the sorted piece.
#           books[j] = books[j-1]
#           j-=1
#         books[j] = temp
#         # 5. Repeat steps 2-4 until all elements have been processed.

#       return books

# print(insertion_sort_books(books))

# def insertion_sort( arr ):
#   # loop through n-1 elements
#   for i in range(1, len(arr)):
#     temp = arr[i]
#     j = i
#     while j > 0 and temp < arr[j - 1]:
#       # shift left until correct position found
#       arr[j] = arr[j - 1]
#       j -= 1
#     # insert at correct position
#     arr[j] = temp

#   return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr