print "How old are you?",
age = int(raw_input())
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = int(raw_input())

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
print "You are overweight! %s" % (age + weight)
