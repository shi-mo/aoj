print('MANHATTAN_DISTANCE = [')
for idx in range(16):
    print('    [ ', end="")
    for val in range(16):
        if (0 != val):
            print(',', end="")
        if (0 != val and 0 == val%4):
            print(' ', end="")
        goal = val - 1 if 1 <= val else 15
        goal_r = goal // 4
        goal_c = goal % 4
        r = idx // 4
        c = idx % 4
        d = abs(goal_r - r) + abs(goal_c - c)
        print(d, end="")
    print(' ],' if idx < 15 else ' ]')
print(']')
