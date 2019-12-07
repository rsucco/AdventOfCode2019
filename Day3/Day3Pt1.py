import csv
import sys

# Get the direction of a wire segment
def getDirection(wireCode):
    return wireCode[0]

# Get the length of a wire segment
def getLength(wireCode):
    return int(wireCode[1:])

# Returns a list of each unique X and Y coordinate that a given segment runs through
def getCoords(direction, length, X, Y):
    newCoords = []
    if direction == 'L':
        for coord in range(1, length + 1):
            newCoords.append([X - coord, Y])
    elif direction == 'R':
        for coord in range(1, length + 1):
            newCoords.append([X + coord, Y])
    elif direction == 'U':
        for coord in range(1, length + 1):
            newCoords.append([X, Y + coord])
    else:
        for coord in range(1, length + 1):
            newCoords.append([X, Y - coord])
    return newCoords
    
# Returns a 2D list with each value of the first dimension consisting of the X coordinate at index 0 and the Y coordinate at 1.
def getWireMap(wire):
    lastCoords = [0, 0]
    wireMap = []
    wireMap.append(lastCoords)
    for segment in range(len(wire[0])):
        nextCoords = (getCoords(wire[0][segment], wire[1][segment], lastCoords[0], lastCoords[1]))
        for nextCoord in nextCoords:
            wireMap.append(nextCoord)
        lastCoords = nextCoords[-1].copy()
    return wireMap

def getIntersections(wireMap1, wireMap2):
    intersections = list((set(map(tuple, wireMap1))) & set(map(tuple, wireMap2)))
    # Leaving this in as a good example of how NOT to compare lists. It worked, but took 10 minutes on a beefy computer.
    # The minor overhead of multiple castings to be able to bitwise-and the lists is far less than comparing them manually.
    #
    # intersections = []
    # for coord in wireMap1:
    #     if coord in wireMap2:
    #         intersections.append(coord)
    #         print("Found candidate: " + str(coord))
    intersections.remove((0,0))
    return intersections


# Read the data file and generate two seperate 2D lists for the two wires.
with open('./Day3Data.txt', 'r') as inputFile:
    fileReader = csv.reader(inputFile)
    wires = list(fileReader)
    wire1 = [list(map(getDirection, wires[0])),
             list(map(getLength, wires[0]))]
    wire2 = [list(map(getDirection, wires[1])),
             list(map(getLength, wires[1]))]

# Get XY mapping lists for the wires. X and Y are relative to the central port and are stored
# as lists inside of the wireMap lists, with X being index 0 and Y being index 1 in each given list.
wireMap1 = getWireMap(wire1)
wireMap2 = getWireMap(wire2)

# Get the coordinates of the points where the wires intersect, minus the central port
intersections = getIntersections(wireMap1, wireMap2)

# Get the closest intersection point to the central port out of the list of candidates
closest = [sys.maxsize, sys.maxsize]
for intersection in intersections:
    candidate = list(map(abs, intersection))
    if candidate[0] + candidate[1] < closest[0] + closest[1]:
        closest = candidate.copy()

print("Closest intersection to central port: " + str(closest))
print("Total distance: " + str(closest[0] + closest[1]))
