# Project image unto sprite stack:
from PIL import Image

# Open image and access it's pixel data and size:
image = Image.open("image.png")
image_pixels = image.load()
size = width, height = image.size
name_digit_length = len(str(height))

for y in range(height):
    # Open the model image of the sprite stack and access it's data:
    # Model image should have the same width as the original image:
    output_layer = Image.open("sprite stack model.png")
    output_layer = output_layer.convert("RGBA")
    output_pixels = output_layer.load()
    output_size = output_width, output_height = output_layer.size

    # Draw the image unto the opaque pixels:
    for x in range(width):
        for y2 in range(output_height):
            if not output_pixels[x, y2][3] == 0:
                output_pixels[x, y2] = image_pixels[x, y]
    # Place the proper amount of 0's in front of the digit:
    digit = y if len(str(y)) == name_digit_length else "0"*(name_digit_length - len(str(y))) + str(y)
    output_layer.save(f"Sprite Stack Frames/sprite stack {digit}.png")