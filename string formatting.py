# Question : Given an integer,n, print the following values for each integer i from 1 to n:
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

# Answer :

def print_formatted(number):

    width = len("{0:b}".format(number))

    for i in range(1, number + 1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
