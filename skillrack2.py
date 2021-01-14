# Five integers are passed as the input to the program. The program must print the count of odd integers as the output

mylist=list(map(int,input().strip().split()))
oddcount=0
for i in mylist:
    if i%2!=0:
        oddcount+=1
print("the count",oddcount)            


