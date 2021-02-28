#raise to power
base_num = int(input("Enter the base number: "))
pow_num = int(input("Enter the power number: "))
def raise_to_power(base_num, pow_num):
    result = 1
    for num in range(pow_num):
        '''since the pow_num is what the base_num will multiply itself by.
        so pow_num if 3 will cause the code loop 3 times that means 1*4
        for pow_num 1 then pow_num 2 the result will be stored as 4 for pow_num
        1 then run again present result 4  4*4 for pow_num 3 16*4'''
        result = result * base_num
    return result
print(raise_to_power(base_num, pow_num))