from collections import Counter

def freqQuery(queries):
    freq = Counter()
    cnt = Counter()
    answers = []
    for q in queries:
        if q[0] == 1:
            cnt[freq[q[1]]] -= 1
            freq[q[1]] += 1
            cnt[freq[q[1]]] += 1
        else:
            if cnt[q[1]] > 0:
                answers.append(1)
            else:
                answers.append(0)
    return answers

print(freqQuery([[1,10],[1,5],[1,4],[1,4],[3,2],[1,5],[1,5],[1,4],[3,2]]))