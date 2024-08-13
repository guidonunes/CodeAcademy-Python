encoded = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
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

decoded_message = decode_message(encoded, 10)
print(decoded_message)
