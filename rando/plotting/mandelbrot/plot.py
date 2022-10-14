from turtle import width
from PIL import Image, ImageDraw
from mandelbrot import mandelbrot, MAX_ITER

WIDTH = 1000
HEIGHT = 1000

RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

palette = []

im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(0, WIDTH):
    for y in range(0, HEIGHT):

        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                IM_START + (y / HEIGHT) * (IM_END - IM_START))

        m = mandelbrot(c)

        color = 255 - int(m * 255 / MAX_ITER)

        draw.point([x, y], (color, color, color))

    im.save('./plotting/mandelbrot/output.png', 'PNG')