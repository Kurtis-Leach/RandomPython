variableName = 'What your variable is'

print variableName

money_in_wallet = 40
sandwich_price = 7.50
sales_tax = .08 * sandwich_price

sandwich_price += sales_tax
money_in_wallet -= sandwich_price
print money_in_wallet

cucumbers = 1
price_per_cucumber = 3.25

total_cost = cucumbers * price_per_cucumber

print total_cost

#when only integers then it rounds down must be float to get a float
cucumbers = 100
num_people = 6

whole_cucumbers_per_person = cucumbers/num_people
float_cucumbers_per_person = float(cucumbers)/num_people
print (whole_cucumbers_per_person)
print (float_cucumbers_per_person)

#multiline strings
haiku = """The old pond,
A frog jumps in:
Plop!"""

#True and False are capatilized

skill_completed = "Python Syntax"
exercises_completed = 13
#The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5
point_total = 100
point_total += exercises_completed * points_per_exercise

print "I got " + str(point_total) + " points!" 