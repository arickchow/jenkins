from square import square

result = [0,1,4,9,16,25,36,49,64,81,100]




def test_square():
	for value in range(1,11):
		assert square(value) == result[value]



