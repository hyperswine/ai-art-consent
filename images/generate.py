# generate images of the .art format

import json
from PIL import Image

def gen_image(input_image_path, output_image_path, metadata):
    """
    input_image_path: path to the input image, e.g., "input_image.png"
    output_image_path: path to the output image, e.g., "output_image.art"
    """

    # generate an image
    # Open an existing PNG image
    # input_image_path = "input_image.png"
    img = Image.open(input_image_path)

    # Metadata to add
    metadata = {
        "artwork": "Baba Yaga",
        "artist_name": "Johnathan Wick",
        "ID (SHA2)": "f1b843b629acbd8bea6cefb00034f5dd62096f28c2c6ef49ed2685a23185f51f",
        "consent": True,
        "value_per_percentage": 0.02
    }

    # Convert the metadata to a JSON string
    metadata_str = json.dumps(metadata)

    # Save the image and metadata as a custom format (e.g., .art for custom image)
    output_image_path = "output_image.art"
    with open(output_image_path, "wb") as f:
        img.save(f, "PNG")
        f.write(metadata_str.encode("utf-8"))
