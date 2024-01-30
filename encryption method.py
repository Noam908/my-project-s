def encrypt(plaintext, secret_key):
    encrypted_text = ""

    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = secret_key[i % len(secret_key)]
        encrypted_char = chr(ord(char) + ord(key_char))
        encrypted_text += encrypted_char

    return encrypted_text

# קליטת מפתח סודי וטקסט רגיל מהמשתמש
secret_key = input("הזן מפתח סודי: ")
plaintext = input("הזן טקסט רגיל: ")

# ההצפנה והדפסת התוצאה
encrypted_text = encrypt(plaintext, secret_key)
print("הטקסט המוצפן הוא:", encrypted_text)
