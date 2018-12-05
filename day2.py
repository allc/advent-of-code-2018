'''
https://adventofcode.com/2018/day/2

Input: https://adventofcode.com/2018/day/2/input

cat inputs/day2.txt | python3 day2.py
'''

def solution(ls):
    two = 0
    three = 0
    for l in ls:
        cs = dict()
        for c in l:
            if c in cs:
                cs[c] += 1
            else:
                cs[c] = 1
        for _, v in cs.items():
            if v == 2:
                two += 1
                break
        for _, v in cs.items():
            if v == 3:
                three += 1
                break

    return two * three


ls = list()
while True:
    try:
        l = input()
        if l == '':
            break
        ls.append(l)
    except EOFError:
        break

print(solution(ls))
