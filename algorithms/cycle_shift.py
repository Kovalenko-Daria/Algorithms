def cycle_shift(array, n):
    """ The input data is an array and integer.
        The function performs a shift to the left with a positive parameter n 
        and a shift to the right if a negative number is passed.
        Returns modified array.
        In case of an input error, returns an error message.
    """
    if type(array) != list or type(n) != int:
        return "Error"
    if n > 0 and len(array):
        for i in range(n):
            first = array[0]
            for j in range(1, len(array)):
                array[j - 1] = array[j]
            array[len(array) - 1] = first
    elif n < 0 and len(array):
        for i in range(abs(n)):
            last = array[-1]
            for j in range(len(array) - 1, 0, -1):
                array[j] = array[j - 1]
            array[0] = last
    return array

def test_cycle_shift():
    test1 = cycle_shift("ddf", 5)
    test2 = cycle_shift([2], [3, 4])
    test3 = cycle_shift(['a', 'b', 'c', 'd'], 3)
    test4 = cycle_shift([5, 7, 3, 4, 2, 5], -2)
    test5 = cycle_shift([1, 2, 3], 0)
    test6 = cycle_shift([3, 5, 6, 7], 9)
    test7 = cycle_shift([], 25)
    if test1 == "Error":
        print("Test #1. Success")
    else:
        print("Test #1. Failure")
    if test2 == "Error":
        print("Test #2. Success")
    else:
        print("Test #2. Failure")
    if test3 == ['d', 'a', 'b', 'c']:
        print("Test #3. Success")
    else:
        print("Test #3. Failure")
    if test4 == [2, 5, 5, 7, 3, 4]:
        print("Test #4. Success")
    else:
        print("Test #4. Failure")
    if test5 == [1, 2, 3]:
        print("Test #5. Success")
    else:
        print("Test #5. Failure")
    if test6 == [5, 6, 7, 3]:
        print("Test #6. Success")
    else:
        print("Test #6. Failure")
    if test7 == []:
        print("Test #7. Success")
    else:
        print("Test #7. Failure")

test_cycle_shift()