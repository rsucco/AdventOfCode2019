import sys

def getOrbitNumber(orbits):
    orbitNum = 0
    for orbit in orbits:
        orbitNum += 1
        while (orbits[orbit] != 'COM'):
            orbit = orbits[orbit]
            orbitNum += 1
    return orbitNum

def getOrbitsToSanta(orbits):
    # First, create an orbit map path for both us and Santa. This will map the number of 
    # transitions necessary to reach each object, with ourselves being -1, the object we 
    # orbit directly being 0, and each other object having the number of transitions.
    youOrbitNum = -1
    youOrbits = {}
    orbit = 'YOU'
    # Create our own orbit path
    while (orbit != 'COM'):
        youOrbits[orbit] = youOrbitNum
        orbit = orbits[orbit]
        youOrbitNum += 1
    sanOrbitNum = -1
    sanOrbits = {}
    orbit = 'SAN'
    # Create Santa's orbit path
    while (orbit != 'COM'):
        sanOrbits[orbit] = sanOrbitNum
        orbit = orbits[orbit]
        sanOrbitNum += 1

    # Create a list of each stop that both orbits share in common
    matchingStops = set(youOrbits.keys()) & set(sanOrbits.keys())

    # Find the matching stop that is the shortest total distance from both us and Santa
    shortestPath = sys.maxsize
    for stop in matchingStops:
        distance = youOrbits[stop] + sanOrbits[stop]
        if distance < shortestPath:
            shortestPath = distance

    return shortestPath
    


inputData = []
with open('./Day6Data.txt', 'r') as inputFile:
    for inputDatum in inputFile:
        inputData.append(inputDatum.replace('\n', ''))

# Create the dictionary of direct orbits
directOrbits = {}
for inputDatum in inputData:
    inputDatum = inputDatum.split(")")
    orbitee = inputDatum[0]
    orbiter = inputDatum[1]
    directOrbits[orbiter] = orbitee


print ("Total number of direct and indirect orbits: " + str(getOrbitNumber(directOrbits)))
print ("Total orbital transfers betwixt us and Santa: " + str(getOrbitsToSanta(directOrbits)))
