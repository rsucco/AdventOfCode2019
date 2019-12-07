def testAdjacency(passwd):
    lastChar = -1
    for char in str(passwd):
        if char == lastChar:
            return True
        lastChar = char
    return False

def testDecrease(passwd):
    lastChar = 0
    for char in str(passwd):
        if int(char) < int(lastChar):
            return False
        lastChar = char
    return True


passwdFloor = 382345
passwdCeiling = 843167
passwdRange = range(passwdFloor, passwdCeiling + 1)

potentialPasswds = []
for passwd in passwdRange:
    if testAdjacency(passwd) and testDecrease(passwd):
        potentialPasswds.append(passwd)

print(len(potentialPasswds))
