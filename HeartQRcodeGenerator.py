import pyqrcode
from PIL import Image, ImageDraw, ImageFont

name = '"웜보국"'
postfix = '을'

# Parsing Excel

# Generate QR Code
url = 'https://wedding-for-junyoung-bomin-20230715.github.io/?name=' + name.encode('utf-8').decode('unicode_escape') + '&postfix=' + postfix.encode('utf-8').decode('unicode_escape')
qr = pyqrcode.create(url)
qr.png('./tmp/tmp.png', scale=6, module_color=[0xff, 0x37, 0x37, 0xff], background=[0xff, 0xff, 0xff])

# get an image
with Image.open("./tmp/tmp.png").convert("RGBA") as img:
    # get a drawing context
    draw = ImageDraw.Draw(img)
    
    # font
    try:
        font = ImageFont.truetype('NanumGothicBold.ttf', 20)
    except:
        font = ImageFont.load_default()
    
    # width, height
    width, height = img.size
    w, h = font.getsize(name)
    margin = 2
    x = 25
    y = (height-h) - margin

    # draw text, full opacity
    draw.text((x, y), name, font=font, fill=(0xff, 0x37, 0x37, 0xff))
    
    # save qr code
    output = "./output/" + name[1:-1] + ".png"
    img.save(output)