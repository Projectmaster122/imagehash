# imagehash
weird image hashing thing that takes image metadata and pixel data and turns it into hex, then hashes it into sha256

heres how the encoded hex string looks like
1. magic number, in order to identify wether its an IMAGEHASH string, i placed 494d41474548415348302e302e31 (IMAGEHASH0.0.1) with a 03 to identify the end of the segment
2. metadata info
