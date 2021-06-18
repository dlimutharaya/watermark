from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor


def watermark_withtext(input_image, text, position):

    text_image = Image.new('RGBA', input_image.size, color=(255, 0, 0, 0))
    font = ImageFont.truetype('fonts/OpenSans-Regular.ttf', 400)
    wm_color = (211, 211, 211, 128)

    drawing = ImageDraw.Draw(text_image)

    drawing.text(position, text, wm_color, font)
    final_image = Image.alpha_composite(
        input_image.convert('RGBA'), text_image)
    final_image.show()
    final_image.convert('RGB').save('images/watermark_image.jpg')


def text_to_image(input_text):

    font = ImageFont.truetype('fonts/OpenSans-Regular.ttf', 200)

    text_image = Image.new('RGBA', font.getsize(
        input_text), color=(128, 128, 128, 0))
    wm_text_color = (211, 211, 211, 128)

    drawing = ImageDraw.Draw(text_image)
    drawing.text((0, 0), input_text, wm_text_color, font)

    return text_image


def wm_image(input_image, wm_logo, position):

    width, height = input_image.size
    wm_image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    wm_image.paste(input_image, (0, 0))
    wm_image.paste(wm_logo, position, mask=wm_logo)
    wm_image.show()
    wm_image.save('images/final_image.png')


def main():

    print("I am in main: ")
    input_image = Image.open('images/rose.jpg')
    text = 'Divya'
    position = (0, 0)

    # output_image = Image.new(input_image.mode,input_image.size)

    # watermark_withtext(input_image, text, position)
    wm_logo = text_to_image(text)
    wm_logo.save('images/wm_logo1.png')

    # final_image = wm_image(input_image, wm_logo, (0, 0))


if __name__ == '__main__':
    main()
