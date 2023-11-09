import pygame
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Esquiva Asteroides")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Cargar imágenes de la nave espacial y asteroides
spaceship = pygame.image.load('spaceship.png')
spaceship = pygame.transform.scale(spaceship, (50, 50))
asteroid = pygame.image.load('asteroid.png')
asteroid = pygame.transform.scale(asteroid, (50, 50))

# Nave espacial
spaceship_rect = spaceship.get_rect()
spaceship_x = width // 2
spaceship_y = height - 100
spaceship_speed = 5

# Asteroides
asteroids = []
asteroid_speed = 5

for _ in range(5):
    asteroid_rect = asteroid.get_rect()
    asteroid_x = random.randint(0, width - asteroid_rect.width)
    asteroid_y = random.randint(0, height // 2)
    asteroids.append((asteroid, asteroid_rect, asteroid_x, asteroid_y))

# Puntuación y vidas
score = 0
lives = 3
font = pygame.font.Font(None, 36)

# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship_x > 0:
        spaceship_x -= spaceship_speed
    if keys[pygame.K_RIGHT] and spaceship_x < width - spaceship_rect.width:
        spaceship_x += spaceship_speed

    spaceship_rect.topleft = (spaceship_x, spaceship_y)

    # Actualizar la posición de los asteroides
    for i, (_, asteroid_rect, asteroid_x, asteroid_y) in enumerate(asteroids):
        asteroid_y += asteroid_speed
        asteroid_rect.topleft = (asteroid_x, asteroid_y)

        # Colisión con la nave espacial
        if spaceship_rect.colliderect(asteroid_rect):
            asteroids[i] = (asteroid, asteroid_rect, random.randint(0, width - asteroid_rect.width), 0)
            lives -= 1

        # Si un asteroide llega al fondo, reinícialo en la parte superior
        if asteroid_y > height:
            asteroids[i] = (asteroid, asteroid_rect, random.randint(0, width - asteroid_rect.width), 0)
            score += 1

    # Dibujar todo en la pantalla
    screen.fill(WHITE)
    screen.blit(spaceship, spaceship_rect)
    for (asteroid, asteroid_rect, asteroid_x, asteroid_y) in asteroids:
        screen.blit(asteroid, asteroid_rect.topleft)

    # Mostrar puntuación y vidas en la pantalla
    score_text = font.render(f"Puntuación: {score}", True, RED)
    lives_text = font.render(f"Vidas: {lives}", True, RED)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

    pygame.display.update()

    # Verificar si el jugador ha perdido
    if lives <= 0:
        running = False

    clock.tick(60)

# Juego terminado
pygame.quit()
