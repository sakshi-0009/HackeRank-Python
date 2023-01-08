''' Question :- Print the average marks of the list corrected to 2 decimal places.'''

# Answer :-

N, headers, total = int(input()), list(input().split()), 0
for _ in range(N):
    total += int(list(input().split())[headers.index('MARKS')])
print(total/N)
