# Encryption of the message
def encrypt(text,shift_amount):
 cipher_text =  ""
 for letter in text:
    if letter in alphabet:
        index = alphabet.index(letter)
        new_index = index + shift_amount
        if new_index > (len(alphabet)-1):
            new_index -= (len(alphabet)-1 +shift_amount-1)
        cipher_text += alphabet[new_index]
    else:
        cipher_text += letter
 print(f"Your Encrypted message is {cipher_text}")

# Decryption of the message
def decrypt(text,shift_amount):
 cipher_text =  ""
 for letter in text:
    if letter in alphabet:
        index = alphabet.index(letter)
        new_index = index - shift_amount
        if new_index < 0:
            new_index += len(alphabet)
        cipher_text += alphabet[new_index]
    else:
        cipher_text += letter
 print(f"Your Decrypted message is {cipher_text}")

def ask():
 ask = input("Do u want to continue Yes or No: ").lower()
 if ask == "no":
    global end
    end = False
    print("GoodBye")
    

import string
alphabet = list(string.ascii_lowercase)
end = True
while end:
    ch = input("Enter Encode to encrypt and decode to decrypt:")
    message = input("enter ur word:")
    shift  =int(input("Enter shift:"))
    if ch == "encode":
        encrypt(message,shift)
        ask()
    elif ch == "decode":
        decrypt(message,shift)
        ask()
    else:
        print("Please Enter Valid input")
        ask()
