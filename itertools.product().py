# Question : You are given a two lists A and B. Your task is to compute their cartesian product AXB.
Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.
Output Format :
Output the space separated tuples of the cartesian product.

# Answer :  

# itertools.product() in Python - Hacker Rank Solution
# Enter your code here. Read input from STDIN. Print output to STDOUT
# itertools.product() in Python - Hacker Rank Solution START
from itertools import product
A = input().split()
A = list(map(int,A))
B = input().split()
B = list(map(int, B))
output = list(product(A,B))
for i in output:
    print(i, end = " ");
# itertools.product() in Python - Hacker Rank Solution END
