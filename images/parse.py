import json
from PIL import Image
from io import BytesIO


def extract_art_metadata(input_image_path="output_image.art"):
    with open(input_image_path, "rb") as f:
        data = f.read()

    metadata_start = data.rfind(b'{')
    metadata_end = data.rfind(b'}')

    print("start =", metadata_start)
    print("end =", metadata_end)

    # Load the image
    image_data = data[:metadata_start]

    # Load the metadata
    metadata_str = data[metadata_start:].decode("utf-8")
    metadata = json.loads(metadata_str)

    # Print the metadata
    print(metadata)

    # Return the image
    return metadata, image_data


if __name__ == "__main__":
    art_format_metadata, img_bytes = extract_art_metadata("output_image.art")
    # then take the png data for use?
