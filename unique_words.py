# Madison Thorburn-Gundlach
# Due November 12, 2015
# exercise 13: use sets to refactor the "unique words in the gettysburg address" program

file = open("gettysburg.txt", "r")
word_list = set()
for line in file:
    words = line.split()
    for word in words:
        word_list.add(word.lower().strip("--,."))

print(len(word_list), "unique words:")
print()
for thing in word_list:
    if thing != "  " and thing != "":
        print(thing)

# exercise 7 answer: (a) same as my_set <= your_set, returns True (b) same as your_set <= my_set, returns False
# exercise 9 answer :
#   coat, had, colors, red, blue
#   coat, had, colors, red, blue
#   the, my, coat, had, many, two, colors, main, red, blue, yellow
#   the, my, coat, had, many, two, colors, main, red, blue, yellow
#   the, my, many, two, main, yellow
#   the, my, many, two, main, yellow

# Please note that the "sets" listed in the book are, infact, tuples.
# I pretended they weren't because tuples can't do intersections and unions and stuff.
# Otherwise everything crashes.
