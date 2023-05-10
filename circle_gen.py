import random
import uuid

from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

# Define a list of colors inspired by "Degen Coin Flip" colors
colors = [
    (238, 223, 167),   # Light beige
    (186, 213, 208),   # Light blue
    (94, 133, 160),   # Dark blue
    (24, 44, 97),  # Navy blue
    (28, 20, 13),  # Dark brown
]

image = Image.new('RGB', (3840, 2160), (0, 0, 0))
width, height = image.size

circle_diameter = 100

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
