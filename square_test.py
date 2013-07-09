from square import square

result = [0,1,4,9,16,25,36,49,64,81,100]
not_square = [0,100,81,64,49,35,25,16,9,4,1]

def test_square():
	for value in range(1,11):
		assert square(value) == result[value]

def test_not_square():
	for value in range(1,11):
		assert not square(value) == not_square[value]
	
	for value in range(1,11):
		assert not square(value+1) == result[value]

