# Ceaser cipher with variable key
# based on https://inventwithpython.com/chapter14.html
MAX_SHIFT = 26

def getMode():
    while True:
        print("Choose your mode:\n 1. Encrypt \n 2. Decrypt")
        mode = input().lower()
        if mode in 'encrypt 1 decrypt 2'.split():
            return mode
        else:
            print("Please enter a valid mode, or 1 or 2.")

def getKey():
    key = 0
    while True:
        print("Please enter your key (1-26):")
        key = int(input())
        if key >= 1 and key <= MAX_SHIFT:
            return key

def getMessage():
    print("Enter your message to encrypt/decrypt:")
    return input()

def translate(mode, key, message):
    if mode[0] == 'e' or '1':
        print("Encrypt mode.")
    elif mode [0] == 'd' or '2':
        print("Dncrypt mode.")
        key = -key

    translate = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

            if symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translate += chr(num)
        else:
            translate += symbol
    return translate

mode = getMode()
key = getKey()
message = getMessage()
out = translate(mode, key, message)
print(out)
