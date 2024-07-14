
if __name__ == '__main__':
    details = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        details.append([name, score])
    
    scoreLst = []

    for name, score in details:
        scoreLst.append(score)

    scoreLst.sort(reverse=True)
    uniqueScores = [item for index, item in enumerate(scoreLst) if item not in scoreLst[:index]]
    secHighest = uniqueScores[-2]
    print(secHighest)
    runnerUps = [name for [name, score] in details if score == secHighest]
    
    runnerUps.sort()
    print(runnerUps)
    for name in runnerUps:
        print(name)
        

            

    
