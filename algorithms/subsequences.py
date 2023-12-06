def lcs(a, b):
    F = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    return F[len(a)][len(b)]

def gis(a):
    F = [0] * (len(a) + 1)
    for i in range(1, len(a) + 1):
        m = 0
        for j in range(1, i):
            if a[i - 1] > a[j - 1] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    return F[len(a)]


def test_lcs():
    test1 = lcs("ABCDE", "BAhjCDBLPCD")
    test2 = lcs("643782", "BAhjCDBLPCD")
    test3 = lcs("", "")
    test4 = lcs("ABCDE", "")
    test5 = lcs("Km^r5", "efuyewyferjkl5")
    if test1 == 4:
        print("Test #1. Success")
    else:
        print("Test #1. Failure")
    if test2 == 0:
        print("Test #2. Success")
    else:
        print("Test #2. Failure")
    if test3 == 0:
        print("Test #3. Success")
    else:
        print("Test #3. Failure")
    if test4 == 0:
        print("Test #4. Success")
    else:
        print("Test #4. Failure")
    if test5 == 2:
        print("Test #5. Success")
    else:
        print("Test #5. Failure")

def test_gis():
    test1 = gis("HGABVSXDCCCCEAAAFAAAG")
    test2 = gis("gfedcba")
    test3 = gis("")
    test4 = gis("abc78990dglmn")
    test5 = gis("byrf12345")
    if test1 == 6:
        print("Test #1. Success")
    else:
        print("Test #1. Failure")
    if test2 == 1:
        print("Test #2. Success")
    else:
        print("Test #2. Failure")
    if test3 == 0:
        print("Test #3. Success")
    else:
        print("Test #3. Failure")
    if test4 == 8:
        print("Test #4. Success")
    else:
        print("Test #4. Failure")
    if test5 == 5:
        print("Test #5. Success")
    else:
        print("Test #5. Failure")

print("Tests for lcs")
test_lcs()

print("Tests for gis")
test_gis()