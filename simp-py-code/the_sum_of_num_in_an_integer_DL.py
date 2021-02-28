def sum_of_numbers_in_an_integer(num):
    answer = 0
    while num > 0:
        last_num = num % 10
        num = num // 10
        answer += last_num
    print(answer)
def main():
    num = int(input("Enter a number:    " ))
    sum_of_numbers_in_an_integer(num)
main()