import pygame

class Player:
    def __init__ (self, immagine, pos_iniziale):
        self.image=immagine
        self.rect=self.image.get_rect(topleft=pos_iniziale)
        self.life=100
        self.speed=5
        self.jump_power=15
        self.gravity=1
        self.is_jumping=False
        self.y_speed=0
    
    def controllo_bordi(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1200:
            self.rect.right = 1200


    def movimento(self, keys, tasto):
        self.controllo_bordi()

        if keys[tasto['su']] and not self.is_jumping:
            self.is_jumping=True
            self.y_speed= - self.jump_power

        if self.is_jumping:
            self.rect.y += self.y_speed
            self.y_speed += self.gravity

        if self.rect.y >= 600:
            self.rect.y = 600
            self.is_jumping = False
            self.y_speed = 0    

        if keys[tasto['giù']]:
            self.rect.y += 2



        if keys[tasto['sinistra']]:
            self.rect.x -= self.speed
            #self.angolo = 180

        if keys[tasto['destra']]:
            self.rect.x += self.speed
            #self.angolo = 0
