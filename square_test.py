def setup():
	result = [1,4,9,16,25,36,49,64,81,100]
def teardown():
	pass

@with_setup(setup,teardown)
def test_square():
	for value in range(1,11):
		assert value*value == result[value]




