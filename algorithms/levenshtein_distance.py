def levenshtein(string1, string2):
    F = [[(i + j) if i * j == 0 else 0 for i in range(len(string2) + 1)] for j in range(len(string1) + 1)]
    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if string1[i - 1] == string2[j - 1]:
                F[i][j] = F[i - 1][j - 1]
            else:
                F[i][j] = 1 + min(F[i - 1][j - 1], F[i - 1][j], F[i][j - 1])
    return F[-1][-1]

def test_levenshtein():
    test1 = levenshtein("cat", "dog")
    test2 = levenshtein("cat", "cat")
    test3 = levenshtein("", "frog")
    test4 = levenshtein("satisfaction", "satisfactory")
    test5 = levenshtein("fact", "factories")
    if test1 == 3:
        print("Test #1. Success")
    else:
        print("Test #1. Failure")
    if test2 == 0:
        print("Test #2. Success")
    else:
        print("Test #2. Failure")
    if test3 == 4:
        print("Test #3. Success")
    else:
        print("Test #3. Failure")
    if test4 == 3:
        print("Test #4. Success")
    else:
        print("Test #4. Failure")
    if test5 == 5:
        print("Test #5. Success")
    else:
        print("Test #5. Failure")

test_levenshtein()