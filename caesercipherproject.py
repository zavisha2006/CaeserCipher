# Imports alphabet
import string
# List to update the new characters with
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
# Number for how far to shift letters
shift = 0
# Checks if the input is encrypt or decrypt
while True:
    typeofcipher = input('Type encrypt or decrypt:').lower()
    if typeofcipher == 'encrypt' or typeofcipher == 'decrypt':
        break
    print('Invalid input. Please try again.')
userstring = list(input('Input the string:'))
# Checks if the input is 1 to 10
while True:
    usershift = int(input('Input the shift from 1 to 10:'))
    if 1 <= usershift <= 10:
        break
    print('Invalid input, please try again.')
converteduserlist = []
converteduserstring = ''

# If the user wants to encrypt
if (typeofcipher == 'encrypt'):
    for i in userstring:
        # Checks if the character is not  a letter, then ignores it
        try:
        # Finds the index according to the character, then compares the character with the character of the list using the index, used to find if it is uppercase or lowercase
            b = alphabet_lower.index(i)
            if i == alphabet_lower[b]:
            # If the index number will go above 25, it will minus 26 
                while alphabet_lower.index(i) + usershift > 25:
                    usershift -= 26
                i = alphabet_lower.index(i)
                i = alphabet_lower[i + usershift]
            converteduserlist.append(i)
        except ValueError:
            try:
                while alphabet_upper.index(i) + usershift > 25:
                    usershift -= 26
                i = alphabet_upper.index(i)
                i = alphabet_upper[i + usershift]
                converteduserlist.append(i)
            except ValueError:
                converteduserlist.append(i)

if (typeofcipher == 'decrypt'):
    for i in userstring:
        # Checks if the character is not a letter, then ignores it
        try:
            # Finds the index according to the character, then compares the character with the character of the list using the index, used to find if it is uppercase or lowercase
            b = alphabet_lower.index(i)
            if i == alphabet_lower[b]:
                while alphabet_lower.index(i) - usershift > 25: 
                    usershift -= 26
                i = alphabet_lower.index(i)
                i = alphabet_lower[i - usershift]
                converteduserlist.append(i)
        except ValueError:
            try:
                while alphabet_upper.index(i) - usershift > 25: 
                    usershift -= 26
                i = alphabet_upper.index(i)
                i = alphabet_upper[i - usershift]
                converteduserlist.append(i)
            except ValueError:
                converteduserlist.append(i)
converteduserstring = ''.join(converteduserlist)
print(converteduserstring)