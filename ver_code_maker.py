#coding=utf-8
import random
import string
import sys
import math
import os

from PIL import Image,ImageDraw,ImageFont,ImageFilter

class MakeVerCOde(object):
    def __init__(
        self,
        code_number,
        image_size,
        bg_color,
        font_color,
        line_color,
        font_path,
        line_number,
        draw_line=True,
        font_size=25,
        output_file_name="test.png"
    ):
        self.code_number = code_number
        self.image_size = image_size
        self.bg_color = bg_color
        self.font_color = font_color
        self.line_color = line_color
        self.font_path = font_path
        self.line_number = line_number
        self.draw_line = draw_line
        self.font_size = font_size
        self.output_file_name = output_file_name

    def gene_text(self):
        source = string.ascii_letters + string.digits
        return ''.join([ random.choice(source) for _ in range(self.code_number) ])


    def gene_line(self, draw, width, height):
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill = self.line_color)


    def gene_code(self):
        width, height = self.image_size
        image = Image.new('RGBA', (width, height), self.bg_color)
        font = ImageFont.truetype(self.font_path, self.font_size) 
        draw = ImageDraw.Draw(image)
        text = self.gene_text() 
        font_width, font_height = font.getsize(text)
        draw.text(
            ((width - font_width) / self.code_number, (height - font_height) / self.code_number),
            text, font=font, fill=fontcolor
        )
        if self.draw_line:
            self.gene_line(draw, width, height)
        image = image.transform(
            (width+20,height+10),
            Image.AFFINE, (1,-0.3,0,-0.1,1,0),
            Image.BILINEAR
        )
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        image.save(self.output_file_name)
if __name__ == "__main__":
    font_path = None
    if os.name == "nt":
        font_path = 'C:/Windows/Fonts/Arial.ttf'
    else:
        font_path = '/Library/Fonts/Arial.ttf'
    number = 4
    image_size = (100, 30)
    bgcolor = (255, 255, 255)
    fontcolor = (0, 0, 255)
    linecolor = (255, 0, 0)
    draw_line = True
    line_number = (1, 5)
    mc = MakeVerCOde(
        number,
        image_size,
        bgcolor,
        fontcolor,
        linecolor,
        font_path,
        line_number
    )
    mc.gene_code()
