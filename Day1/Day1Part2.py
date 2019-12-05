def getAdditionalFuel(fuelAdded, totalFuel = 0):
    if totalFuel == 0:
        totalFuel = fuelAdded
    fuelToAdd = fuelAdded // 3 -2
    if (fuelToAdd <= 0):
        return totalFuel
    else:
        totalFuel += fuelToAdd
        return getAdditionalFuel(fuelToAdd, totalFuel)

totalFuel = 0
inputData = []
with open('./Day1Data.txt', 'r') as inputFile:
    for inputDatum in inputFile:
        inputData.append(inputDatum.replace('\n', ''))

for moduleMass in inputData:
    totalFuel += getAdditionalFuel(int(moduleMass) // 3 - 2)

print(totalFuel)
