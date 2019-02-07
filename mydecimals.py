round(2.5) # 3 in python2 and 2 in python3
round(234, -1) # 230

'value is {:0.1f}.'.format(1.2345) # 'value is 1.2.'
format(2.34, '0.1f') # '2.3'

from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')
assert (a + b) == Decimal('6.3')
# assert (4.2 + 2.1) == 6.3 would fail

from decimal import localcontext
c = Decimal('1.3')
d = Decimal('1.7')
with localcontext() as ctx:
	ctx.prec = 3
	assert (c/d) == Decimal('0.765')
	
# the decimal module should be used with financial data
# it has worse performance than native float numbers

x = 1234.5678
format(x, '>10.2f') # right justified
format(x, ',') # include thousand separator