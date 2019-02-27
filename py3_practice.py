def average(num1, num2):
	return ((num1 + num2) / 2)

print(average(1, 100))
print(average(1, -1))

def tenth_power(num):
  return num**10

print(tenth_power(1))
print(tenth_power(0))

def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

def square_root(num):
  return num**(1/2)
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

def tip(total, percentage):
  return total*(percentage/100)
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
#should print 2.5
print(tip(0, 100))
#should print 0.0

def win_percentage(wins, losses):
  	return (wins/(wins+losses) * 100)
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

def first_three_multiples(num):
  num1 = num
  num2 = num*2
  num3 = num*3
  print(num1, num2, num3)
  return num3
# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

