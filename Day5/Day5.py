import Intcode as computer
import csv

# Load Intcode program
with open('/home/ryan/git/AdventOfCode2019/Day5/Day5Data.txt', 'r') as inputFile:
    fileReader = csv.reader(inputFile)
    intcodeProgram = [int(i) for i in list(fileReader)[0]]


print(computer.compileIntcode(intcodeProgram))
