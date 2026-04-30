# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/tempo/

# Point 90/100
# t = 0,025s / 1s
# memory 4.06 MB/ 64 MB

# By josephyzz

import sys
from collections import defaultdict

time_of_response = defaultdict(int)
waiting_response = defaultdict(int)
last_time = 0

restrict_passed = True
record = int(sys.stdin.readline().strip())

if record >= 1 and record <= 20:
    for _ in range(record):
        event, number = input().split()
        number = int(number)
        if number >= 1 and number <= 100:
            if event == 'T':
                last_time += number - 1
            else:
                last_time += 1

            if event == 'R':
                waiting_response[number] = last_time
            else:
                if number in waiting_response:
                    time_of_response[number] += (
                        last_time - waiting_response[number]
                    )
                    del waiting_response[number]
        else:
            restrict_passed = False

    if restrict_passed:
        for x in waiting_response:
            time_of_response[x] = -1

        for k in sorted(time_of_response.keys()):
            print(f'{k} {time_of_response[k]}')
