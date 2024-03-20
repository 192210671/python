
def maxprofit(difficulty,profit,worker):
    jobs=sorted(zip(difficulty,profit))

    res,i,best=0,0,0

    for ability in sorted(worker):
        while i<len(jobs) and ability>=jobs[i][0]:
            best=max(jobs[i][1],best)
            i+=1
        res+=best
    return res       




difficulty=[2,4,6,8,10]
profit=[10,20,30,40,50]
worker=[4,5,6,7]

print(maxprofit(difficulty,profit,worker))
