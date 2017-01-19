# define function with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print output args in integer format
    print "You have %d cheeses." % cheese_count
    print "You have %d boxes of crackers." % boxes_of_crackers
    print "Man, that's enough for a party!"
    print "Get a blanket.\n"

# Pass in a set of values directly
print "We can just give the function numbers directly."
cheese_and_crackers(20, 30)

# create variables and assign values.  Use the vars to pass in the values.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# add additional functionality in the arguments
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Add to variables inside the arguments
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# figure out cheese required per boxe
crackers_per_box = 300
cheese_per_cracker = 2
boxes_of_crackers = 10
cheese_count = (crackers_per_box * cheese_per_cracker)
cheese_and_crackers(cheese_count, boxes_of_crackers)
