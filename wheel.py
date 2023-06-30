import math
from PIL import Image, ImageDraw
import random
import uuid

# Set the dimensions of the image
width = 3840
height = 3840

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

# Create a blank image with a black background
image = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(image)

# Generate random color palette with colors
def generate_glitch_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Function to draw the logo
def draw_logo(x, y, size, color):
    outer_circle_radius = size // 2
    inner_circle_radius = outer_circle_radius * 0.8
    line_length = outer_circle_radius * 0.55

    # Draw outer circle
    draw.ellipse([(x - outer_circle_radius, y - outer_circle_radius), (x + outer_circle_radius, y + outer_circle_radius)], fill=color)

    # Draw inner circle
    draw.ellipse([(x - inner_circle_radius, y - inner_circle_radius), (x + inner_circle_radius, y + inner_circle_radius)], fill="black")

    # Draw lines
    num_lines = 8
    angle_increment = 360 / num_lines

    for i in range(num_lines):
        angle = i * angle_increment
        x1 = x + int(line_length * (1 - 0.1) * math.cos(math.radians(angle)))
        y1 = y + int(line_length * (1 - 0.1) * math.sin(math.radians(angle)))
        x2 = x + int(line_length * (1 + 0.2) * math.cos(math.radians(angle)))
        y2 = y + int(line_length * (1 + 0.2) * math.sin(math.radians(angle)))
        draw.line([(x1, y1), (x2, y2)], fill=color, width=3)

# Generate logos randomly with glitch colors
num_logos = 100
logo_size_range = (300, 800)

for _ in range(num_logos):
    x = random.randint(0, width)
    y = random.randint(0, height)
    size = random.randint(logo_size_range[0], logo_size_range[1])
    color = generate_glitch_color()
    draw_logo(x, y, size, color)

# Save the image
image.save(f'{run_id}.png')
