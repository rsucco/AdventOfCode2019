# Writing this comment because I did not comment this one at all. I promise I write better comments elsewhere.
import numpy as np

def testAdjacency(passwdInt):
    indices = []
    passwd = np.array([int(i) for i in str(passwdInt)])
    for char in range(10):
        indices = np.where(passwd == char)[0]
        if len(indices) > 1:
            for index in range(1,5):
                if (passwd[index] == passwd[index - 1] and (index == 1 or passwd[index] != passwd[index - 2]) and passwd[index] != passwd[index + 1]) or \
                    (passwd[index] == passwd[index + 1] and (index == 4 or passwd[index] != passwd[index + 2]) and passwd[index] != passwd[index - 1]):
                    return True
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
