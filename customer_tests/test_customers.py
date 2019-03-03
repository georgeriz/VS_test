import pytest

from Customer import Customer

@pytest.fixture
def make_customer_record():

	created_records = []
	
	def _make_customer_record(name):
		record = Customer(name, [])
		created_records.append(record)
		return record

	return _make_customer_record

		
def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")