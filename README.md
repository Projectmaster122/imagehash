# imagehash
weird image hashing thing that takes image metadata and pixel data and turns it into hex, then hashes it into sha256

heres how the encoded hex string looks like (for Canon_40D.jpg)
1. magic number, in order to identify whether its an IMAGEHASH string, i placed 494d41474548415348302e302e32 (IMAGEHASH0.0.2) with a 03 to identify the end of the segment
2. metadata info:<br />
  a. the program fetches the exif of the image and makes it a list<br />
  b. there are two variables, camera, and date<br />
    b1. for camera, get the Model part of the exif list and add a 00 to seperate it from the date<br />
    b2. for date, get the DateTime part of the exif list and add a 01 to signify end of metadata<br />
   the resulting string for metadata should look like this (for Canon_40D.jpg): 323030383a30...<br />
3. pixel data: this one is pretty self explanatory, get the hex rgb values
pixel data should look like this:
7f6b268470336a5a273c330a29...

in total, the entire thing should look like this:
494d41474548415348302e302e3203323030383a30373a3...

# for bigger images this will take a longer time
