import random
import uuid

from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

# Define a list of colors inspired by "The Starry Night" painting by Vincent van Gogh
colors = [
    (80, 150, 36),   # dark green
    (80, 150, 36),   # dark green
    (80, 150, 36),   # dark green
    (80, 150, 36),   # dark green
    (80, 150, 36),   # dark green
    (32, 103, 44),   # deep green
    (32, 103, 44),   # deep green
    (32, 103, 44),   # deep green
    (32, 103, 44),   # deep green
    (31, 84, 144),  # dark blue
    (28, 30, 133),  # deep blue
    (28, 30, 133),  # deep blue
    (28, 30, 133),  # deep blue
    (238, 0, 0),  # red
]

image = Image.new('RGB', (3840, 2160), (0, 0, 0))
width, height = image.size

rectangle_width = 5
rectangle_height = 100

number_of_squares = random.randint(1, 1000)

draw_image = ImageDraw.Draw(image)
for i in range(number_of_squares):
    rectangle_x = random.randint(0, width)
    rectangle_y = random.randint(0, height)

    # Choose a random color from the list
    color = random.choice(colors)

    rectangle_shape = [
        (rectangle_x, rectangle_y),
        (rectangle_x + rectangle_width, rectangle_y + rectangle_height)]
    draw_image.rectangle(
        rectangle_shape,
        fill=color
    )

image.save(f'{run_id}.png')
