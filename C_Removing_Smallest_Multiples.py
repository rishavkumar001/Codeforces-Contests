'''
Link to the problem :-https://codeforces.com/contest/1734/problem/C

'''

#Solution of the Problem

for _ in range(int(input())):
    n=int(input())
    s=input()
    v=[0]*n
    res=0
    for i in range(1,n+1):
        j=i
        while j<n+1:
            if s[j-1]=='1':
                break
            if v[j-1]==0:
                v[j-1]=1
                res+=i
            j+=i
    print(res)