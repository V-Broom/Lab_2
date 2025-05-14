print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    inputstr = input()
    strlist = inputstr.split(",")
    print(strlist)
    return strlist

def calc_average():
    print("calc_average")
    total = 0.0
    for eachstr in stringlist:
        total = total + float(eachstr)
    average = total / len(stringlist)
    print("Avg = ", average)
    return average

def find_min_max():
    print("find_min_max")
    floatlist = [] // Defining an empty list
    for eachstr in stringlist:
        floatlist.append(float(eachstr))
    floatlist.sort()
    return (floatlist[0], floatlist[-1])

def sort_temperature():
    print("sort_temperature")


def calc_median_temperature():
    print("calc_median_temperature")
    sortedlist = sort_temperature(datalist)
    listLen = len(sortedlist)
    if listLen % 2 == 1:
        median = sortedlist[lostLen/2]
    else:
        median = (sortedliste[listLen//2 -1] + sortedlist[listLen//2])/2
    return median

def main():
    print("Ex 3")
    display_main_menu()
    num_list = get_user_input()
    calc_average(temp_list)