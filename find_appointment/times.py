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
        m = s + timedelta(minutes=i)
        yield (s,m)
        s = m

for i in trange(datetime.strptime("09:00", "%H:%M"), datetime.strptime("15:30", "%H:%M"), 30):
    print i