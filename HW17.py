# Madison Thorburn-Gundlach
# Due October 22, 2015
# hw 17 exercises 25 and 27 and another thing not from the book -- see below for further detail

# exercise 25: take an input sentence and return every letter used (no duplicates in the return)
def unique_letters(sentence_string):
    import string
    unique_list = []
    sentece_string = sentence_string.strip(string.punctuation) # this doesn't work a I can't figure out why.  It breaks the whole code.
    sentence_string = sentence_string.lower()
    
    # (b) use a for loop
    for char in sentence_string:
        if character not in unique_list:
            unique_list.append(char)
            
    # (a) use a while loop
    index = 0
    while index < sentence_string.length():
        if sentence_string[index] not in unique_list:
            unique_list.append(sentence_string[index])
        index += 1

    print(unique_list)

# exercise 28: I don't even know what this is supposed to do what does it want from me
# something about taking a list and making a 2-dimensional list but I don't know anything beyond that
# wait no yes I do it might involve the alphabet
# but other than that I'm lost and it's late so if I emailed you I probably wouldn't get help in time


# another thing not from the book: take two strings as input, return true if they have the same unique_letters list (essentially)
def same_letters(string1, string2):
    string1_unique = []
    string1.lower()
    string1.strip(string.punctuation) # this doesn't work a I can't figure out why.  It breaks the whole code.

    string2.lower()
    string2.strip(string.punctuation) # this doesn't work a I can't figure out why.  It breaks the whole code.

    for char in string1:
        if char not in string1_unique:
            string1_unique.append(char)
            
    for char in string2:
        if char not in string2_unique:
            string2_unique.append(char)

    if string1_unique == string2_unique:
        return True # breaks out of function if true
    
    return False
