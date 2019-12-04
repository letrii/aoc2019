"""
You arrive at the Venus fuel depot only to discover it's protected 
by a password. The Elves had written the password on a sticky note,
 but someone threw it out.

However, they do remember a few key facts about the password:

 - It is a six-digit number.
 - The value is within the range given in your puzzle input.
 - Two adjacent digits are the same (like 22 in 122345).
 - Going from left to right, the digits never decrease; they only ever 
increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle 
input meet these criteria?

Your puzzle input is 172851-675869.

--- Part Two ---
An Elf just remembered one more important detail: the two adjacent 
matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, 
the following are now true:

112233 meets these criteria because the digits never decrease and 
all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a 
larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, 
it still contains a double 22).
How many different passwords within the range given in your puzzle input
 meet all of the criteria?

Your puzzle input is still 172851-675869.

"""
puzzle_input = '172851-675869'
puzzle_input = puzzle_input.split('-')
numbers = map(str, range(int(puzzle_input[0]), int(puzzle_input[1])))

def check_rules(number):
    is_decrease = False
    repeats = {}
    for idx in range(len(number)):
        if idx > 0 and number[idx] == number[idx - 1]:
            if number[idx] not in repeats:
                repeats[number[idx]] = 1
            else:
                repeats[number[idx]] += 1
        if idx > 0 and number[idx] < number[idx - 1]:
            is_decrease = True
    return repeats, is_decrease

part1 = 0
part2 = 0
for number in numbers:
    repeats, is_decrease = check_rules(number)
    if len(repeats) > 0 and not is_decrease:
        part1 += 1
        is_adjacent = 1 in repeats.values()
        if is_adjacent:
            part2 += 1

print(part1, part2)