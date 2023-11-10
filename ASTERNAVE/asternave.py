import pygame
import random

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
width, height = 640, 480
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Tamaño del bloque de la serpiente y posición inicial
snake_block = 10
snake_speed = 15

x1 = width // 2
y1 = height // 2

x1_change = 0
y1_change = 0

# Lista del cuerpo de la serpiente
snake_list = []
length_of_snake = 1

# Función para dibujar la serpiente en la ventana
def draw_snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(win, black, [segment[0], segment[1], snake_block, snake_block])

game_over = False

# Bucle principal del juego
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

    # Evita que la serpiente salga de la ventana
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

    # Velocidad de la serpiente
    pygame.time.delay(snake_speed)

# Cierra Pygame
pygame.quit()
