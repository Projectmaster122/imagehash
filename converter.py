from PIL import Image, ExifTags
import hashlib

def hashmaker():
    #magic number define
    magicnumber = "IMAGEHASH0.0.2"
    magicnum_hex = magicnumber.encode().hex()

    #open image and get exif
    imgname = "Canon_40D.jpg"
    img = Image.open(imgname)
    exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}

    #get pixel data and turn it into hex, then take it out of a list
    pixel_data = list(img.getdata())
    hex_pixel_data = [f"{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}" for rgb in pixel_data]
    hex_string = ''.join(hex_num for hex_num in hex_pixel_data)

    # TODO: address = exif['Address']
    date = exif['DateTime']
    camera = exif['Model']
    #hexify exif
    date_hex = date.encode().hex()
    camera_hex = camera.encode().hex()
    #make metadata
    metadata_string = date_hex + "00" + camera_hex + "01"
    # hexify
    metadata_bytes = bytes.fromhex(metadata_string)
    metadata_hex = metadata_bytes.hex()
    # make final hex output
    final_hex = magicnum_hex + "03" + metadata_hex + hex_string

    #hash
    hash_object = hashlib.sha256(final_hex.encode())
    hash_value = hash_object.hexdigest()

    main(date, camera, date_hex, camera_hex, metadata_hex, final_hex, hash_value, magicnumber, magicnum_hex, imgname)

def main(date, camera, date_hex, camera_hex, metadata_hex, final_hex, hash_value, magicnumber, magicnum_hex, imgname):
    while True:
        cmd = input(">")
        if cmd == "ret":
            exit(0)
        elif cmd == "date":
            print(f"{date_hex}/{date}")
        elif cmd == "camera":
            print(f"{camera_hex}/{camera}")
        elif cmd == "meta_hex":
            print(f"{metadata_hex}")
        elif cmd == "final_hex":
            print(f"{final_hex}")
        elif cmd == "hash_val":
            print(f"{hash_value}")
        elif cmd == "magicnumber":
            print(f"{magicnum_hex}/{magicnumber}")
        elif cmd == "img":
            print(f"{imgname}")

if __name__ == "__main__":
    hashmaker()
