def last_digit_best(lst):
    if not lst:
        return 1
    else:
        out = 1
        for n in lst[len(lst):0:-1]:
            print "#1", n, out
            out = n**out
            print "#2", n, out
            if out > 2:
                out -= 2
                out %= 4
                out += 2
            print "#3", n, out
    return lst[0]**out% 10

def foo(lst):
    if len(lst) == 1:
        return lst[0]%4
    if lst[0]%4 == 3:
        if lst[1]%2 == 0:
            return 1
        return 3
    elif lst[0]%4 == 2:
        if lst[1] == 1:
            return 2
        return 0
    return lst[0]%4 # 0 or 1

def last_digit(lst):
    if len(lst) == 0:
        return 1
    if len(lst) == 1:
        return lst[0]%10
    for i in range(len(lst) - 1, 0, -1):
        if lst[i] == 0:
            lst[i-1] = 1
    lasts = [[0]*4,
            [1]*4,
            [6,2,4,8],
            [1,3,9,7],
            [6,4]*2,
            [5]*4,
            [6]*4,
            [1,7,9,3],
            [6,8,4,2],
            [1,9]*2]
    return lasts[lst[0]%10][foo(lst[1:])]