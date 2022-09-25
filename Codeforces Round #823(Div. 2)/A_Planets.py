for _ in range(int(input())):
    n,c=map(int,input().split())
    a=list(map(int,input().split()))
    d={}
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    ans=0
    for i in d:
        if d[i]>c:
            ans+=c
        else:
            ans+=1*d[i]
    print(ans)