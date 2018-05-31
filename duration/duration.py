def duration(seconds):
	if seconds == 0:
		return "now"
	y, seconds = divmod(seconds, 31536000)
	d, seconds = divmod(seconds, 86400)
	h, seconds = divmod(seconds, 3600)
	m, seconds = divmod(seconds, 60)
	t = ["year", "day", "hour", "minute", "second"]
	t = [str(j) + " " + t[i] if j == 1 else str(j) + " " + t[i] + "s" for i,j in enumerate((y,d,h,m,seconds)) if j != 0]
	return ", ".join(t[:-1]) + " and " + t[-1] if len(t) > 1 else t[0]
	