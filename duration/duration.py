def duration(seconds):
	p, s = divmod(seconds, 60)
	p, m = divmod(p, 60)
	p, h = divmod(p, 60)
	p, d = divmod(p, 24)
	y = p%365
	res = [y,d,h,m,s]
	q = ["year", "day", "hour", "minute", "second"]
	
	t = []
	for i,j in enumerate(res):
		if j != 0:
			t.append(str(j) + " " + q[i])
			if j != 1:
				t[-1] += "s"
	return ", ".join(t[:-1]) + " and " + t[-1] if len(t) > 1 else t[0]
	