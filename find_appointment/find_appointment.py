from datetime import datetime, timedelta

def get_start_time(schedules, duration):
    s = [(datetime.strptime(x[0], "%H:%M"), datetime.strptime(x[1], "%H:%M")) for l in schedules for x in l]
    def trange(s,f,i):
        while s < f:
            m = s + timedelta(minutes=1)
            yield (s,m)
            s = m
    # TODO it should be zip(range, range)
    for p in trange(datetime.strptime("09:00", "%H:%M"), datetime.strptime("19:00", "%H:%M"), duration):
        #print p
        if all(p[1] <= t[0] or p[0] >= t[1] for t in s):
            # TODO return string no datetime
            return p
    return None