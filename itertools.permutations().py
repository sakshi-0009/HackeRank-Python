# Question : You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

# Answer :

from itertools import permutations
s , n = input().split()

for i in list(permutations(sorted(s),int(n))):
    print(''.join(i))
