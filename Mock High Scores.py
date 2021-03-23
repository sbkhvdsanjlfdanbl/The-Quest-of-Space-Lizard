import csv

allScores = []
with open('High Scores.csv') as dataFile:
    fileReader = csv.DictReader(dataFile)
    for row in fileReader:
        allScores.append([row['PLAYER'] ,row['SCORE']])

allScores = sorted(allScores, key = lambda x: int(x[1]), reverse=True)
for i in range(len(allScores)):
    print(allScores[i])

    
