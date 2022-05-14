#Import required Image library
from PIL import Image
from PIL import ImageDraw, ImageFont
import os

files_formats = ['.jpg', '.jpeg', '.png', '.webp']
size_1080 = (1080,1080)

os.mkdir('img')

for x in os.listdir('.'):
    fn, fext = os.path.splitext(x)

    if fext.lower() in files_formats:
        # Create an Image Object from an Image
        img = Image.open(x)
        img = img.resize(size_1080)
        img = img.convert('L')
        width, height = img.size

        # Draw a watermarker
        draw = ImageDraw.Draw(img)
        text = "10R"

        font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 75)
        textwidth, textheight = draw.textsize(text, font)

        # calculate the x,y coordinates of the text
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        # draw watermark in the bottom right corner
        draw.text((x, y), text, font=font)

        img.save(f'img/{fn}.jpg')