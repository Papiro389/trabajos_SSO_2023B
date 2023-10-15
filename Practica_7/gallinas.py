import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
window_width = 700
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Gallinas en Movimiento')

# Cargar imágenes para los elementos
element1_image = pygame.image.load('img1.png')
element2_image = pygame.image.load('img2.png')

# Ajustar el tamaño de las imágenes al tamaño deseado
element_size = 225
element1_image = pygame.transform.scale(element1_image, (element_size, element_size))
element2_image = pygame.transform.scale(element2_image, (element_size, element_size))

# Cargar el fondo y ajustar su tamaño
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (window_width, window_height))

# Posiciones iniciales de los elementos (centrados)
element1_x = (window_width - element_size) // 2
element1_y = (window_height - element_size) // 2
element2_x = (window_width - element_size) // 2
element2_y = (window_height - element_size) // 2

# Velocidad de movimiento de los elementos
element1_speed_x = 2  # Mover de izquierda a derecha
element2_speed_y = 2  # Mover de arriba hacia abajo

clock = pygame.time.Clock()

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar la posición del primer elemento (mover de izquierda a derecha)
    element1_x += element1_speed_x

    # Cambiar la dirección del primer elemento si alcanza los bordes
    if element1_x > window_width - element_size or element1_x < 0:
        element1_speed_x *= -1

    # Actualizar la posición del segundo elemento (mover de arriba hacia abajo)
    element2_y += element2_speed_y

    # Cambiar la dirección del segundo elemento si alcanza los bordes
    if element2_y > window_height - element_size or element2_y < 0:
        element2_speed_y *= -1

    # Limpiar la ventana
    window.blit(background, (0, 0))

    # Dibujar el primer elemento
    window.blit(element1_image, (element1_x, element1_y))

    # Dibujar el segundo elemento
    window.blit(element2_image, (element2_x, element2_y))

    # Actualizar la pantalla
    pygame.display.flip()

    clock.tick(60)  # Controlar la velocidad de actualización

# Salir de Pygame
pygame.quit()
sys.exit()
