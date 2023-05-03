import pygame

pygame.init()
pygame.mixer_music.load('ex21.mp3')
pygame.mixer_music.play()
pygame.event.wait()
