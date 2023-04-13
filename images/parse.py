import json
from PIL import Image
from io import BytesIO

# Read the custom image format (e.g., .cimg)
input_image_path = "output_image.cimg"
with open(input_image_path, "rb") as f:
    data = f.read()

# Find the start of the metadata
metadata_start = data.find(b'{')

# Load the image
image_data = data[:metadata_start]
img = Image.open(BytesIO(image_data))

# Load the metadata
metadata_str = data[metadata_start:].decode("utf-8")
metadata = json.loads(metadata_str)

# Print the metadata
print(metadata)
