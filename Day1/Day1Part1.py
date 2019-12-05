
totalFuel = 0
inputData = []
with open('./Day1Data.txt', 'r') as inputFile:
    for inputDatum in inputFile:
        inputData.append(inputDatum.replace('\n', ''))

for moduleMass in inputData:
    totalFuel += int(moduleMass) // 3 - 2

print (totalFuel)
