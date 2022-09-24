'''
Link to the problem :-https://codeforces.com/contest/1734/problem/B

'''

#Solution of the Problem

for _ in range(int(input())):
    n=int(input())
    for i in range(1,n+1):
        for j in range(1,i+1):
            if j==1 or j==i:
                print(1,end=" ")
            else:
                print(0,end=" ")
        print()