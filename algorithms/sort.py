def insert_sort(array):
    for i in range(1, len(array)):
        j = i
        while j != 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array

def choice_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(1, len(array) - i):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]
    return array

def fast_sort(array):
    if len(array) == 0 or len(array) == 1:
        return array
    elem = array[0]
    return fast_sort([i for i in array if i < elem]) + [i for i in array if i == elem] + fast_sort([i for i in array if i > elem])  

def merge_arrays(a, b):
    c = []
    while a and b:
        if a[0] > b[0]:
            c.append(b[0])
            b = b[1:]
        else:
            c.append(a[0])
            a = a[1:]
    if len(a) == 0:
        c += b[:]
    elif len(b) == 0:
        c += a[:]
    return c

def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return array
    return merge_arrays(merge_sort(array[:len(array) // 2]), merge_sort(array[len(array) // 2:]))

def test_sorts():
    sorts = [insert_sort, choice_sort, bubble_sort, fast_sort, merge_sort]
    names = ["insert_sort", "choice_sort", "bubble_sort", "fast_sort", "merge_sort"]
    for function in sorts:
        print("Tests for function", names[sorts.index(function)])
        test1 = function([])
        test2 = function([1])
        test3 = function([3, 3, 3, 3, 3, 3, 3])
        test4 = function([78, 93, 21, -45, 0, -23, 8])
        test5 = function([4, 6, 7, 3, 0, -2, -5, -32, 5, 3, 6, 3, 2, 0, 4])
        if test1 == []:
            print("Test #1. Success")
        else:
            print("Test #1. Failure")
        if test2 == [1]:
            print("Test #2. Success")
        else:
            print("Test #2. Failure")
        if test3 == [3, 3, 3, 3, 3, 3, 3]:
            print("Test #3. Success")
        else:
            print("Test #3. Failure")
        if test4 == [-45, -23, 0, 8, 21, 78, 93]:
            print("Test #4. Success")
        else:
            print("Test #4. Failure")
        if test5 == [-32, -5, -2, 0, 0, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7]:
            print("Test #5. Success")
        else:
            print("Test #5. Failure")
        print()

test_sorts()