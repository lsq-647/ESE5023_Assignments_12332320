# 5. Dynamic programming
# 5.1
def Find_expression(num):
    def backtrack(expr, pos, val, prev):
        if pos == len(digits) and val + prev == num:
            print(expr + '=' + str(num))
            return
        for i in range(pos, len(digits)):
            cur = int(digits[pos:i+1])
            if pos == 0:
                backtrack(expr + str(cur), i + 1, 0, cur)
            else:
                backtrack(expr + '+' + str(cur), i + 1, val + prev, cur)
                backtrack(expr + '-' + str(cur), i + 1, val + prev, -cur)
    digits = '123456789'
    backtrack('', 0, 0, 0)

import random
target = random.randint(1,101)
print(target)
Find_expression(target)

#5.2
def Find_expression(num):
    count = 0
    def backtrack(pos, val, prev):
        nonlocal count
        if pos == len(digits) and val + prev == num:
            count += 1
            return
        for i in range(pos, len(digits)):
            cur = int(digits[pos:i+1])
            if pos == 0:
                backtrack(i + 1, 0, cur)
            else:
                backtrack(i + 1, val + prev, cur)
                backtrack(i + 1, val + prev, -cur)
    digits = '123456789'
    backtrack(0, 0, 0)
    return count

Total_solutions = []
for i in range(1, 101):
    Total_solutions.append(Find_expression(i))
print(Total_solutions)

# I consulted ChatGDP to help me.