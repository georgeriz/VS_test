def duration(seconds):
	m, s = divmod(seconds, 60)
	h = m/60
	d = h/24
	y = d/365
	res = [y,d,h,m,s]
	q = ["year", "day", "hour", "minute", "second"]
	t = [str(i) + " " + q[j] for j,i in enumerate(res) if i != 0]
	t = [i + "s" for i in t if i!=1]
	f = ", ".join(t[:-1])
	if f:
		return f + " and " + t[-1]
	return t[-1]
	