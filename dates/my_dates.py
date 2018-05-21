import calendar

def foo(year, month):
	first = "{}-{}-01".format(year, month)
	last = "{}-{}-{}".format(year, month, calendar.monthrange(year, month)[1])
	return first, last