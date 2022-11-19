# Queston : Consider the following:

A string, s, of length n where s = c0c1. . . . cn-1.

An integer, k, where k is a factor of n.


We can split s into n/k substrings where each subtring, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

The characters in ui are a subsequence of the characters in ti.

Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index < j in ti, then do not include the character in string ui.

Given s and k, print n/k lines where each line i denotes string ui.
Print each subsequence on a new line. There will be n/k of them. No return value is expected.

Input Format
The first line contains a single string, s.

The second line contains an integer, k, the length of each substring.

# Answer :

def merge_the_tools(string, k):
    # your code goes here
    temp = []
    len_temp = 0
    for item in string:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            print (''.join(temp))
            temp = []
            len_temp = 0
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
