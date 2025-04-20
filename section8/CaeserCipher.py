alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def encrypt():
    encrypted_text = ""

    for char in text:
        if char == ' ':
            encrypted_text += ' '
            continue
        shifted_index = alphabet.index(char) + shift

        shifted_index %= len(alphabet)

        encrypted_text += alphabet[shifted_index]

    print(encrypted_text)

def decode():
    decrypted_text = ""

    for char in text:
        if char == ' ':
            decrypted_text += ' '
            continue
        shifted_index = alphabet.index(char) - shift

        if shifted_index > len(alphabet):
            shifted_index = shifted_index - len(alphabet)

        decrypted_text += alphabet[shifted_index]

    print(decrypted_text)

if direction == "encode":
    encrypt()
elif direction == "decode":
    decode()
else:
    print("Type a valid option!")