from PIL import Image
import hashlib

image = Image.open("colorful_board.png")
pixel_data = list(image.getdata())

hex_pixel_data = [f"{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}" for rgb in pixel_data]

hex_string = hex(int(''.join(hex_num for hex_num in hex_pixel_data)))


address = "123,ExampleStreet,US"
date = "6_11_2023"
camera = "CAN_EOS_R"

address_hex = address.encode().hex()
date_hex = date.encode().hex()
camera_hex = camera.encode().hex()

metadata_string = address_hex + "00" + date_hex + "00" + camera_hex + "01"

metadata_bytes = bytes.fromhex(metadata_string)
metadata_hex = metadata_bytes.hex()

final_hex = metadata_hex + hex_string


hash_object = hashlib.sha256(final_hex.encode())
hash_value = hash_object.hexdigest()

print(hash_value)
