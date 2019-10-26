alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjklmnopqrstuvwxyzabcdefghjklmnopqrstuvwxyz01234567890123456789"
a=input("Enter your sentence:")
key=int(input("Enter your key:"))
b=""
for letter in a:
    position=alphabet.find(letter)
    newPosition=position+key
    if letter in alphabet:
        b=b+alphabet[newPosition]
    else:
        b=b+letter
print("Your sentence:", b)