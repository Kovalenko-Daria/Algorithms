def KMP(string, sub):
    new_string = sub + '#' + string
    enter = []
    Pr = [0] * (len(new_string) + 1)
    for i in range(len(new_string)):
        p = Pr[i]
        while p > 0 and new_string[i] != new_string[p]:
            p = Pr[p - 1]
        if new_string[i] == new_string[p] and p != i:
            p += 1
        Pr[i + 1] = p
        if p == len(sub):
            enter.append(i - 2 * len(sub))
    return enter

def test_KMP():
    test1 = KMP("blablab", "b")
    test2 = KMP("string", "stw")
    test3 = KMP("", "gh")
    test4 = KMP("some_long_string", "ng")
    test5 = KMP("abcdghef", "abcdf")
    if test1 == [0, 3, 6]:
        print("Test #1. Success")
    else:
        print("Test #1. Failure")
    if test2 == []:
        print("Test #2. Success")
    else:
        print("Test #2. Failure")
    if test3 == []:
        print("Test #3. Success")
    else:
        print("Test #3. Failure")
    if test4 == [7, 14]:
        print("Test #4. Success")
    else:
        print("Test #4. Failure")
    if test5 == []:
        print("Test #5. Success")
    else:
        print("Test #5. Failure")


test_KMP()