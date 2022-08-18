from Crypto.Cipher import AES

print("ADVANCED ENCRYPTION STANDARD \n")

#Key has to be either 16, 24 or 32 bytes
def padKey(key):
    while len(key) % 8 != 0:
        key += " "
    return key

#Plain text has to be in multiple of 16 bytes
def padText(text):
    while len(text) % 16 != 0:
        text += " "
    return text

plainText = input("Write your message: ")
plainText = padText(plainText)
key = input("Input the key: ")
key = padKey(key) #Asking for the key of choice

#Checking to see if the bytes condition are met
if (len(key) <= 16 & len(key) >= 32):
    print("Key must be between 16 and 32 bytes")
cipher = AES.new(key, AES.MODE_CBC)
cipherText = cipher.encrypt(plainText)
print(f"Cipher Text: {cipherText.encode('hex')}")

decryptText = cipher.decrypt(cipherText)
print(f"Decrypted Text: {decryptText}")