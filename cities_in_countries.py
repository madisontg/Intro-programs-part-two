# Madison Thorburn-Gundlach
# Due November 11, 2015
# exercise 17

# establish a dictionary
cities = {}

# open a file for reading
file = open("cities.txt", "r")

# go through the file line by line
for line in file:
    # create a list for each city
    line = line.strip()
    city = line.split(", ")
    # if the second index (the country) is in the dictionary, += 1 the value of that key
    if city[1] in cities.keys():
        cities[city[1]] += 1
    # if not add a new index value thingy
    else:
        cities.update({city[1]:1})

print(cities)























# go through the file line by line
for line in file:
    # suck down the city
    line = line.strip()
    thing = line.split(",")
    print(thing)
    # append to the dictionary

# report number of cities in a country
