""" A Functional Egg breakfast """
cheese = 'cheddar'
def mix_and_cook():
	print('Mixing the ingredients')
	print('Greasing the frying pan')
	print('Pouring the mixture into a frying pan')
	print('Cooking the first side')
	print('Flipping it!')
	print('Cooking the other side!')

#using the global variable to see how the output changes.
#experimenting with accessing global vs local variables.
def make_omelette():
	
	global cheese
	cheese = 'swiss'
	mix_and_cook()
	omelette = 'And there you have it, a {} omelette'.format(cheese)
	print omelette

def make_pancake(ingredient):
	mix_and_cook()
	pancake = 'Tada.... a delicious {} pancake'.format(ingredient)
	print pancake

#you can change the value of the argument everytime you access the function.
# remember: parameter != arguments
make_omelette()
# make_pancake('blueberries')

def fancy_omelette(*ingredients):
	mix_and_cook()
	omelette = 'Yummy! A fancy omelette with {}for ingredients'.format(ingredients)
	print omelette
# fancy_omelette('bell peppers', 'cheese', 'olives', 'tomatoes')