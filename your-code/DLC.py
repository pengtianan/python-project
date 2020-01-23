#!/usr/bin/python

import pygame
pygame.init()

win = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("First Game")

x = 50
y = 50
radius = 40
vel = 20

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

    if keys[pygame.K_SPACE] and radius == 40:
        radius -= 10


    win.fill((0,0,0))  # Fills the screen with black
    pygame.draw.circle(win, (255,0,0), (x, y), radius)
    pygame.display.update()

pygame.quit()
