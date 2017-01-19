# This is one of the scripts wtih argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# okay, that *args is actually pointless, let's do it again.
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1


# this takes NO arguments
def print_none():
    print "I got nothin'."

print_two("Ryan","Yount")
print_two_again("Ryan","Yount")
print_one("First!")
print_none()
