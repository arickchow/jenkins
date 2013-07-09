from square import square

def setup_func():
	result = [1,4,9,16,25,36,49,64,81,100]

def teardown_func():
	pass

@with_setup(setup_func,teardown_func)
def test_square():
	for value in range(1,11):
		assert square(value) == result[value]




