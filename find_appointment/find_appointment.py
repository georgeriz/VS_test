from datetime import datetime, timedelta

def get_start_time(schedules, duration):
    s = [(datetime.strptime(x[0], "%H:%M"), datetime.strptime(x[1], "%H:%M")) for l in schedules for x in l]
    def trange(s,f,i):
        while s < f:
            yield s
            s += timedelta(minutes=i)
    for p in trange(datetime.strptime("09:00", "%H:%M"), datetime.strptime("19:00", "%H:%M") - timedelta(minutes=duration-1), 1):
        e = p + timedelta(minutes=duration)
        if all(e <= t[0] or p >= t[1] for t in s):
            return p.strftime("%H:%M")
    return None