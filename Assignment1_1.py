# 1. Flowchart
import random
a = random.random()
b = random.random()
c = random.random()
print(a)
print(b)
print(c)

def Print_values():
    if a>b:
        if b>c:
            print(a, b, c)
        elif b<c:
            if a>c:
                print(a, c, b)
            elif a<c:
                print(c, a, b)
    elif a<b:
        if b>c:
            print(c, a, b)
        elif b<c:
            print(c, b, a)
Print_values()

