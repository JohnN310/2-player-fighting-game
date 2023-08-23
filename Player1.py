import pygame, sys

class Player1(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.attack_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load('player1\download.png'))
        self.sprites.append(pygame.image.load('player1\download (1).png'))
        self.sprites.append(pygame.image.load('player1\download (2).png'))
        self.sprites.append(pygame.image.load('player1\download (3).png'))
        self.sprites.append(pygame.image.load('player1\download (4).png'))
        self.sprites.append(pygame.image.load('player1\download (5).png'))
        self.sprites.append(pygame.image.load('player1\download (6).png'))
        self.sprites.append(pygame.image.load('player1\download (7).png'))
        self.sprites.append(pygame.image.load('player1\download (8).png'))
        self.sprites.append(pygame.image.load('player1\download (9).png'))
        self.sprites.append(pygame.image.load('player1\download (10).png'))
        self.sprites.append(pygame.image.load('player1\download (11).png'))
        self.sprites.append(pygame.image.load('player1\download (12).png'))
        self.sprites.append(pygame.image.load('player1\download (13).png'))
        self.sprites.append(pygame.image.load('player1\download (14).png'))
        self.sprites.append(pygame.image.load('player1\download (15).png'))
        self.sprites.append(pygame.image.load('player1\download (16).png'))
        self.sprites.append(pygame.image.load('player1\download (17).png'))
        self.sprites.append(pygame.image.load('player1\download (18).png'))
        self.sprites.append(pygame.image.load('player1\download (19).png'))
        self.sprites.append(pygame.image.load('player1\download (20).png'))
        self.sprites.append(pygame.image.load('player1\download (21).png'))
        self.sprites.append(pygame.image.load('player1\download (22).png'))
        self.sprites.append(pygame.image.load('player1\download (23).png'))
        self.sprites.append(pygame.image.load('player1\download (24).png'))
        self.sprites.append(pygame.image.load('player1\download (25).png'))
        self.sprites.append(pygame.image.load('player1\download (26).png'))
        self.sprites.append(pygame.image.load('player1\download (27).png'))
        self.sprites.append(pygame.image.load('player1\download (28).png'))
        self.sprites.append(pygame.image.load('player1\download (29).png'))
        self.sprites.append(pygame.image.load('player1\download (30).png'))
        self.sprites.append(pygame.image.load('player1\download (29).png'))
        self.sprites.append(pygame.image.load('player1\download (28).png'))
        self.sprites.append(pygame.image.load('player1\download (27).png'))
        self.sprites.append(pygame.image.load('player1\download (26).png'))
        self.sprites.append(pygame.image.load('player1\download (25).png'))
        self.sprites.append(pygame.image.load('player1\download (24).png'))
        self.sprites.append(pygame.image.load('player1\download (23).png'))
        self.sprites.append(pygame.image.load('player1\download (22).png'))
        self.sprites.append(pygame.image.load('player1\download (21).png'))
        self.sprites.append(pygame.image.load('player1\download (20).png'))
        self.sprites.append(pygame.image.load('player1\download (19).png'))
        self.sprites.append(pygame.image.load('player1\download (18).png'))
        self.sprites.append(pygame.image.load('player1\download (17).png'))
        self.sprites.append(pygame.image.load('player1\download (16).png'))
        self.sprites.append(pygame.image.load('player1\download (15).png'))
        self.sprites.append(pygame.image.load('player1\download (14).png'))
        self.sprites.append(pygame.image.load('player1\download (13).png'))
        self.sprites.append(pygame.image.load('player1\download (12).png'))
        self.sprites.append(pygame.image.load('player1\download (11).png'))
        self.sprites.append(pygame.image.load('player1\download (10).png'))
        self.sprites.append(pygame.image.load('player1\download (9).png'))
        self.sprites.append(pygame.image.load('player1\download (8).png'))
        self.sprites.append(pygame.image.load('player1\download (7).png'))
        self.sprites.append(pygame.image.load('player1\download (6).png'))
        self.sprites.append(pygame.image.load('player1\download (5).png'))
        self.sprites.append(pygame.image.load('player1\download (4).png'))
        self.sprites.append(pygame.image.load('player1\download (3).png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def attack(self):
        self.attack_animation = True

    def update(self, speed):
        if self.attack_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.attack_animation = False
        self.image = self.sprites[int(self.current_sprite)]