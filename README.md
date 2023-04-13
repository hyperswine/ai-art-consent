# AI Art Consent

Sample code that implements consent in AI Art.

## Model

Train it on 5 images with this metadata format with `python model.py --train`. If the images aren't generated, it will generate them automatically.

Then run it with `python model.py --run`. You should see a generated image with a list of contributing artists like Johnathan, Alex, etc. With a percentage of contribution to the image's overall style.

## Image Format

What the image format `.art` that includes an artist's ID and explicit consent looks like:

<!-- table of metadata for the .art file format -->

|field|value|
|---|---|
|artwork|Baba Yaga|
|artist name|Johnathan Wick|
|ID (SHA2)| f1b843b629acbd8bea6cefb00034f5dd62096f28c2c6ef49ed2685a23185f51f  |
|consent|`true`|
|value per percentage (*optional*)|$0.02|

The value per percentage could be updated automatically based on the artwork's market price, e.g. daily.
