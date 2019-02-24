def freqQuery(queries):
    d = {}
    h = {}
    answers = []
    for q in queries:
        if q[0] == 1:
            if q[1] in d:
                h[d[q[1]]].remove(q[1])
            d[q[1]] = d.setdefault(q[1], 0) + 1
            if d[q[1]] in h:
                h[d[q[1]]].append(q[1])
            else:
                h[d[q[1]]] = [q[1]]
            print 'add:', h
        elif q[0] == 2:
            if q[1] in d:
                h[d[q[1]]].remove(q[1])
                d[q[1]] -= 1
                if d[q[1]] == 0:
                    del d[q[1]]
                else:
                    if d[q[1]] in h:
                        h[d[q[1]]].append(q[1])
                    else:
                        h[d[q[1]]] = [q[1]]
                print 'del:', h
        else:
            if q[1] in h and h[q[1]]:
                answers.append(1)
            else:
                answers.append(0)
    return answers

print(freqQuery([[1,10],[1,5],[1,4],[1,4],[3,2],[1,5],[1,5],[1,4],[3,2]]))