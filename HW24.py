# Madison Thorburn-Gundlach
# Due November 15, 2015
# hw 24 -- do stuff with functions and numpy and python.  Further comments below.

def main():
    def why_would_you_do_this():
        y = "no" # enclosed
        return y
    x = "no" # local
    z = len(x) # built-in
    return "blah"

joe = "joe" # global

def find_frequency(val,list_of_vals):
    freq = 0
    for val in list_of_vals:
        freq += 1
    return freq

def bar_graph(values_list):
    import numpy
    import pylab
    minimum = min(values_list)
    maximum = max(values_list)
    rang = numpy.ceil(((maximum - minimum)/10)-1)
    x_values = []
    y_values = [0,0,0,0,0,0,0,0,0,0]

    # establish x_values as 0*rang, 1*rang, ..., 10* rang
    thing = 0
    for i in range(0,11):
        thing += 1
        x_values.append(rang*i + thing)

    # go through every value in values_list, if it's between the rangs then append to appropriate thing
    for val in values_list:
        if x_values[0] <= val < x_values[1]:
            y_values[0] += 1
        elif x_values[1] <= val < x_values[2]:
            y_values[1] += 1
        elif x_values[2] <= val < x_values[3]:
            y_values[2] +=1
        elif x_values[3] <= val < x_values[4]:
            y_values[3] += 1
        elif x_values[4] <= val < x_values[5]:
            y_values[4] += 1
        elif x_values[5] <= val < x_values[6]:
            y_values[5] += 1
        elif x_values[6] <= val < x_values[7]:
            y_values[6] += 1
        elif x_values[7] <= val < x_values[8]:
            y_values[7] += 1
        elif x_values[8] <= val < x_values[9]:
            y_values[8] += 1
        elif x_values[9] <= val < x_values[10]:
            y_values[9] += 1


    pylab.plot(x_vals, y_vals)
    pylab.show()
