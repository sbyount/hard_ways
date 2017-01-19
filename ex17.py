from sys import argv
from os.path import exists

# uppack from argv
script, from_file, to_file = argv

print "\nCopying from %s to %s." % (from_file, to_file)

# open the input file to pointer
in_file = open(from_file)
# read the file into var
in_data = in_file.read()

# measure the file length in decimal
print "The input file is %d bytes long." % len(in_data)

# Use exist function and pass true if file exists
print "Does the output file exist? %r" % exists(to_file)
# Pause for input
print "When ready, press RETURN to continue, or Cntrl-C to abort."
raw_input()

# Open or create the output file in write mode
out_file = open(to_file, "w")
# write the data read from the input file
out_file.write(in_data)

# Close the files.
print "Alright, that is done, closing files."
out_file.close()
in_file.close()
