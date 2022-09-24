'''
Link to the problem :-https://codeforces.com/contest/1734/problem/E

'''

#Solution of the Problem

n=int(input())
l=list(map(int,input().split()))
i=0
while i<n:
    j=0
    while j<n:
        a=(j-i)*i
        b=l[i]%n+n
        print((a+b)%n,end=" ")
        j+=1
    print()
    i+=1