import csv

allScores = []


with open('PlayerSaves.csv') as dataFile:
    fileReader = csv.DictReader(dataFile)
    for row in fileReader:
        allScores.append([row['playerName'], row['SaveCode'], row['SlotNum']])


for x in range(len(allScores)):
    word = str(allScores[int(allScores[x][2])][0])
    print(word)

#    word = str(allScores[allScores[0][0][1]][0])
#    button(word, 585, (125 + (75 * 0)), 180, 60, ORANGE, PlayerInfo)
#    word = str(allScores[len(allScores) - (len(allScores) - 1)][0])
#    button(word, 585, (125 + (75 * 1)), 180, 60, ORANGE, PlayerInfo)
#    word = str(allScores[len(allScores) - (len(allScores) - 2)][0])
#    button(word, 585, (125 + (75 * 2)), 180, 60, ORANGE, PlayerInfo)

    print(allScores[x][1])
