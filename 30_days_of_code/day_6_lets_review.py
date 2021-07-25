# TODO: Break code into smaller functions.

word_count = int(input())

even_steven = ""
odd_todd = ""

for i in range(word_count):
    word = input()
    for u in range(len(word)):
        if (u % 2) == 0:
            even_steven = even_steven + word[u]
        
        else:
            odd_todd = odd_todd + word[u]

    print(f"{even_steven} {odd_todd}")
    even_steven = ""
    odd_todd = ""
