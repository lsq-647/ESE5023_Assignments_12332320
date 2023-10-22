# 3. Pascal triangle
def Pascal_triangle(k):
    line = [[1], [1, 1]]
    for i in range(2, k):
        pre = line[i-1]
        cul = [1]
        for j in range(i-1):
            cul.append(pre[j] + pre[j+1])
        cul.append(1)
        line.append(cul)
    return cul

print(Pascal_triangle(100))
print(Pascal_triangle(200))

# I consulted this website to help me: https://blog.csdn.net/W_chuanqi/article/details/123679167
