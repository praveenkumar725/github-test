# A nonprime number N is passed as the input to the program. The program must print the first three factors of N as the output.


N=int(input())
factorcount,ctr=0,1
while factorcount<3:
    if N%ctr==0:
        print(ctr,end=" ")
        factorcount+=1
    ctr+=1    





