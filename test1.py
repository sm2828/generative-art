import random
import uuid

from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

# Define a list of colors to choose from
colors = [
    (230, 220, 218),   # 
    (185, 85, 110),   # light blue
    (22, 22, 20),  # Red
    (72, 68, 132),  # Red

]

image = Image.new('RGB', (1500, 500), (190, 201, 185))
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
