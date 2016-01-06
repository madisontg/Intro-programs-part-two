# Madison Thorburn-Gundlach
# highest mileage data
# from http://www.fueleconomy.gov/FEG/download.shtml

def create_mileage_list(epa_file):
    """Create a list of cars and mileage from epa_file."""
    mileage_list = []

    for line in epa_file:          
        if line[0:5] == 'CLASS' or 'VAN' in line or 'PICKUP' in line:   
            continue                 
        line_list = line.split(',')
        
        # create tuple: (city mileage, hwy mileage, make, model)
        car_tuple = (int(line_list[8]), int(line_list[9]), line_list[1], line_list[2])
        mileage_list.append(car_tuple)
    return mileage_list

def average_city_hwy_by_maker(mileage_list):
    avgcity_avghwy_make = []
    make_list = []
    
    for car in mileage_list:
        if car[2] not in make_list:
            make_list.append(car[2])
    
    maker_city_hwy = []
    for make in make_list:
        # reset total counters for each make
        total_mpg_city = 0
        total_mpg_hwy = 0
        cars_number = 0
        # add to totals
        for car in mileage_list:
            if car[2] == make:
                cars_number +=1
                total_mpg_city += car[0]
                total_mpg_hwy += car[1]
        # add new make data to end-result list
        maker_city_hwy.append([make, total_mpg_city/cars_number, total_mpg_hwy/cars_number, cars_number])
        # sort it just for kicks, so that the end-result table is in alphabetical order
        maker_city_hwy.sort()
    return maker_city_hwy

##############################################
epa_file = open("epaData.csv", "r")
mileage_list = create_mileage_list(epa_file)
relevant_data = average_city_hwy_by_maker(mileage_list)
# print headers
print("{:20} {:20} {:20}".format("MAKER","CITY MPG AVERAGE","HWY MPG AVERAGE"))
# print spacers (for aesthetic reasons it looks better this way trust me)
print("{:20} {:20} {:20}".format("-----","----------------","---------------"))
# loop through list to print each make and it's data
for thing in relevant_data:
    print("{:20} {:<20.2f} {:<20.2f}".format(thing[0],thing[1],thing[2]))


