N = int(input())
numList = list(map(int,input().split()))
for index in range(0,len(numList)):
    currval = numList[index]
    cmpIndex = index 
    while(cmpIndex>0 and numList[cmpIndex-1]>currval):
        numList[cmpIndex]=numList[cmpIndex-1]
        cmpIndex -= 1
        numList[cmpIndex]=currval
for index in range(N):
    print(numList[index],end=" ")