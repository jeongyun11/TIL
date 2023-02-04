
x, y = 1, 7
print ((x,y))
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
print(delta)
test = []
for dx, dy in delta :
    test.append((x+dx, y+dy))
print(test)
