def check_bracket_sequence(seq):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for i in seq:
        if i in pairs.values():
            stack.append(i)
        else:
            if len(stack) and stack[-1] == pairs[i]:
                stack.pop()
            else:
                stack.append('(')
                break
    if len(stack) == 0:
        return True
    return False


def test_check_bracket_sequence():
    test1 = check_bracket_sequence("(((){}")
    test2 = check_bracket_sequence("{}(){((()))}([)]")
    test3 = check_bracket_sequence("({[([[]])]})")
    test4 = check_bracket_sequence("(((}}}")
    test5 = check_bracket_sequence("[")
    if not test1:
        print("Test #1. Success")
    else:
        print("Test #1. Failure")
    if not test2:
        print("Test #2. Success")
    else:
        print("Test #2. Failure")
    if test3:
        print("Test #3. Success")
    else:
        print("Test #3. Failure")
    if not test4:
        print("Test #4. Success")
    else:
        print("Test #4. Failure")
    if not test5:
        print("Test #5. Success")
    else:
        print("Test #5. Failure")

test_check_bracket_sequence()