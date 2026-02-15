#Name: Nailah Wanjiku
#Date: 12/2/2026
#string_formating

#capitalize
sentence = "confirmed:"
capitalized = sentence.upper()

print(" ", capitalized)

#splitting string
sentence = "You have received 50.0kes from Phillip"
split = sentence.split("  ")

print(f" ", split[0])


#junior developers
#"CONFIRMED : You have received 50kes from Phillip "

balance = "70.02kes"
amount_added = "50kes"

cleaned_balance = float (balance.replace("kes", ""))
cleaned_amount_added =float (amount_added.replace("kes", ""))

print("cleaned balance: ", cleaned_amount_added)

#previous balance
previous_balance = "balance"

print("Previous balance: ", balance)

#finding new balance
new_balance = (cleaned_balance) + (cleaned_amount_added)

print("Your new balance is: ", new_balance)


