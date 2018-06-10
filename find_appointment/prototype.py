def foo():
    possible = zip(range(9,19), range(10,20))
    schedules = [[(10,11),(14,15)],[(9,10)],[(11,12),(16,17),(17,18)]]
    possibles =[]
    for i, schedule in enumerate(schedules):
        possibles.append([])
        for p in possible:
            if all([p[1] <= t[0] or p[0] >= t[1] for t in schedule]):
                possibles[i].append(p)
    for item in possibles[0]:
        if all([item in li for li in possibles[1:]]):
            return item
    return None


schedules = [[(10,11),(13,14)],[(9,10)],[(11,15),(16,17),(17,19)]]
def bar(s=schedules):
    possible = zip(range(9,19), range(10,20))
    s = [x for l in s for x in l]
    for p in possible:
        if all(p[1] <= t[0] or p[0] >= t[1] for t in s):
            return p
    return None

print bar()