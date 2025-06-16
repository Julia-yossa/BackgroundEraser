import rembg
from rembg import remove
from PIL import Image
#from pathlib import Path

# Load the image
input_path = 'input.png'  # Replace with your image path
output_path = "output_image.png"  # The output file will have a transparent background

image = Image.open(input_path)

# Remove the background
result = remove(image)

# Save the result
result.save(output_path)

print("Background removed successfully!")