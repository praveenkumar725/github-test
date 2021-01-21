N=int(input())
S=list(map(int,input().split()))
for i in range(len(S)):
   M=i 
   for j in range(i+1,len(S)):
       if S[j]>S[M]:
          M=j 
   if M != i:
        S[i],S[M]=S[M],S[i]
for i in range(N):
    print("%d" %S[i],end=" ")