# Question :  Problem Statement :

collections.Counter() 
A counter is container, where elements are stored as dictionary keys and their counts are stored as dictionary values.
[3, 4, 4, 2, 1]

Task :
Raghu is a shoe shop owner. His shop has X number of shoes. 
He has a list containing size of each shoe he has in his shop. 
There are N number of customers, who are willing to pay xi amount of money only if they get the shoe of their desired size.
Your task is to compute, how much money Raghu earned.

Input Format :
First line contains, X number of shoes. 
Second line contains, space separated size of the shoes. 
Third line contains, N number of customers. 
Next N line contain, space separated values of shoe size and xi price of shoe.

Constraints :
0<X<103 
0<N≤103 
20<xi<100 
2<shoe size<20

Output Format :
Print the amount of money earned by Raghu

# Answer :

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
X = int(input())
N = map(int,input().split())
x = int(input())
L = map(tuple,(map(int,input().split()) for _ in range(x)))
n = Counter(N)
p =0
for i in L:
    if i[0] in n.keys() and n[i[0]] >0 :
        n[i[0]] = n[i[0]]-1
        p = p+i[1]
          
print(p)
