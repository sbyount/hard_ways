from sys import argv

# unpack the following variablses from argv
script, input_file = argv

# define function that prints all of the supplied file
def print_all(f):
    print f.read()

# define function.  Set the file supplied at line 0
def rewind(f):
    f.seek(0)

# define function to print supplied line in supplied file
def print_a_line(line_count, f):
    print line_count, f.readline() # not sure where these come from.

# Open the file inpput by argv on the command line.
current_file = open(input_file)

print "First let's print the whole file:\n"

# call print_all funciton with current file'
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# call the rewind function to set the file to line 0
rewind(current_file)

print "Let's print three lines."

# Set line to 1 and print
current_line = 1
print_a_line(current_line, current_file)
# increment by one line
current_line += 1
print_a_line(current_line, current_file)
# increment by one line
current_line += 1
print_a_line(current_line, current_file)
