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

# Generate random color palette with nighttime colors
colors = [
    (255, 40, 40, 200),    # Red
    (255, 150, 40, 200),   # Orange
    (255, 255, 40, 200),   # Yellow
    (0, 255, 0, 200),      # Lime Green
    (40, 200, 255, 200),   # Light Blue
    (150, 40, 255, 200),   # Purple
    (255, 40, 150, 200),   # Pink
    (255, 255, 255, 200),  # White
]


# Draw random rectangles with different colors
for _ in range(1000):
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = x1 + random.randint(10, 500)
    y2 = y1 + random.randint(10, 500)
    color = random.choice(colors)
    draw.rectangle([(x1, y1), (x2, y2)], fill=color)

# Save the image
image.save(f'{run_id}.png')
