def caesar_encrypt(text, k):
    ciphertext = ""

    for char in text:
        if char.isalpha():  # Kiểm tra có phải chữ cái không
            # Phân biệt chữ hoa và chữ thường
            if char.isupper():
                # Dịch ký tự theo mã ASCII
                new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            ciphertext += new_char
        else:
            # Nếu không phải chữ cái thì giữ nguyên
            ciphertext += char

    return ciphertext

k = 24
plaintext = "HuynhDoanKimHoa"

# Gọi hàm 
ciphertext = caesar_encrypt(plaintext, k)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
