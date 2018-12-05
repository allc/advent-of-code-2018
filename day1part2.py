'''
https://adventofcode.com/2018/day/1#part2

Input: https://adventofcode.com/2018/day/1/input

cat inputs/day1.txt | python3 day1part2.py
'''

def solution(changes):
    frequency = 0

    seen_freq = set([frequency])

    while True:
        for change in changes:
            frequency += change
            if frequency in seen_freq:
                return frequency
            else:
                seen_freq.add(frequency)


changes = list()

while True:
    try:
        changes.append(int(input()))
    except:
        break

print(solution(changes))
