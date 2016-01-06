# Madison Thorburn-Gundlach
# Due November 10, 2015
# take a string as an input and translate it using a codex dictionary

# establish codex
codex = {}
for asci in range(97,123):
    if asci <= 120:
        codex.update({chr(asci):chr(asci+2)})
    else:
        codex.update({chr(asci):chr(asci-24)})

# establish a return placeholder
to_return = []

# take input
to_translate = (input("What to translate?\n")).lower()

# iterate through input
for char in to_translate:
    # check if character is a key
    if char in codex.keys():
    # if it is then add the VALUE to the return placeholder
        to_return.append(codex[char])
    # if not then add the CHAR to the return placehold
    else:
        to_return.append(char)
        
# make pretty for output, output
output = "".join(to_return)
print(output.strip("'"))

