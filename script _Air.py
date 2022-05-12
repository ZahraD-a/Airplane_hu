from os.path import exists

filename = "./input.txt"
lines = []

# function to validate user input
def validate(line):
    try:
        a, b, c = line.split(" ")
        if len(a)>=1 and len(b)>=1 and len(b)>=1:
            #check if c can be int
            _ = int(c)
        else:
            return False
    except Exception:
        return False
    else:
        return True

# check if ./input.txt exists
if exists(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
else:
    #read from input
    while True:
        line = input()
        if validate(line):
            lines.append(line)
        else:
            break

airlines = list()
destinations = list()
passengers = list()

# for each line split it into lists created above
for line in lines:
    tmp = line.strip().split(" ")
    if validate(line):
        airlines.append(tmp[0])
        destinations.append(tmp[1])
        passengers.append(tmp[2])

# convert passengers into int data type
passengers = [int(x) for x in passengers]

# Exercice 1
print(destinations.count("Frankfurt"))

# Exercice 2
if len(passengers) == 0:
    print("The file is empty!")
else:
    index = passengers.index(max(passengers))
    print(airlines[index],destinations[index], passengers[index])

# Exercice 3
for x in passengers:
    if x < 100:
        index = passengers.index(x)
        print(airlines[index],destinations[index], passengers[index])
        break
else:
    print('There is no flight with passengers less than 100.')

# Exercice 4
if len(passengers) == 0:
    print("The file is empty!")
else:
    # initiate dictionary
    data = {}
    # group data and sum by key
    for key, value in zip(airlines, passengers):
        data[key] = data.get(key, 0) + value

    # get key with max value
    max_key = max(data, key=data.get)
    print(max_key, data.get(max_key))