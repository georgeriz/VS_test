def pick_hole(up_holes, left_holes, down_holes, right_holes, bug_pos, result):
    for hole in reversed(up_holes):
        if bug_pos >= hole[1]:
            result[hole[0]] += 1
            break
    else:
        if left_holes:
            result[left_holes[0][0]] += 1
        elif down_holes:
            result[down_holes[0][0]] += 1
        elif right_holes:
            result[right_holes[-1][0]] += 1
        else:
            result[up_holes[-1][0]] += 1

def cockroaches(room):
    result = [0]*10
    bugs = []
    up_holes, down_holes, right_holes, left_holes = [], [], [], []
    for i, line in enumerate(room):
        for j, symbol in enumerate(line):
            if symbol.isdigit():
                if i == 0:
                    up_holes.append((int(symbol), j))
                if i == len(room) - 1:
                    down_holes.append((int(symbol), len(line) - j))
                if j == 0:
                    left_holes.append((int(symbol), len(room) - i))
                if j == len(line) - 1:
                    right_holes.append((int(symbol), i))
            elif symbol in "UDLR":
                bugs.append((symbol, i, j))
    for bug in bugs:
        if bug[0] == 'U':
            pick_hole(up_holes, left_holes, down_holes, right_holes, bug[2], result)
        elif bug[0] == 'L':
            pick_hole(left_holes[::-1], down_holes, right_holes[::-1], up_holes, len(room) - bug[1], result)
        elif bug[0] == 'D':
            pick_hole(down_holes[::-1], right_holes[::-1], up_holes[::-1], left_holes[::-1], len(line) - bug[2], result)
        else:
            pick_hole(right_holes, up_holes[::-1], left_holes, down_holes[::-1], bug[1], result)
    return result
