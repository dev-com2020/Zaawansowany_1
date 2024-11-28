import struct

# bin_data = b'\x01\x00\x00\x00\xcd\xcc\xcc\x3d'

# # Unpack the data into a tuple of two floats
# x, y = struct.unpack('if', bin_data)
# print(x, y)

rec_format = '10si'
size = struct.calcsize(rec_format)
print(size)



# with open('D:\projekty\Z1\PythonZ1\slick.bin', 'rb') as f:
#     while True:
#         data = f.read(struct.calcsize(rec_format))
#         if not data:
#             break
#         record = struct.unpack(rec_format, data)
#         print(record)

# bi_data = b'\x01\x00\x00\x00Atomek  '
# user_format = 'i c 7s'
# user_id, flag, username = struct.unpack(user_format, bi_data)

# username = username.decode('utf-8').strip()
# print(f"User ID = {user_id}, Flag = {flag.decode('utf-8')}, Username = {username}")


b_data = b'\x00\x01'
little_endian = struct.unpack('<H', b_data)
print(little_endian)
big_endian = struct.unpack('>H', b_data)
print(big_endian)