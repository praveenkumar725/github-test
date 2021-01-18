#  The program must accept three integers X, Y and Z as the input. Two of these three integers will have same unit digit. 
#  The program must the print smallest integer among the integers which are having the same unit digit.
#  Then the program must print the largest integer among the integers which are having the same unit digit.
#  Finally, the program must print the remaining integer as the output.



X,Y,Z=map(int,input().split())
if X%10 == Y%10:
    print(min(X, Y), max(X, Y), Z)
elif Y%10 == Z%10:
    print(min(Y, Z), max(Y, Z), X)
elif X%10 == Z%10:
    print(min(X, Z), max(X, Z), Y)





