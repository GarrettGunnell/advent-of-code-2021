
inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    input.append(int(line.strip()))

def silver(input):
    timesIncremented = 0
    for i in range(1, len(input)):
        if input[i] > input[i - 1]:
            timesIncremented += 1
    return timesIncremented

def gold(input):
    timesIncremented = 0

    for i in range(0, len(input) - 3):
        sum1 = input[i] + input[i + 1] + input[i + 2]
        sum2 = input[i + 1] + input[i + 2] + input[i + 3]

        if sum2 > sum1:
            timesIncremented += 1
    return timesIncremented

print(silver(input))
print(gold(input))