import this

#Get the Zen of Python as a string
zen = "".join([this.d.get(c, c) for c in this.s])
#print(zen)

# Count occurrences
better_count = zen.count("better")
never_count = zen.count("never")
is_count = zen.count("is")

# Modify the text
zen_upper = zen.upper()
zen_final = zen_upper.replace("I", "&")

# Print results
#print("Modified Zen of Python:\n")
print(zen_final)
print("\nWord counts:")
print(f'"better" occurs {better_count} times')
print(f'"never" occurs {never_count} times')
print(f'"is" occurs {is_count} times')