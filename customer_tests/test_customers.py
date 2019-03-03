import pytest

def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")
	
@pytest.fixture
def customer_repr():
	return 'customer_Maria'
	
def test_customer_repr(customer, customer_repr):
	assert customer_repr == 'customer_' + customer.name