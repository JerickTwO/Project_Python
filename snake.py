import pygame
import random

# Initialize Pygame
pygame.init()

# Window setup
width, height = 640, 480
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Snake block size and initial position
snake_block = 10
snake_speed = 15

x1 = width // 2
y1 = height // 2

x1_change = 0
y1_change = 0

# Snake body list
snake_list = []
length_of_snake = 1

# Function to draw the snake on the window
def draw_snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(win, black, [segment[0], segment[1], snake_block, snake_block])

game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    # Prevent the snake from going out of the window
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    win.fill(white)

    snake_head = [x1, y1]
    snake_list.append(snake_head)

    if len(snake_list) > length_of_snake:
        del snake_list[0]

    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    draw_snake(snake_block, snake_list)
    pygame.display.update()

    # Snake speed
    pygame.time.delay(snake_speed)
import pygame


# Direction 
direction = 'RIGHT'  

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                x1_change = -snake_block
                y1_change = 0
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                x1_change = snake_block
                y1_change = 0
                direction = 'RIGHT'
            elif event.key == pygame.K_UP and direction != 'DOWN':
                y1_change = -snake_block
                x1_change = 0
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                y1_change = snake_block
                x1_change = 0
                direction = 'DOWN'
# Quit Pygame
pygame.quit()
