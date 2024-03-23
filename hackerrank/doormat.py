def design(n,m):
    for i in range(n//2):        #0 to 5
        pattern=".|."*(2*i+1)
        print(pattern.center(m,'-'))

    print("Welcome".center(m,'-'))  


    for i in range(n//2-1,-1,-1):
        pattern=".|."*(2*i+1)
        print(pattern.center(m,'-'))  










n,m=map(int,input().split())
design(n,m)
