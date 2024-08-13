ALPHABET = "abcdefghijklmnopqrstuvwxyz"
encoded = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"


decoded = ""
for char in encoded:
  if char in ALPHABET:
    index = (ALPHABET.index(char) + 10) % len(ALPHABET)
    decoded += ALPHABET[index]
  else:
    decoded += char
print(decoded)
