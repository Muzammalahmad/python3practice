def ground_shipping(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return 20 + (price_per_pound * weight)
#Test 8.4 lb×$4.00+$20.00=$53.60 // passed
#print(ground_shipping(8.4))

# constant variable for premium ground shipping
PREMIUM_GROUND_SHIPPING = 125.0

def drone_shipping(weight):
  if weight <= 2:
    price_per_pound = 4.5 
  elif weight >= 6:
  	price_per_pound = 9.0 
  elif weight >= 10:
    price_per_pound = 12.00
  else:
 		price_per_pound = 14.25
  return price_per_pound * weight
  
# Test 1.5 lb×$4.50+$0.00=$6.75 // passed
#print((drone_shipping(1.5)))

def print_cheapest_method(weight):
  #create variables for each function below
  ground = ground_shipping(weight)
  premium = PREMIUM_GROUND_SHIPPING
  drone = drone_shipping(weight)
  
  #conditionals to check cheapest price
  if ground < premium and ground < drone:
    #define the method and set cost
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone
    
  #print statment to share cheapest price by method.
  print(
  	"The cheapest option available is $%.2f with %s shipping." % (cost, method)
  )
# Test 4.8 and 41.5 as weight input // passed
print_cheapest_method(4.8)
print_cheapest_method(41.5)