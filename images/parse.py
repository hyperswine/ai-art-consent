import json
from PIL import Image
from io import BytesIO


def parse_art_file(input_image_path="output_image.art"):
    with open(input_image_path, "rb") as f:
        data = f.read()

    # Find the start of the metadata
    # can you start from the end of the file?
    metadata_start = data.rfind(b'{')
    metadata_end = data.rfind(b'}')

    # res_start = list(filter(lambda x: x == b'{', data))
    # print(res_start)

    print("start =", metadata_start)
    print("end =", metadata_end)

    # exit()

    # Load the image
    image_data = data[:metadata_start]
    # img = Image.open(BytesIO(image_data))

    # Load the metadata
    metadata_str = data[metadata_start:].decode("utf-8")
    metadata = json.loads(metadata_str)

    # Print the metadata
    print(metadata)

    # Return the image
    # return img


if __name__ == "__main__":
    parse_art_file("output_image.art")
