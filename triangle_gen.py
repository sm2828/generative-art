import random
import uuid

from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

colors = [
    (197, 145, 212),  # #c591d4
    (135, 108, 171),  # #876cab
    (102, 102, 147),  # #666693
    (142, 190, 201),  # #8ebec9
    (163, 228, 229),  # #a3e4e5
]

background_color = (240, 240, 240)  # Light gray

image_size = (3840, 2160)
line_thickness = 10

image = Image.new('RGB', image_size, background_color)
width, height = image.size

number_of_triangles = 10

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

    # Draw the triangle with an outline
    draw_image.polygon(
        [(x1, y1), (x2, y2), (x3, y3)],
        outline=(0, 0, 0),
        width=line_thickness,
        fill=color
    )

image = image.resize((image_size[0] // 2, image_size[1] // 2), resample=Image.LANCZOS)

image.save(f'{run_id}.png')
