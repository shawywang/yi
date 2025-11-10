from typing import Dict

from PIL import Image, ImageDraw, ImageFont

key_images: str = "qwertyuiopasdfghjklzxcvbnm"


class Handle:
    def __init__(self):
        pass

    def draw26(self):
        key_width = 167
        key_height = 232
        padding = 10  # 键之间的距离：宽和高
        lr: int = 32  # 画布左、右空白像素
        ud: int = 155  # 画布上、下空白像素
        keyboard_layout = [
            list("qwertyuiop"),
            list("asdfghjkl"),
            list("zxcvbnm"),
        ]
        # 键盘底图，宽1824，高1026
        keyboard_width = len(keyboard_layout[0]) * (key_width + padding) - padding + lr * 2  # 左右各加32个像素的空白
        keyboard_height = len(keyboard_layout) * (key_height + padding) - padding + ud * 2  # 上下各加155个像素，以适配宽/高=1920/1080
        keyboard_image = Image.new("RGB", (keyboard_width, keyboard_height), (255, 255, 255))
        draw = ImageDraw.Draw(keyboard_image)
        # 加载单键文件
        letter_images = {letter: Image.open(f"C:\\Users\\wangxiao\\Downloads\\{letter}.webp") for letter in key_images}
        y_offset = ud  # 上方有155像素的空白
        x_add: Dict[int, int] = {  # 不同行起始位置偏移量
            0: 0 + lr,
            1: round(key_width * 0.4) + lr,
            2: round(key_width * 1.2) + lr,
        }
        for n, row in enumerate(keyboard_layout):
            x_offset = x_add[n]
            for l in row:
                keyboard_image.paste(letter_images[l], (x_offset, y_offset))
                x_offset += (key_width + padding)
            y_offset += (key_height + padding)

        # 加备注文字
        n_x = round(key_width * 1.2) + lr
        n_y = 3 * (key_height + padding) + ud
        n_font1 = ImageFont.truetype(font=r"C:\Users\wangxiao\AppData\Local\Microsoft\Windows\Fonts\华文楷体粗.ttf", size=25)
        n_font2 = ImageFont.truetype(font=r"C:\Users\wangxiao\AppData\Local\Microsoft\Windows\Fonts\IntelOneMono-Bold.ttf", size=20)

        draw.text(xy=(lr, ud - 35), text="逸码v20：连续二码纯形顶功输入方案", fill=(0, 0, 0), font=n_font1)
        draw.text(xy=(lr + 438, ud - 35), text="https://yb6b.github.io/yima", fill=(0, 0, 0), font=n_font2)
        draw.text(xy=(n_x, n_y), text="注：因无字根字，红色“落”应去掉“各”、“释”应去掉右边；红色“一丨丶丿”为首笔", fill=(0, 0, 0), font=n_font1)
        draw.text(xy=(n_x, n_y + 30), text="https://github.com/shawywang/yi.git or: https://gitee.com/shawywang/yi.git QQ: 790835977", fill=(0, 0, 0), font=n_font2)

        # 保存
        palette_img = Image.new("P", (1, 1))  # 调色板
        palette_img.putpalette(
            [
                0, 0, 0,  # 黑色
                255, 0, 0,  # 红色
                255, 255, 255,  # 白色
                255, 204, 153,  # 浅橙色
                95, 95, 95,  # 灰色
                221, 221, 221,  # 浅灰色
            ]
        )
        fixed_image = keyboard_image.quantize(palette=palette_img, dither=Image.Dither.NONE)
        fixed_image.save(
            fp="C:\\Users\\wangxiao\\Downloads\\字根图（PIL生成）.webp",
            optimize=True,
            compress_level=5,
            dpi=(72, 72),
            format="WEBP",
            quality=80,
        )
        fixed_image.save(
            fp="C:\\Users\\wangxiao\\Downloads\\字根图（PIL生成）.png",
            optimize=True,
            compress_level=5,
            dpi=(72, 72),
            format="PNG",
            quality=80,
        )


def main():
    h = Handle()
    h.draw26()


if __name__ == "__main__":
    main()
