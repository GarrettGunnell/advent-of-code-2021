
inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
for line in inputLines:
    line = line.strip()
    input.append(line)

def silver(input):
    bit = 0
    gamma = ''
    epsilon = ''

    for col in range(len(input[0])):
        num1s = 0
        num0s = 0
        for row in input:
            if row[bit] == '0':
                num0s += 1
            else:
                num1s += 1

        bit += 1
        if num1s > num0s:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
        

        
    return int(gamma, 2) * int(epsilon, 2)

def gold(input):
    bit = 0
    
    numbers = input.copy()

    while len(numbers) > 1:
        num1s = 0
        num0s = 0
        newnums = []
        for num in numbers:
            if num[bit] == '0':
                num0s += 1
            else:
                num1s += 1 

        if num0s > num1s:
            for num in numbers:
                if num[bit] == '0':
                    newnums.append(num)
        else:
            for num in numbers:
                if num[bit] == '1':
                    newnums.append(num)

        bit += 1
        numbers = newnums.copy()

    oxygen = numbers[0]

    bit = 0
    numbers = input.copy()

    while len(numbers) > 1:
        num1s = 0
        num0s = 0
        newnums = []
        for num in numbers:
            if num[bit] == '0':
                num0s += 1
            else:
                num1s += 1 

        if num0s > num1s:
            for num in numbers:
                if num[bit] == '1':
                    newnums.append(num)
        else:
            for num in numbers:
                if num[bit] == '0':
                    newnums.append(num)

        bit += 1
        numbers = newnums.copy()

    co2 = numbers[0]
    return int(oxygen, 2) * int(co2, 2)

print(silver(input))
print(gold(input))