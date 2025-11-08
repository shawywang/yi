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
        keyboard_layout = [
            list("qwertyuiop"),
            list("asdfghjkl"),
            list("zxcvbnm"),
        ]
        # 键盘底图
        keyboard_width = len(keyboard_layout[0]) * (key_width + padding) - padding
        keyboard_height = len(keyboard_layout) * (key_height + padding) - padding
        keyboard_image = Image.new("RGB", (keyboard_width, keyboard_height), "white")
        draw = ImageDraw.Draw(keyboard_image)
        # 加载单键文件
        letter_images = {letter: Image.open(f"C:\\Users\\wangxiao\\Downloads\\{letter}.webp") for letter in key_images}
        y_offset = 0
        x_add: Dict[int, int] = {  # 不同行起始位置偏移量
            0: 0,
            1: round(key_width * 0.4),
            2: round(key_width * 1.2)
        }
        for n, row in enumerate(keyboard_layout):
            x_offset = x_add[n]
            for l in row:
                keyboard_image.paste(letter_images[l], (x_offset, y_offset))
                x_offset += (key_width + padding)
            y_offset += (key_height + padding)

        # 宽1439，高484
        # 加备注文字
        n_x = round(key_width * 1.2) + 7 * (key_width + padding)
        n_y = 2 * (key_height + padding)
        n_font1 = ImageFont.truetype(font=r"C:\Users\wangxiao\AppData\Local\Microsoft\Windows\Fonts\华文楷体粗.ttf", size=25)
        n_font2 = ImageFont.truetype(font=r"C:\Users\wangxiao\AppData\Local\Microsoft\Windows\Fonts\IntelOneMono-Bold.ttf", size=20)

        draw.text(xy=(n_x, n_y), text="注：因无字根字\n红色“落”应去掉“各”、\n“释”应去掉右边；\n红色“一丨丶丿”为首笔", fill="black", font=n_font1)
        draw.text(xy=(n_x, n_y + 120), text="github.com/shawywang/yi", fill=(0, 0, 0), font=n_font2)
        draw.text(xy=(n_x, n_y + 140), text="or: gitee.com/shawywang/yi", fill=(95, 95, 95), font=n_font2)
        draw.text(xy=(n_x, n_y + 160), text="QQ: 790835977", fill=(0, 0, 0), font=n_font2)

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


def main():
    h = Handle()
    h.draw26()


if __name__ == "__main__":
    main()
