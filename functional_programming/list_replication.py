def solution_function(num1, *other_nums):
    """
    This python program solves the "List Replication" problem on
    HackerRank, but it stil needs to be translated to Racket.
    """

    for args in other_nums:

        for i in range(num1):
            print(args)


solution_function(3, 1, 2, 3, 4)
