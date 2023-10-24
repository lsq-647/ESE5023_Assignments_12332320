# 4. Add or double
import random
x = random.randint(1,100)
print(x)

def Least_moves(x):
    moves = 0
    while x > 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x -= 1
        moves += 1
    return moves
Least_moves(x)


