import random
import uuid

from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

colors = [
    (163, 255, 160),   # light green
    (129, 199, 251),   # light blue
    (255, 96, 75),  # Red
    (255, 255, 79),  # Red
]

image = Image.new('RGB', (3840, 2160), (0, 0, 0))
width, height = image.size

number_of_triangles = 2

draw_image = ImageDraw.Draw(image)

for i in range(number_of_triangles):
    # Define the coordinates of the triangle vertices
    x1 = random.randint(0, width)
    x2 = random.randint(0, width)
    x3 = random.randint(0, width)

    y1 = random.randint(0, height)
    y2 = random.randint(0, height)
    y3 = random.randint(0, height)

    # Choose a random color from the list
    color = random.choice(colors)

    # Draw the triangle
    draw_image.polygon(
        [(x1, y1), (x2, y2), (x3, y3)],
        fill=color
    )

image.save(f'{run_id}.png')
