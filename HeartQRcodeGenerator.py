import pandas as pd
import pyqrcode
from PIL import Image, ImageDraw, ImageFont

file = './input/invitation.xlsx'

def ParsingExcel(filename):
    df = pd.read_excel(filename, sheet_name=0, engine='openpyxl')
    df_name = df['name']
    df_postfix = df['postfix']
    return df_name, df_postfix

def GenerateQR(name, postfix):
    # Generate QR Code
    url = 'https://wedding-for-junyoung-bomin-20230715.github.io/?name=' + name.encode('utf-8').decode('unicode_escape') + '&postfix=' + postfix.encode('utf-8').decode('unicode_escape')
    qr = pyqrcode.create(url)
    qr.png('./tmp/tmp.png', scale=6, module_color=[0x4c, 0x49, 0x48, 0xff], background=[0xff, 0xff, 0xff, 0x00])  # R76/G73/B72
    
    # get an image
    with Image.open('./tmp/tmp.png').convert('RGBA') as img:
        # get a drawing context
        draw = ImageDraw.Draw(img)
        
        # font
        try:
            font = ImageFont.truetype('NanumGothicBold.ttf', 22)
        except:
            font = ImageFont.load_default()
        
        # width, height
        width, height = img.size
        w, h = font.getsize(name)
        margin = 2
        x = 25
        y = (height-h) - margin

        # draw text, full opacity
        draw.text((x, y), name, font=font, fill=(0x4c, 0x49, 0x48, 0xff))
        
        # save qr code
        output = "./output/" + name + ".png"
        img.save(output)

if __name__ == '__main__':
    df_name, df_postfix = ParsingExcel(file)
    
    for name, postfix in zip(df_name, df_postfix):
        GenerateQR(name, postfix)