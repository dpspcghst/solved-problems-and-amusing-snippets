"""
This snippet will be studied to learn about concatenating integers within strings.
"""

inp_str = "can2you0see2this1"

print("Original String : " + inp_str)
num = ""
for c in inp_str:

    if c.isdigit():
        num = num + c

    else:

        pass

print("Extracted numbers from the list : " + num)
