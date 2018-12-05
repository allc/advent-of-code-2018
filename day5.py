'''
https://adventofcode.com/2018/day/5

Input: https://adventofcode.com/2018/day/5/input

cat inputs/day5.txt | python3 day5.py
'''

s = input()

l = list()

for c in s:
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

print(len(l))
