# Question : Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.You are given  scores. Store them in a list and find the score of the runner-up.

# Answer :
# Python Program Code :

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    playersList=list(arr)
    playersList.sort(reverse=True)
    dubleList=[]
    for element in playersList:
        if playersList.count(element)>1:
            dubleList.append(element)
    for element in dubleList:
        if playersList.count(element)>1:
            playersList.remove(element)
    placeInGame=2     
    print(playersList[placeInGame-1])
