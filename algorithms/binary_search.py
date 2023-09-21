def binary_search(min_gr, max_gr):
    """ The input data is the minimum and maximum values at which the hidden number can be found. 
        The function outputs a possible number, after which it expects a comment from the user,
        regardless of whether it is "Greater" or "Less" than the guessed one.
        Guessing continues until the user enters the phrase "Got it!".
        Doesn't return anything.
    """
    guess = guess = (max_gr + min_gr) // 2 + (max_gr + min_gr) % 2
    print(guess)
    while (ans := input()) != "Got it!":
        if ans == "Less":
            max_gr = guess
        else:
            min_gr = guess
        guess = (max_gr + min_gr) // 2 + (max_gr + min_gr) % 2
        print(guess)

print("Enter the boundaries of guessing:")
min_b, max_b = [int(i) for i in input().split()]
binary_search(min_b, max_b)