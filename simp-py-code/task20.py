# Question: Assumming that we have some email addresses in the "username@companyname.com" format, please write a program to print the company name of a given
# email address. Both user names and company names are composed of letters only.
# Example:
# If the following email address is given as inputs to the program: john@google.com Then, the output of the program should be: google in case of input data
# being supplied to the question, it should be assumed to be a console input.
# Hints: 
# Use \w to match letters.
email = input("please enter an email address: ")

start = email.index("@")
end = email.index(".com")
company_name = email[start+1 : end]
print("The name of the company from the address given is " + company_name)
