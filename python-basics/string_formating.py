#Name: Nailah Wanjiku
#Date: 12/2/2026
#string_formating

#get string length
sentence = "i play games"

string_length = len(sentence)

print(f"the length is:{string_length}")

#spliting a string
sentence_2 = "mathematics physics"
split = sentence_2.split(" ")

print(f"the first subject is:", split[0])


#make everything CAPS
mpesa_code = "ub21ddsfhg"

capitalized = mpesa_code.upper()

print("new mpesa code: ", capitalized)


#make everything lower
mpesa_code = "UB32ghjS"

lower_case = mpesa_code.lower()

print("new mpesa code: ", lower_case)


#replacing characters in a string

balance = "100kes"
amount_added = "50kes"

cleaned_balance = balance.replace("kes", "")
cleaned_amount_added = amount_added.replace("kes", "")


print("cleaned balance: ", cleaned_amount_added)

#finding new balance
new_balance = int(cleaned_balance) + int(cleaned_amount_added)

print("The new balance is: ", new_balance)






