# Question
# Suppose we have values for hours worked and rate of pay (the amount paid per hour) and wish to calculate a person’s regular pay,  overtime pay, and gross pay based on the following: If hours worked is less than or equal to 40, regular pay is calculated by multiplying hours worked by rate of pay and overtime pay is 0. If hours worked is greater than 40, regular pay is calculated by multiplying 40 by the rate of pay and overtime pay is calculated by multiplying the hours  in excess of  40 by the rate of pay by 1.5. Gross pay is calculated by adding regular pay and overtime pay. For example, if hours is  36  and rate is  20  dollars per hour, regular pay is  $720  (36  times  20) and overtime pay is  $0. Gross pay is  $720. And if hours is  50  and rate is  12  dollars per hour, regular pay is  $480  (40  times  12) and overtime pay is  $180  (excess hours  10  times  12  times  1.5). Gross pay is  $660  (480  +  180)
# for proces output check pay_roll.py
import random
import string


def main():
    infile = open("work_file.txt", "a") # open work_file.txt for appending data
    # to randomly generate 100 worker use the code below
    

    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.sample(letters, length))
        return (result_str) # get the text
    
    # write various worker's details into work_file.txt
    for i in range(0, 100):
        infile.write(str(get_random_string(random.randint(3, 8))) + " " + str(get_random_string(random.randint(3, 8))) + " " + str(random.randint(0, 70)) + " "+str(random.randint(30, 100)) + "\n")
    
    
    infile.close
    
   
main()
# this is to generate random words in lower case 
letters =  string.ascii_lowercase
result_str = ''.join(random.sample(letters, random.randint(6,9)))
print(result_str)