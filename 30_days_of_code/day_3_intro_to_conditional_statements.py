"""
Objetcive: In this challenge, we learn about conditional statements. Check
out the Tutorial tab for learning materials and an instructional video.
"""

"""
Task: given an integer, n, perform the following conditional actions: if n
is odd, print Weird. If n is even and in the inclusive range of 2 to 5,
print Not Weird. If n is even and in the inclusive range of 6 to 20, print
Weird. If n is even and greater than 20, print Not Weird. Complete the stub
code provided in your editor to print whether or not  is weird.
"""


def assess_number(number):
    """
    """

    if number % 2 != 0:
        print("Weird")

    elif number % 2 == 0:
        if 1 < number < 6:
            print("Not Weird")

        elif 5 < number < 21:
            print("Weird")

        elif 20 < number:
            print("Not Weird")

        else:
            pass

    else:
        pass
