for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans=[l[0]]
    flag=0
    for i in range(1,n):
        if l[i]==0 or l[i]>=ans[i-1]:
            ans.append(abs(l[i]+ans[i-1]))
        else:
            print(-1)
            flag=1
            break
    if flag==0:
        for i in ans:
            print(i,end=" ")
        print()