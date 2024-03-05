# Improving the Caesar cipher
'''
You are already familiar with the Caesar cipher, and this is why we want you to improve the code we showed you recently.

The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on.
Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case)
and all non-alphabetical characters should remain untouched.

Your task is to write a program which:

asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25
-note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
prints out the encoded text.
'''

# Prompt (and reprompt the user until they in put a valid message) the user for a message
is_message = False
while not is_message:
    message = input("Enter a message: ")
    
    # Confirm if the message is valid
    message_len = len(message)
    message_split_len = len(message.split())
    if message_len > 0 and message_split_len:
        is_message = True

# Prompt the user for the shift value (until they input the right value)
is_valid = False
while not is_valid:
    try:
        shift_value = int(input("Enter a shift value: "))
        if shift_value >= 1 and shift_value <= 25:
            is_valid = True
    except:
        print("Shift value is invalid!")
        
# Shifting the message
shifted_message = ''
for char in message:
    
    if char.isalpha():
        if char.islower():
            ord_value = ord(char) + shift_value
            
            # If the value overflows then get its modulus value
            if ord_value > 122:
                ord_value %= 122
                ord_value += 96
            char = chr(ord_value)
        else:
            ord_value = ord(char) + shift_value
            
            # If the value overflows then get its modulus value
            if ord_value > 90:
                ord_value %= 90
                ord_value += 64
            char = chr(ord_value)
    shifted_message += char
print(shifted_message)