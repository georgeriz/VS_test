from datetime import datetime, timedelta

def conv(s):
    if type(s) == str:
        return datetime.strptime(s, "%H:%M")
    return s.strftime("%H:%M")

def trange(s,f,i):
    while s < f:
        yield s
        s += timedelta(minutes=i)

def get_start_time(schedules, duration):
    s = [(conv(x[0]), conv(x[1])) for l in schedules for x in l]
    for p in trange(conv("09:00"), conv("19:00"), 1):
        e = p + timedelta(minutes=duration)
        if all(e <= t[0] or p >= t[1] for t in s) and e <= conv("19:00"):
            return conv(p)
    return None