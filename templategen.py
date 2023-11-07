from PIL import Image

width = 16
height = 16

image = Image.new("RGB", (width, height))

# Get the pixel access object
pixels = image.load()

# Set each pixel to a different color
for i in range(width):
    for j in range(height):
        pixels[i, j] = (i * 16, j * 16, (i + j) * 8)

# Save the image
image.save("colorful_board.png")
