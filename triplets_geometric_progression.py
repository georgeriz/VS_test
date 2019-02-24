from collections import defaultdict

def countTriplets(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1
        print count
        print v3
        print v2

    return count

print(countTriplets([1,2,1,2,4], 2))