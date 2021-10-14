import argparse
import requests
from PIL import Image

r = requests.get(input("輸入要轉換的圖片:"))
with open("./demo.png", "wb") as f:
    f.write(r.content)
parser = argparse.ArgumentParser()
args = parser.parse_args()

img = "./demo.png"
width = 45
height = 38
ascii_char = list("⠀⠄⠆⠖⠶⡶⣩⣪⣫⣾⣿")


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


if __name__ == "__main__":
    im = Image.open(img).resize((width, height), Image.NEAREST)
    txt = ""
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j, i)))
        txt += "\n"
    print(txt)
    f = open("./黑白.txt", "w", encoding="utf-8")
    f.write(txt)