print("Selection sort")
print(
    '''
What you need to know
To understand the performance analysis bits in this chapter, you need to
know Big O notation and logarithms. If you don’t know those, I suggest
you go back and read chapter 1. Big O notation will be used throughout
the rest of the book.
'''
)

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
# Stores the smallest value
# Stores the index of the smallest value
# Now you can use this function to write selection sort:
print(findSmallest([4, 5, 6, 7, 8]))


def selectionSort(arr):
# Sorts an array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
# Finds the smallest element in the
        newArr.append(arr.pop(smallest))    # array, and adds it to the new array
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))