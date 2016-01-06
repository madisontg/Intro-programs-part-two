# Madison Thorburn-Gundlach
# Due October 6, 2015
# For a file consisting of one integer per line (unknown number),
# return the average, mean deviation, and how many of each number there are in the file

# import math

# assume only single-digit numbers

# storage
total = 0
standard_deviation = 0
numbers = ""
count = 0
# open file (input)
file = input("What file contains one single-digit number per line?\n")
open(file, "r")

# read through file; record each number to a total; record count; calculate average
for line in file:
    line = int(line)
    total += line
    count += 1
average = total/count    
    
# close file
file.close()

# open file
open(file, "r")

# read through file; calculate standard deviation
for line in file:
    line = int(line)
    temp = ((math.abs(average - line)) ** 2)
    # I'm lost beyond that
    
# close file
file.close()

# open file
open(file, "r")

# read through file; concat each number to a string
for line in file:
    numbers += line
    
# close file
file.close()

# for each instance of each number in string (0-9) concat to new string [number]
for index in numbers:
    index = int(index)
    if index == 1:
        one += "*"
    if index == 2:
        two += "*"
    if index == 3:
        three += "*"
    if index == 4:
        four += "*"
    if index == 5:
        five += "*"
    if index == 6:
        six += "*"
    if index == 7:
        seven += "*"
    if index == 8:
        eight += "*"
    if index == 9:
        nine += "*"
    if index == 0:
        zero += *
        
# starting at position 1 of each number string, replace each number with "*"

# returns
print("Average is", average)
print("Standard deviation is", standard_deviation)
print("Histogram:")

# This is my process, the best I could do
# I'm not exactly sure how to implement half of it, or if it'll even work
# But hopefully I can get partial credit maybe.
