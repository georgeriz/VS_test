def duration(seconds):
	p, s = divmod(seconds, 60)
	p, m = divmod(p, 60)
	p, h = divmod(p, 60)
	p, d = divmod(p, 24)
	y = p%365
	t = ["year", "day", "hour", "minute", "second"]
	t = [str(j) + " " + t[i] for i,j in enumerate((y,d,h,m,s)) if j != 0]
	t = map(lambda x: x if x.startswith("1") else x + "s", t)
	return ", ".join(t[:-1]) + " and " + t[-1] if len(t) > 1 else t[0]
	