encoded = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
my_message = "hey there! i am having a lot of fun learning python, you should also give it a try."
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def decode_message(message, offset):
    decoded = ""
    for char in message:
        if char in ALPHABET:
            index = (ALPHABET.index(char) + offset) % len(ALPHABET)
            decoded += ALPHABET[index]
        else:
            decoded += char
    return decoded

# fix the bug in the encode_message function
def encode_message(message, offset):
    encoded = ""
    for char in message:
        if char in ALPHABET:
            index = (ALPHABET.index(char) - offset) % len(ALPHABET)
            encoded += ALPHABET[index]
        else:
            encoded += char
    return encoded

# Decode my custom message
def decode_message_custom(message):
    encoded = ""
    for char in message:
        if char in ALPHABET:
            index = (ALPHABET.index(char)) % len(ALPHABET)
            encoded += ALPHABET[index]
        else:
            encoded += char
    return encoded



encoded_message = encode_message(my_message, 10)
my_message_decoded = decode_message_custom(my_message)
print(encoded_message)
print(my_message_decoded)
