# Write a funtion that parses a binary number as a string into a decimal integer. Use the function header:
#def binaryToDecimal(binary string):
#For example, binary string 10001 is 17 (1*2^4 + 0*2^3 + 0*2^2 + 0*2^1 + 1*2^0 = 17). So, binaryToDecimal("10001") returns 17
#Write a tes program that prompts the user to enter a binary string and displays the corresponding decimal integer value.


def binaryToDecimal(binarystring):
    
    num_reverse = reversed(binarystring) # reverse the number so that the power will be able to start from 0 for the last digit(1011)
    power = 0
    answer = 0
    for k in binarystring:
        if int(k)>1:
            print("Please enter a number in binary form.\n")
        else:
            for i in num_reverse:
                decimal_num = (int(i) * (2**power)) # (1*2^0 + 1*2^1 + 0*2^2 + 1*2^3)  
                answer += decimal_num 
                power += 1
    return(answer)
def main():
    num = input("Enter a number in binary:  ")
    print(binaryToDecimal(num))
main()



def DecimalTobinary(decimalstring):
    string_dec_num = ""
    answer = ""
    while decimalstring > 0:
        remainder = decimalstring % 2
        decimalstring = decimalstring // 2
        string_dec_num += str(remainder)
    for j in reversed(string_dec_num):
        answer += j
    return answer
def main():
    dec_num = int(input("Please Enter a decimal number: "))
    print(DecimalTobinary(dec_num))

main()