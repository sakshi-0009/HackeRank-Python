# Question : Kevin and Stuart want to play the 'The Minion Game'.

Game Rules
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring -
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Input Format :
A single line of input containing the string S.
Note: The string S will contain only uppercase letters:[A - Z] .

Constraints :
0 < len(s) <= 10^6

Output Format :
Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.

# Answer :

def minion_game(string):
    # your code goes here
    player1 = 0;
    player2 = 0;
    str_len = len(string)
    for i in range(str_len):
        if s[i] in "AEIOU":
            player1 += (str_len)-i
        else :
            player2 += (str_len)-i
    
    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart",player2)
    elif player1 == player2:
        print("Draw")
    else :
        print("Draw")
    # The Minion Game in Python - Hacker Rank Solution END
if __name__ == '__main__':
    s = input()
    minion_game(s)
