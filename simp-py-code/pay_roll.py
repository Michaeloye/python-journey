# Question
# Suppose we have values for hours worked and rate of pay (the amount paid per hour) and wish to calculate a person’s regular pay,  overtime pay, and gross pay based on the following: If hours worked is less than or equal to 40, regular pay is calculated by multiplying hours worked by rate of pay and overtime pay is 0. If hours worked is greater than 40, regular pay is calculated by multiplying 40 by the rate of pay and overtime pay is calculated by multiplying the hours  in excess of  40 by the rate of pay by 1.5. Gross pay is calculated by adding regular pay and overtime pay. For example, if hours is  36  and rate is  20  dollars per hour, regular pay is  $720  (36  times  20) and overtime pay is  $0. Gross pay is  $720. And if hours is  50  and rate is  12  dollars per hour, regular pay is  $480  (40  times  12) and overtime pay is  $180  (excess hours  10  times  12  times  1.5). Gross pay is  $660  (480  +  180)

# open the file for reading

read_infile = open("work_file.txt", "r") 

# open another file so that the data in work_file.txt after being processed can be written in pay_roll.txt
outfile = open("pay_roll.txt", "a")
outfile.write("Name       " + "Hours       " + "Rate       " + "Regular       " + "Overtime       " + "Net       " + "\n") 


for line in read_infile:
    details = line.split() # splits words in a line in to a list
    first_name = details[0] # the first data in the list is the employee's first name
    last_name = details[1] # the second data in the list is the employee's second name
    hours_worked = details[2] # the third data in the list is the number of hours the employee worked for
    rate_of_pay = details[3] # the fourth data in the list is the rate of pay
    
    def regular(time, rate):
        if int(time) <= 40:
            return (int(time) * int(rate))
        elif int(time) > 40:
            return(40 * int(rate)) 
    def overtime(time, rate):
        if int(time) <= 40:
            return( 0 )
        elif int(time) > 40:
            return((int(time) - 40) * int(rate) * 1.5)
    Net = regular(hours_worked, rate_of_pay) + overtime(hours_worked, rate_of_pay)
    outfile.write(first_name + " " + last_name + "            " + hours_worked + "            " + rate_of_pay + "      " + str(regular(hours_worked, rate_of_pay)) + "            " + str(overtime(hours_worked, rate_of_pay)) + "            " + str(Net) + "\n")
read_infile.close()
outfile.close()