import pygame
import datetime

pygame.init()
pygame.display.set_caption("Clock")

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(center=(x, y)).center)
    return rotated_image, new_rect


HEIGHT, WIDTH = 920, 700
screen = pygame.display.set_mode((HEIGHT, WIDTH))
mickey = pygame.image.load("mickeyClock.jpg")
hand = pygame.image.load("minute.png")
hand1 = pygame.image.load("second.png")

mickey = pygame.transform.scale(mickey, (HEIGHT, WIDTH))
hand = pygame.transform.scale(hand, (HEIGHT / 2, WIDTH / 2))
hand1 = pygame.transform.scale(hand1, (HEIGHT / 2, WIDTH / 2))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    second = datetime.datetime.now().second
    minute = datetime.datetime.now().minute
    x = (-6*minute) % 360
    y = ((-1)*second * 6) % 360

    rot_hand, x = rot_center(hand, x, HEIGHT / 2, WIDTH / 2)
    rot_hand1, y = rot_center(hand1, y, HEIGHT / 2, WIDTH / 2)
    screen.blit(mickey, (0, 0))
    screen.blit(rot_hand, x)
    screen.blit(rot_hand1, y)

    pygame.display.update()
clock.tick(60)
pygame.quit()
