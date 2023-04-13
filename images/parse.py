import json
from PIL import Image
from io import BytesIO


def parse_art_file(input_image_path = "output_image.art") -> Image.Image:
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

    # Return the image
    return img


if __name__ == "__main__":
    parse_art_file("output_image.art")
