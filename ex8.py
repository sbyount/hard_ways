# Assign formatters to variable
formatter = "%r %r %r %r"

# Pass integers into variable and print
print formatter % (1, 2, 3, 4)
# Pass strings into variable and print
print formatter % ("one", "two", "three", "four")
# Pass boolean values into variable
print formatter % (True, False, False, True)
# Pass format characters into variable
print formatter % (formatter, formatter, formatter, formatter)
# Pass multiple word strings into variable
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
