# baralho len(52)
# naipes is 4

naipes = {
    'C': {
        'length': 0,
        'list': [],
    },
    'E': {
        'length': 0,
        'list': [],
    },
    'U': {
        'length': 0,
        'list': [],
    },
    'P': {
        'length': 0,
        'list': [],
    },
}
line = input()


for i in line:
    if not i.isdigit():
        naipes[i]['length'] += 1

        index = line.index(i)
        deck = line[(index - 2)] + line[(index - 1)] + line[index]
        print(deck)

        naipes[i]['list'].append(deck)

print(naipes)
