from datetime import datetime, timedelta

def foo(t, d):
    q = [int(i) for i in t.split(":")]
    h,m = divmod(d, 60)
    q[0] += h
    q[1] += m
    return q

#print foo("09:08", 125)

def bar(a):
    return [datetime.strptime(i, "%H:%M") for i in a]

#print bar(['09:00', '11:30'])

def blah(t, d):
    t = datetime.strptime(t, "%H:%M")
    return t + timedelta(minutes=d)

#print blah("09:08", 125)

def trange(s,f,i):
    while s < f:
        yield s
        s += timedelta(minutes=i)

for i in trange(bar(["09:00"])[0], bar(["11:30"])[0], 10):
    print i