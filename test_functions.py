import functions as fn

def test_snake():
	test = fn.snake()
	test_ = fn.food()
	assert type(test) == object
	assert type(test_) == object