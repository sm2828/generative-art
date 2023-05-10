import random
import uuid

from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

colors = [
    (85, 171, 122),   # green
    (220, 105, 110),   #  red
]

image = Image.new('RGB', (3840, 2160), (0, 0, 0))
width, height = image.size

number_of_triangles = 2

draw_image = ImageDraw.Draw(image)

for i in range(number_of_triangles):
    # Define the coordinates of the triangle vertices
    x1 = random.randint(0, width/2)
    x2 = random.randint(0, width/2)
    x3 = random.randint(0, width/2)

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
