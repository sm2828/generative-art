import pygame
import random
import uuid

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH = 1000
HEIGHT = 800

# Colors
LIGHT_BEIGE = (238, 223, 167)
LIGHT_BLUE = (186, 213, 208)
DARK_BLUE = (94, 133, 160)
NAVY_BLUE = (24, 44, 97)
DARK_BROWN = (28, 20, 13)
GREEN = (85, 171, 122)
RED = (220, 105, 110)

# Color options
colors = [LIGHT_BEIGE, LIGHT_BLUE, DARK_BLUE, NAVY_BLUE, DARK_BROWN, GREEN, RED]

# Circle parameters
circle_radius = 80

# Number of circles
number_of_circles = 8

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("circle_???")

# Clock object to control frame rate
clock = pygame.time.Clock()

# Ball class
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity = [0, 0]  # Initial velocity
        self.collided = False  # Flag to indicate collision

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def apply_gravity(self):
        # Apply downward force (gravity)
        self.velocity[1] += .69

    def apply_friction(self):
        # Apply friction to reduce horizontal velocity
        self.velocity[0] *= 0.99

    def check_collision(self, cursor_pos):
        # Check for collision with the cursor
        cursor_x, cursor_y = cursor_pos
        distance = ((self.x - cursor_x) ** 2 + (self.y - cursor_y) ** 2) ** 0.5
        return distance < self.radius

    def draw(self, screen):
        if self.collided:
            # Draw a larger circle with a brighter color when collided
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius + 10)
        else:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


# List to store the balls
balls = []

# Create balls
for _ in range(number_of_circles):
    circle_x = random.randint(circle_radius, WIDTH - circle_radius)
    circle_y = random.randint(circle_radius, HEIGHT - circle_radius)

    # Choose a random color from the list
    color = random.choice(colors)

    ball = Ball(circle_x, circle_y, circle_radius, color)
    balls.append(ball)


# Function to handle events
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEMOTION:
            # Check for collision with the cursor
            for ball in balls:
                if ball.check_collision(pygame.mouse.get_pos()):
                    # Apply a stronger reaction to the ball
                    ball.velocity[0] += random.uniform(-8, 8)
                    ball.velocity[1] += random.uniform(-8, 8)
                    ball.collided = True
                else:
                    ball.collided = False


# Function to updatethe ball positions
def update_positions():
    for ball in balls:
        ball.update()
        ball.apply_gravity()
        ball.apply_friction()
        ball.check_collision(pygame.mouse.get_pos())

        # Keep the balls within the window boundaries
        if ball.x - ball.radius < 0 or ball.x + ball.radius > WIDTH:
            ball.velocity[0] *= -1
        if ball.y - ball.radius < 0 or ball.y + ball.radius > HEIGHT:
            ball.velocity[1] *= -0.9  # Adjust the coefficient of restitution here


# Function to draw on the screen
def draw_screen():
    screen.fill((245, 245, 220))
    for ball in balls:
        ball.draw(screen)
    pygame.display.flip()


# Game loop
running = True
while running:
    handle_events()
    update_positions()
    draw_screen()
    clock.tick(60)
