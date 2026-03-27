print("welcome to algoritms!!! help book is  Grokking algoritms \n by Aditya Bhargava")


def theme(name):
    return f"Theme is {name}"

focus = theme("to introduction algorithms")
print(focus)
# BOOK code
# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#     while low <= high:
#         mid = (low + high)
#         guess = list[mid]
#         if guess == item:
#             return mid    # medium element
#         if guess > item:  # guess need element
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
# my_list = [1, 3, 5, 7, 9]

# print ( binary_search(my_list, 3)) # => 1
# print (binary_search(my_list, - 1)) # => None

# my code
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target1 = 70
target2 = 60
target3 = 1

def binary_search(list, item):
    low = 0                            #started index 
    high = len(list) - 1               # finish index
    while low <= high:                  # sikl continue if low smaller high
        medium = (low + high) // 2      # medium index
        need_num = list[medium]         # item equal of need number
        if need_num == item:
            return medium               # medium number is true
        if need_num > item:             # 1 2 3 4 5  need num = 2, medium = 3 , low = 0 and high = 2
            high = medium - 1
        else:
            low = medium + 1             # etc
    return None
my_list = numbers

print(binary_search(my_list, target1))
print(binary_search(my_list, target2))
print(binary_search(my_list, target3))

