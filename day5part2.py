'''
https://adventofcode.com/2018/day/5#part2

Input: https://adventofcode.com/2018/day/5/input

cat inputs/day5.txt | python3 day5part2.py
'''

def react(s, r=None):
    l = list()
    for c in s:
        if c.lower() == r or c.upper() == r:
            continue
        if len(l) > 0:
            last = l.pop()
            if str.isupper(c) and c.lower() == last:
                pass
            elif str.islower(c) and c.upper() == last:
                pass
            else:
                l.append(last)
                l.append(c)
        else:
            l.append(c)
    return l

s = input()

l = react(s)

c = None # best remove char
shortest = 10000

for r in range(65, 91):
    r = chr(r)
    current_l = react(l, r=r)
    if len(current_l) < shortest:
        c = r
        shortest = len(current_l)

print(shortest)
