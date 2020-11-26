#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password= ""
# for letter in range(1, nr_letters + 1):
#   us_letter = random.choice(letters)
#   password += us_letter

# for symbol in range(1, nr_symbols + 1):
#   us_symbol = random.choice(symbols)
#   password += us_symbol

# for number in range(1, nr_numbers + 1):
#   us_number = random.choice(numbers)
#   password += us_number

# print(password)  

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_l = []
for letter in range(1, nr_letters + 1):
  us_letter = random.choice(letters)
  password_l += us_letter

for symbol in range(1, nr_symbols + 1):
  us_symbol = random.choice(symbols)
  password_l += us_symbol

for number in range(1, nr_numbers + 1):
  us_number = random.choice(numbers)
  password_l += us_number

# print(password_l)
random.shuffle(password_l)
# print(password_l)

password1 = ""
for p in password_l:
  password1 += p

print(f"A good password is: {password1}")
