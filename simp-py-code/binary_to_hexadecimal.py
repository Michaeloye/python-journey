# Decimal to Binary
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

def Decimaltohexa(decimal_num):
    string_dec_num = ""
    
    while decimal_num > 0:
        remainder = decimal_num % 16 #to get the remainder of each time you divide the number by 16
        decimal_num = decimal_num // 16 #to get the whole number integer inorder to divide it 
        
        if 0<= remainder <=9:
            string_dec_num += str(remainder)
        else:
            if remainder == 10:
                string_dec_num += "A"
            elif remainder == 11:
                string_dec_num += "B"
            elif remainder == 12:
                string_dec_num += "C"
            elif remainder == 13:
                string_dec_num += "D"
            elif remainder == 14:
                string_dec_num += "E"
            elif remainder == 15:
                string_dec_num += "F"
            
    answer = ""                   
    for j in reversed(string_dec_num):
        answer += j
    return answer

def binary_to_hexadecimal(binary_num):
    dec_answer = binaryToDecimal(binary_num)
    hexa_answer = Decimaltohexa(dec_answer)
    
    return hexa_answer

def main():
    binary_num = input("Please enter in a binary number   ")
    print(binary_to_hexadecimal(binary_num))
main()