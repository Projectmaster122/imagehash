from PIL import Image, ExifTags
import hashlib

#magic number define
magicnumber = "IMAGEHASH0.0.1"
magicnum_hex = magicnumber.encode().hex()

#open image and get exif
img = Image.open("Canon_40D.jpg")
exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}

#get pixel data and turn it into hex, then take it out of a list
pixel_data = list(img.getdata())
hex_pixel_data = [f"{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}" for rgb in pixel_data]
hex_string = ''.join(hex_num for hex_num in hex_pixel_data)

# address = "123,ExampleStreet,US"
date = exif['DateTime']
camera = exif['Model']

address_hex = address.encode().hex()
date_hex = date.encode().hex()
camera_hex = camera.encode().hex()

metadata_string = date_hex + "00" + camera_hex + "01"

metadata_bytes = bytes.fromhex(metadata_string)
metadata_hex = metadata_bytes.hex()

final_hex = magicnum_hex + "03" + metadata_hex + hex_string


hash_object = hashlib.sha256(final_hex.encode())
hash_value = hash_object.hexdigest()

print(final_hex)
