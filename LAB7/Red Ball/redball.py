import pygame

pygame.init()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
x = 25
y = 25
l = 1050
w = 650  
clock = pygame.time.Clock()
screen = pygame.display.set_mode((l, w))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), 25)
    pygame.draw.line(screen, (0, 0, 0), (x, y), (x, y))
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (l-1, 0), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, w-1), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, w-1), (l-1, w-1), 1)
    pygame.draw.line(screen, (0, 0, 0), (l-1, 0), (l-1, w-1), 1)

    pressed = pygame.key.get_pressed()
    if x + 25 <= l - 1 and y + 25 <= w - 1 and x > 25 and y > 25:
        if pressed[pygame.K_UP]:
            y -= 20
        if pressed[pygame.K_DOWN]:
            y += 20
        if pressed[pygame.K_LEFT]:
            x -= 20
        if pressed[pygame.K_RIGHT]:
            x += 20

    elif x + 25 >= l - 1 and y <= 25:
        if pressed[pygame.K_DOWN]:
            y += 20
        if pressed[pygame.K_LEFT]:
            x -= 20
    elif x + 25 >= l - 1 and y + 25 >= w - 1:
        if pressed[pygame.K_UP]:
            y -= 20
        if pressed[pygame.K_LEFT]:
            x -= 20
    elif x <= 25 and y+25 >= w - 1:
        if pressed[pygame.K_UP]:
            y -= 20
        if pressed[pygame.K_RIGHT]:
            x += 20
    elif x <= 25 and y <= 25:
        if pressed[pygame.K_RIGHT]:
            x += 20
        if pressed[pygame.K_DOWN]:
            y += 20

    elif x <= 25:
        if pressed[pygame.K_UP]:
            y -= 20
        if pressed[pygame.K_DOWN]:
            y += 20
        if pressed[pygame.K_RIGHT]:
            x += 20
    elif x + 25 > l - 1:
        if pressed[pygame.K_UP]:
            y -= 20
        if pressed[pygame.K_DOWN]:
            y += 20
        if pressed[pygame.K_LEFT]:
            x -= 20
    elif y <= 25:
        if pressed[pygame.K_DOWN]:
            y += 20
        if pressed[pygame.K_LEFT]:
            x -= 20
        if pressed[pygame.K_RIGHT]:
            x += 20
    elif y + 25 > w - 1:
        if pressed[pygame.K_UP]:
            y -= 20
        if pressed[pygame.K_LEFT]:
            x -= 20
        if pressed[pygame.K_RIGHT]:
            x += 20

    pygame.display.flip()

    clock.tick(20)
