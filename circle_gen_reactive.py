import pygame
import random
import uuid

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH = 1400
HEIGHT = 800

# Colors
LIGHT_BEIGE = (238, 223, 167)
LIGHT_BLUE = (186, 213, 208)
DARK_BLUE = (94, 133, 160)
NAVY_BLUE = (24, 44, 97)
DARK_BROWN = (28, 20, 13)

# Color options
colors = [LIGHT_BEIGE, LIGHT_BLUE, DARK_BLUE, NAVY_BLUE, DARK_BROWN]

# Circle parameters
circle_radius = 25

# Number of circles
number_of_circles = 30

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Generative Art")

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

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def apply_gravity(self):
        # Apply downward force (gravity)
        self.velocity[1] += 1

    def apply_friction(self):
        # Apply friction to reduce horizontal velocity
        self.velocity[0] *= 0.99

    def check_collision(self, cursor_pos):
        # Check for collision with the cursor
        cursor_x, cursor_y = cursor_pos
        distance = ((self.x - cursor_x) ** 2 + (self.y - cursor_y) ** 2) ** 0.5
        return distance < self.radius

    def draw(self, screen):
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

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            # Check for collision with the cursor
            for ball in balls:
                if ball.check_collision(pygame.mouse.get_pos()):
                    # Apply a reaction to the ball
                    ball.velocity[0] += random.uniform(-3, 3)
                    ball.velocity[1] += random.uniform(-3, 3)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Update ball positions and apply gravity
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

        # Draw the ball
        ball.draw(screen)

    # Refresh the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
