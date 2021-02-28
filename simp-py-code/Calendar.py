def print_month(year, month):
    title_of_calendar(year, month)
    print_month_body(year, month)
def title_of_calendar(year, month):
    print("     " + get_month_name(month) +" "+ str(year))
    print("--------------------------------------")
    print(" Sun  Mon  Tue  Wed  Thur  Fri  Sat ")
def get_month_name(month):
    
    if month == 1:
        month_name = "January"
    elif month == 2:
        month_name = "February"
    elif month == 3:
        month_name = "March"
    elif month == 4:
        month_name = "April"
    elif month == 5:
        month_name = "May"
    elif month == 6:
        month_name = "June"
    elif month == 7:
        month_name = "July"
    elif month == 8:
        month_name = "August"
    elif month == 9:
        month_name = "September"
    elif month == 10:
        month_name = "October"
    elif month == 11:
        month_name = "November"
    else:
        month_name = "December"
    return month_name
        
def print_month_body(year, month):
    startday = get_start_day(year, month)
    number_of_days_in_month = get_number_of_days_in_a_month(year, month)
    i = 0
    for i in range(0, startday):
        print("    ", end = " ")
    for i in range(1, number_of_days_in_month + 1):
        print(format(i, "4d"), end= " ")
        
        if (i + startday) % 7 == 0:
            print()
def get_start_day(year, month):
    start_day_starting_from_jan1_1800 = 3
    total_num_of_days = get_number_of_days(year, month)
    return ((total_num_of_days + start_day_starting_from_jan1_1800)%7)
    
def get_number_of_days(year, month):
    start_year = 1800
    days = 0
    for j in range(start_year, year):   #Possible bug
        if is_leap_year(j):
            days += 366
        else:
            days += 365
    for i in range(1, month):
        days += get_number_of_days_in_a_month(year, i)
    return days

def get_number_of_days_in_a_month(year, month):
    leap_year = is_leap_year(year)
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        num_of_days_in_month = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        num_of_days_in_month = 30
    elif month == 2 and leap_year:
        num_of_days_in_month = 29
    elif month == 2 and not(leap_year):
        num_of_days_in_month = 28
    return num_of_days_in_month
def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        leap_year = True
    else:
        leap_year = False
    return leap_year 
        
def main():
    year = int(input("Enter year:   "))
    month = int(input("Enter month as number (1-12):   "))
    if year<1800:
        print("Please Enter year above 1800")
    if month < 1 or month > 12:
        print("Please Enter month between 1 and 12")
    else:
        print_month(year, month)
main()
    
    
