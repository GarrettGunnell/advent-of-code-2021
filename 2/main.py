
inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip()
    line = line.split(' ')
    
    input.append(line)

def silver(input):
    horizontal = 0
    depth = 0
    for line in input:
        direction = line[0]
        amount = int(line[1])
        if direction == 'forward':
            horizontal += amount
        elif direction == 'up':
            depth -= amount
        elif direction == 'down':
            depth += amount

    return  horizontal * depth

def gold(input):
    horizontal = 0
    depth = 0
    aim = 0

    for line in input:
        direction = line[0]
        amount = int(line[1])
        if direction == 'forward':
            horizontal += amount
            depth += aim * amount
        elif direction == 'up':
            aim -= amount
        elif direction == 'down':
            aim += amount

    return  horizontal * depth

print(silver(input))
print(gold(input))