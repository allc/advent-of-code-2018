'''
https://adventofcode.com/2018/day/1

Input: https://adventofcode.com/2018/day/1/input

cat inputs/day1.txt | python3 day1.py
'''

frequency = 0

while True:
    try:
        frequency += int(input())
    except:
        break

print(frequency)
