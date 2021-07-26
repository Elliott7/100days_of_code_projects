"""
Project Number Eight - Caeser Cipher
Make a selection whether you would like to encrypt or decrypt.
Select the amount of shift positions you would like.
Enter your message the encryption/decryption will take place.
"""


def logo():
    log = """           
     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP'''''''  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
               88             88                                 
               ""             88                                 
                              88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                  88                                             
                  88           
    """
    print(log)


alpha_string = 'abcdefghijklmnopqrstuvwxyz123456789-=!@#$%^&*()_+;",./<>?| '

# Provides a numbered dictionary of the alphabet
alph_dict = {}
for number, letter in enumerate(alpha_string):
    alph_dict[letter] = number


# Returns a dictionary that has the alphabet numbers shifted according to how many places you specify
def get_encrypted_dict(input_string, num_letters_shifted):
    """
    Encrypts the dictionary based on the letters in the alpha_string and the number of letters requested to shift

    :param input_string: String containing all the characters of the alphabet/numbers/symbols
    :param num_letters_shifted: How far you want the result shifted
    :return shifted_dict: dictionary that has the alphabet numbers shifted according to how many places you specify
    """
    new_string = input_string[num_letters_shifted:] + input_string[:num_letters_shifted]
    shifted_dict = {}
    for num, let in enumerate(new_string):
        shifted_dict[num] = let

    return shifted_dict


def get_reverse_dict(input_dict):
    return dict([(value, key) for key, value in input_dict.items()])


def hide_message(message, shift_amount=5):
    """
    Encrypts your message

    :param message: Message you would like to encrypt
    :param shift_amount: How much you would like to shift the result by
    :return text: Encrypted message
    """
    text = ''
    new_cypher = get_encrypted_dict(alpha_string, shift_amount)
    for x in message.lower():
        text = text + new_cypher[alph_dict[x]]

    return text


def unhide_message(message, shift_amount=5):
    """
    Decrypts your message

    :param message: Message you would like to decrypt
    :param shift_amount: How much you would like to shift the result by
    :return text: decrypted message
    """
    text = ''
    reverse_cypher = get_reverse_dict(get_encrypted_dict(alpha_string, shift_amount))
    reverse_base_dict = get_reverse_dict(alph_dict)
    for x in message.lower():
        key = reverse_cypher[x]
        text = text + reverse_base_dict[key]
    return text


def main():
    logo()

    while True:
        get = input("Would you like to encrypt or decrypt? 'E' or 'D'\n")
        try:
            intervals = int(input("How many intervals would you like to shift your cypher by?\n"))
            if intervals >= len(alpha_string) or intervals <= (len(alpha_string) - len(alpha_string)*2):
                print(f"Please select a number below {len(alpha_string)}"
                      f" and above {(len(alpha_string) - len(alpha_string)*2)}")
                continue

        except ValueError:
            print(f"Please select a number below {len(alpha_string)}")
            continue

        if get.lower() == 'e':
            secret_message = input("Enter a message: \n")
            print(f"The secret message is: {secret_message}")
            hidden = hide_message(secret_message, intervals)
            print(f"The encrypted message is: {hidden}")

        elif get.lower() == 'd':
            secret_message = input("Enter a message: \n")
            print(f"The secret message is: {secret_message}")
            unhidden = unhide_message(secret_message, intervals)
            print(f"The decrypted message is: {unhidden}")

        else:
            print("Invalid response, please enter either 'E' or 'D' try again")
            continue

        cont = input("Would you like to use this again? 'Y' or 'N'\n")

        if cont.lower() == "y":
            continue
        else:
            print("Goodbye")
            break


if __name__ == "__main__":
    main()
