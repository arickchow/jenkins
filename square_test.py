from square import square
import nose

result = [0,1,4,9,16,25,36,49,64,81,100]
not_square = [0,100,81,64,49,35,25,16,9,4,1]

def test_square():
	for value in range(1,11):
		nose.tools.assert_equal(square(value),result[value])
def test_not_square():
	for value in range(1,11):
		nose.tools.assert_not_equal(square(value),not_square[value])
	
	for value in range(1,11):
		nose.tools.assert_not_equal(square(value+1),result[value])
	
	for value in range(1,11):
		nose.tools.assert_not_equal(square(value+2),result[value])
