'''
Link to the problem :-https://codeforces.com/contest/1734/problem/A

'''

#Solution of the Problem

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    t=999999999
    a.sort()
    for i in range(n-2):
        x=abs(a[i]-a[i+1])
        x+=abs(a[i+1]-a[i+2])
        t=min(t,x)
        c=0
    print(t)
