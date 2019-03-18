from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 



class ImageText:
    def __init__(self, imagedata):
        self.image = imagedata
    
    def AddText(text):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("sans-serif.ttf", 16)
        draw.text((0, 0),text,(255,255,255),font=font)
        return self.image
