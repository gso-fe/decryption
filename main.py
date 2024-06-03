# main.py

# import ...
# import ...

def main():
    print("Willkommen zum Verschlüsselungs-Tool")
    print("Wählen Sie ein Verfahren:")
    print("1. Cäsar-Verschlüsselung")
    print("2. Vigenère-Verschlüsselung")
    
    choice = input("Ihre Wahl: ")
    
    if choice == "1":
        caesar_encrypt_decrypt()
    elif choice == "2":
        vigenere_encrypt_decrypt()
    else:
        print("Ungültige Wahl. Bitte starten Sie das Programm erneut.")

def caesar_encrypt_decrypt():
    message = input("Geben Sie die Nachricht ein: ")
    shift = int(input("Geben Sie die Verschiebung ein (z.B. 3): "))
    action = input("Möchten Sie verschlüsseln oder entschlüsseln? (v/e): ")
    
    if action == 'v':
        encrypted_message = caesar_cipher.encrypt(message, shift)
        print(f"Verschlüsselte Nachricht: {encrypted_message}")
    elif action == 'e':
        decrypted_message = caesar_cipher.decrypt(message, shift)
        print(f"Entschlüsselte Nachricht: {decrypted_message}")
    else:
        print("Ungültige Aktion.")

def vigenere_encrypt_decrypt():
    message = input("Geben Sie die Nachricht ein: ")
    key = input("Geben Sie den Schlüssel ein: ")
    action = input("Möchten Sie verschlüsseln oder entschlüsseln? (v/e): ")
    
    if action == 'v':
        encrypted_message = vigenere_cipher.encrypt(message, key)
        print(f"Verschlüsselte Nachricht: {encrypted_message}")
    elif action == 'e':
        decrypted_message = vigenere_cipher.decrypt(message, key)
        print(f"Entschlüsselte Nachricht: {decrypted_message}")
    else:
        print("Ungültige Aktion.")

if __name__ == "__main__":
    main()
