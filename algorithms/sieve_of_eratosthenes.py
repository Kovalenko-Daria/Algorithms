def sieve_eratosthenes(n):
    """ The input data is a natural number greater than one.
        The function uses an algorithm to search for prime numbers
        from 2 to a given number inclusive and returns an array with them.
        In case of an input error, returns an error message.
    """
    if type(n) != int or n < 2:
        return "Error"
    array_num = [True] * (n + 1)
    array_num[0] = array_num[1] = False
    for i in range(2, n + 1):
        if array_num[i]:
            for j in range(i**2, n + 1, i):
                array_num[j] = False
    prime = []
    for i in range(2, n + 1):
        if array_num[i]:
            prime.append(i)
    return prime

def test_sieve_erat():
    test1 = sieve_eratosthenes(-2)
    test2 = sieve_eratosthenes("abc")
    test3 = sieve_eratosthenes(1)
    test4 = sieve_eratosthenes(2)
    test5 = sieve_eratosthenes(25)
    if test1 == "Error":
        print("Test #1. Success")
    else:
        print("Test #1. Failure")
    if test2 == "Error":
        print("Test #2. Success")
    else:
        print("Test #2. Failure")
    if test3 == "Error":
        print("Test #3. Success")
    else:
        print("Test #3. Failure")
    if test4 == [2]:
        print("Test #4. Success")
    else:
        print("Test #4. Failure")
    if test5 == [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        print("Test #5. Success")
    else:
        print("Test #5. Failure")

test_sieve_erat()