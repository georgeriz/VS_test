def last_digit(lst):
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

print last_digit([7, 6, 21])