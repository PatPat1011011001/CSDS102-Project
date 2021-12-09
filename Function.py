def myVariance():
    N=int(input())
    Q=[float(x) for x in input() .split()]
    
    m=sum(Q)/N
    s=sum((Q-m)**2)
    print(s)




myVariance()