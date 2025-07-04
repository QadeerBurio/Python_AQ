# How the Program Works:
# Encoding (encode_word function):
#
# If the word has 3 or more characters:
# Moves the first character to the end of the word.
# Adds three random characters at the beginning and end of the word.
# If the word has fewer than 3 characters, it simply reverses the word.
# Decoding (decode_word function):
#
# If the word has fewer than 3 characters, it reverses the word.
# If the word has 3 or more characters:
# Removes the three random characters from the start and end.
# Moves the last character to the beginning of the word.
# Main Function (main function):
#
# Asks the user whether they want to encode or decode a message.
# Depending on the user's choice, it processes the input message accordingly and prints the result.

import random
import string

def generate_random_chars(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def encode_word(word):
    if len(word) >= 3:
        # Remove the first letter and append it at the end
        encoded = word[1:] + word[0]
        # Append three random characters at the start and end
        random_prefix = generate_random_chars(3)
        random_suffix = generate_random_chars(3)
        encoded = random_prefix + encoded + random_suffix
    else:
        # Simply reverse the string
        encoded = word[::-1]
    return encoded

def decode_word(word):
    if len(word) < 3:
        # Reverse the string
        decoded = word[::-1]
    else:
        # Remove 3 random characters from start and end
        word = word[3:-3]
        # Remove the last letter and append it to the beginning
        decoded = word[-1] + word[:-1]
    return decoded

def main():
    choice = input("Do you want to code or decode? (Enter 'code' or 'decode'): ").strip().lower()

    if choice == 'code':
        message = input("Enter the message to encode: ").strip()
        encoded_message = ' '.join(encode_word(word) for word in message.split())
        print(f"Encoded Message: {encoded_message}")
    elif choice == 'decode':
        message = input("Enter the message to decode: ").strip()
        decoded_message = ' '.join(decode_word(word) for word in message.split())
        print(f"Decoded Message: {decoded_message}")
    else:
        print("Invalid choice. Please enter 'code' or 'decode'.")

if __name__ == '__main__':
    main()




#
# st = input("Enter message")
# words = st.split(" ")
# coding = input("1 for Coding or 0 for Decoding")
# coding = True if (coding == "1") else False
# print(coding)
# if (coding):
#     nwords = []
#     for word in words:
#         if (len(word) >= 3):
#             r1 = "dsf"
#             r2 = "jkr"
#             stnew = r1 + word[1:] + word[0] + r2
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))
#
# else:
#     nwords = []
#     for word in words:
#         if (len(word) >= 3):
#             stnew = word[3:-3]
#             stnew = stnew[-1] + stnew[:-1]
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))




