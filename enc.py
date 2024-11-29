import base64

# text = "Hello 🫥"
# utf8 = text.encode('utf-8')
# print(utf8)
# utf16 = text.encode('utf-16')
# print(utf16)

# decoded_text = utf8.decode('utf-8')
# print(decoded_text)

# print(ord('🫥'))
# print(ord('A'))
# print(chr(129421))
# print(chr(65))

# tekst = "\xf0\x9f\xab\xa5"
# tekst2 = "\u0105\u0041\U0001F60A"
# print(tekst)
# print(tekst2)

# with open('utf8.txt', 'w', encoding='utf-8') as f:
#     f.write(text)

# with open('utf8.txt', 'r', encoding='utf-8') as f:
#     con = f.read()
# print(con)

# binary_data = b'\xf0\x9f\xab\xa5'
# with open('utf8.txt', 'wb') as f:
#     f.write(binary_data)

# with open('utf8.txt', 'rb') as f:
#     con = f.read()
# print(con)

# for b in binary_data:
#     print(b)

binary = b'hello'
encoded = base64.urlsafe_b64encode(binary)
encoded2 = base64.b32encode(binary)
print(encoded)
print(encoded2)

decoded = base64.urlsafe_b64decode(encoded)
print(decoded)
# test komentarza