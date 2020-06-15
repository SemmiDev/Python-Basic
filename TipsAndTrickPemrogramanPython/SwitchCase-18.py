def one():
	print("one")

def two():
	print("two")

def three():
	print("three")

case = 'one'
switch = {
	'one': one,
	'two': two,
	'three': three
}

switch[case]()