import pytest

from Customer import Customer

@pytest.fixture
def make_customer_record():

	created_records = []
	
	def _make_customer_record(name):
		record = Customer(name, [])
		created_records.append(record)
		return record

	yield _make_customer_record
	
	for record in created_records:
		# clean up code
		record.destroy()
		
@pytest.fixture
def customer():
	return Customer('Maria', [])
	
@pytest.fixture
def customer_repr():
	return 'Maria'