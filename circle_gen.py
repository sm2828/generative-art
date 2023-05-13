import random
import uuid

from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

LIGHT_BEIGE = (238, 223, 167)
LIGHT_BLUE = (186, 213, 208)
DARK_BLUE = (94, 133, 160)
NAVY_BLUE = (24, 44, 97)
DARK_BROWN = (28, 20, 13)
GREEN = (85, 171, 122)
RED = (220, 105, 110)

# Color options
colors = [LIGHT_BEIGE, LIGHT_BLUE, DARK_BLUE, NAVY_BLUE, DARK_BROWN, GREEN, RED]

phone_format = (1179, 2556)
desktop_format = (3840, 2160)
image = Image.new('RGB', desktop_format, (245, 245, 220))
width, height = image.size

circle_diameter = 160

number_of_circles = random.randint(1, 1000)

draw_image = ImageDraw.Draw(image)
for i in range(number_of_circles):
    circle_x = random.randint(0, width)
    circle_y = random.randint(0, height)

    # Choose a random color from the list
    color = random.choice(colors)

    circle_shape = [
        (circle_x - circle_diameter / 2, circle_y - circle_diameter / 2),
        (circle_x + circle_diameter / 2, circle_y + circle_diameter / 2)
    ]
    draw_image.ellipse(
        circle_shape,
        fill=color
    )

image.save(f'{run_id}.png')
