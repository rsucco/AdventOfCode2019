# Intcode computer version 2, with added functionality for I/O

# Create opcode and parameter constants
ADD = '01'
MULTIPLY = '02'
INPUT = '03'
OUTPUT = '04'
JUMPIFTRUE = '05'
JUMPIFFALSE = '06'
LESSTHAN = '07'
EQUALS = '08'
HALT = '99'
IMMEDIATE = 1
POSITION = 0

def compileIntcode(intcodeProgram, noun = "err", verb = "err"):
    intcodeProgram = list(intcodeProgram)
    # Set the noun and verb in the program
    if noun != "err":
        intcodeProgram[1] = noun
    if verb != "err":
        intcodeProgram[2] = verb

    # Iterate through all the values in the opcode memory addresses
    instructionAddress = 0
    while instructionAddress < len(intcodeProgram):
        # Get the opcode and the modes for the parameters
        opcodeModes = str(intcodeProgram[instructionAddress]).zfill(5)
        opcode = opcodeModes[-2:]
        param1Mode = int(opcodeModes[2])
        param2Mode = int(opcodeModes[1])
        
        # Halt if ordered
        if opcode == HALT:
            break
        
        # Get parameters
        param1 = int(intcodeProgram[instructionAddress + 1])
        if param1Mode == POSITION and opcode != INPUT and opcode != OUTPUT:
            param1 = int(intcodeProgram[param1])

        # Only get the second and third parameters if the opcode requires them to avoid index errors
        if opcode != INPUT and opcode != OUTPUT:
            param2 = intcodeProgram[instructionAddress + 2]
            if param2Mode == POSITION:
                param2 = intcodeProgram[param2]
            pointer = intcodeProgram[instructionAddress + 3]

      # Run the designated operations with the arguments specified
        try:
            if opcode == ADD:
                intcodeProgram[pointer] = param1 + param2
                instructionAddress += 4
            elif opcode == MULTIPLY:
                intcodeProgram[pointer] = param1 * param2
                instructionAddress += 4
            elif opcode == INPUT:
                inputValue = input("Enter input: ")
                inputValue = int(inputValue)
                intcodeProgram[param1] = inputValue
                instructionAddress += 2
            elif opcode == OUTPUT:
                if param1Mode == IMMEDIATE:
                    print("Output: " + str(param1))
                else:
                    print("Output: " + str(intcodeProgram[param1]))
                instructionAddress += 2
            elif opcode == JUMPIFTRUE:
                if param1 != 0:
                    instructionAddress = param2
                else:
                    instructionAddress += 3
            elif opcode == JUMPIFFALSE:
                if param1 == 0:
                    instructionAddress = param2
                else:
                    instructionAddress += 3
            elif opcode == LESSTHAN:
                if param1 < param2:
                    intcodeProgram[pointer] = 1
                else:
                    intcodeProgram[pointer] = 0
                instructionAddress += 4
            elif opcode == EQUALS:
                if param1 == param2:
                    intcodeProgram[pointer] = 1
                else:
                    intcodeProgram[pointer] = 0
                instructionAddress += 4
        except IndexError:
            # This program is invalid and won't compile, so return -1 as the error code
            print("Invalid program")
            return -1

    # Return the output
    return intcodeProgram[0]
