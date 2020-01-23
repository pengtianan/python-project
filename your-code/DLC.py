#!/usr/bin/python

import pygame
pygame.init()

win_width = 1920
win_height = 1080

win = pygame.display.set_mode((win_width,win_height))
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
    if keys[pygame.K_LEFT] and x > vel+radius:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
        x -= vel

    if keys[pygame.K_RIGHT] and x < win_width - vel - radius:  # Making sure the top right corner of our character is less than the screen width - its width
        x += vel

    if keys[pygame.K_UP] and y > vel + radius:  # Same principles apply for the y coordinate
        y -= vel

    if keys[pygame.K_DOWN] and y < win_height - radius - vel:
        y += vel

    if keys[pygame.K_SPACE] and radius > 10:
        radius -= 10

    if keys[pygame.K_g] and radius < 100:
        radius += 10


    win.fill((0,0,0))  # Fills the screen with black
    pygame.draw.circle(win, (255,0,0), (x, y), radius)
    pygame.display.update()

pygame.quit()
