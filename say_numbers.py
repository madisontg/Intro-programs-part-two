# Madison Thorburn-Gundlach
# Due November 12, 2015
# exercise 22: create a program that prompts for an integer and prints out the integer using words

translate = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}
to_translate = input("Gimme a whole number of any length\n")
translated = ""

# cycle through input
for char in to_translate:
    # double check to make sure the char is a number between 0 and 9
    if char in translate.keys():
        # add the value of the key "char" to the translated string (I know it's not really adding just go with it)
        translated += translate[char] + " "
        
print(translated)
