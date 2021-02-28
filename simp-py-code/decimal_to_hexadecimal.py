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
                
def main():
    dec_num = int(input("Please Enter a decimal number: "))
    print(Decimaltohexa(dec_num))

main()