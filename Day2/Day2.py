import csv

# Compile a given intcode program with the specified noun and verb, and return its output (number in position 0)
def compileIntcode(intcodeProgram, noun, verb):
    # Set the noun and verb in the program
    intcodeProgram[1] = noun
    intcodeProgram[2] = verb

    # Iterate through all the values in the opcode memory addresses
    for instructionAddress in range(0, len(intcodeProgram), 4):
        opcode = intcodeProgram[instructionAddress]
        if opcode == HALT:
            break
        param1 = intcodeProgram[instructionAddress + 1]
        param2 = intcodeProgram[instructionAddress + 2]
        pointer = intcodeProgram[instructionAddress + 3]
        # Run the designated operations with the arguments specified
        try:
            if opcode == ADD:
                intcodeProgram[pointer] = intcodeProgram[param1] + \
                    intcodeProgram[param2]
            elif opcode == MULTIPLY:
                intcodeProgram[pointer] = intcodeProgram[param1] * \
                    intcodeProgram[param2]
        except IndexError:
            # This program is invalid and won't compile, so return -1 as the error code
            return -1
    # Return the output
    return intcodeProgram[0]

# Create opcode constants
ADD = 1
MULTIPLY = 2
HALT = 99

# Load Intcode program
with open('./Day2Data.txt', 'r') as inputFile:
    fileReader = csv.reader(inputFile)
    intcodeProgram = [int(i) for i in list(fileReader)[0]]

# Compile the Intcode program with nouns and verbs from 0-100, inclusive
for noun in range(100):
    found = False
    for verb in range(100):
        # Have to make sure to copy the program so you don't just modify the object the variable references
        output = compileIntcode(intcodeProgram.copy(), noun, verb)
        if output == 19690720:
            print("FOUND!!!")
            print(100 * noun + verb)
            found = True
            break
    if found:
        break
