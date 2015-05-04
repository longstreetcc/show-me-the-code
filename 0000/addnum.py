from PIL import Image,ImageDraw,ImageFont
import sys

def addnum(img):
    w,h = img.size
    font = ImageFont.truetype('Ubuntu-B.ttf',w//5)
    draw = ImageDraw.Draw(img)
    draw.text((w-w//4,0),'4',font=font,fill="#C80003")
    img.save('result.jpg',"jpeg")

if __name__ == '__main__':
    img = Image.open(sys.argv[1])
    addnum(img)

#python addnum.py head.py
