S = str(input())

alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in alp:
    if i in S:
        print(S.index(i),end=" ")
    else:
        print(-1,end=" ")

