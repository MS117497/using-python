# Get user name
name = raw_input("Enter your name: ")
# get the length of the user name
name_length = len(name)
# Print first line of banner
# Add a line space between the top of the banner and the name
print("-" * (name_length + 6) + "\n")
# print the user name in the banner
# Add a line space between the bottom of the banner and the name
print(".::" + name + "::.\n")
# Print last line of banner
print("-" * (name_length + 6) + "\n")
