""" The Blueprints for Jeans """

class jeans:
#init method gets called everytime a new object is created.
    def __init__(self, waist, length, color):
        self.waist = waist
        #my_jeans.waist
        self.length = length
        #my_jeans.length
        self.color = color
        #represents a pair of jeans being worn or not
        #my_jeans.color
        self.wearing = False
        #returns a boolean value 
        #my_jeans.wearing = True/False
    
    def put_on(self):
        #user will not need to provide any aruguments with self in place.my_
        print('Putting on {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = True
        #my_jeans.put_on() # calling a bound method jeans.put_on.
        #sets value for wearing to True


    def take_off(self):
        print('Taking off {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = False
        #bound method jeans.take_off() sets value for wearing to False.
        
# create and examine a pair of jeans
my_jeans = jeans(31,32,'blue')
print(type(my_jeans))
print(dir(my_jeans))

# don and remove the jeans
my_jeans.put_on()
print(my_jeans.wearing)

my_jeans.take_off()
print(my_jeans.wearing)
