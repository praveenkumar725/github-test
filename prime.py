
# Python3 program to display first N Prime numbers
 

def prime(limit):
    for i in range(0,limit+1):
        if i>1:
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                print(i,end=" ")
N=int(input("enter a number:"))
prime(N)                