print("Caesari nihe")

plaintext = input("Sisestage tekst: ")
shift = int(input("Sisestage nihke suurus: "))

ciphertext = ""
for letter in plaintext:
    if letter.isalpha():
        ciphertext += chr((ord(letter.lower()) - ord('a') + shift) % 26 + ord('a'))
    else:
        ciphertext += letter

print("Krüpteeritud tekst:", ciphertext)
