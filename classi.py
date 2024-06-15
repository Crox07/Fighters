import pygame
import time

class Player:
    def __init__ (self, immagine, pos_iniziale):
        self.image=immagine
        self.rect=self.image.get_rect(topleft=pos_iniziale)
        self.life=100
        self.speed=5
        self.jump_power=25
        self.gravity=0.8
        self.is_jumping=False
        self.y_speed=0
        self.is_attacking = False
        self.attack_cooldown_L = 0.5
        self.attack_cooldown_M = 0.8
        self.attack_cooldown_H = 1.2        
        self.last_attack_time = 0
        self.last_attack_time_L = 0  
        self.last_attack_time_M = 0  
        self.last_attack_time_H = 0  
        self.tasto_precedente = pygame.key.get_pressed()


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
            self.rect.y += 5

        if keys[tasto['sinistra']]:
            self.rect.x -= self.speed
            #self.angolo = 180

        if keys[tasto['destra']]:
            self.rect.x += self.speed
            #self.angolo = 0
    
    def attack(self, keys, tasto):
        now=time.time()

        if keys[tasto['light']] and not self.tasto_precedente[tasto['light']] and (now - self.last_attack_time_L > self.attack_cooldown_L):
            self.is_attacking = True
            print("Light attack!")
            self.last_attack_time_L = now

        if keys[tasto['medium']] and not self.tasto_precedente[tasto['medium']] and (now - self.last_attack_time_M > self.attack_cooldown_M):
            self.is_attacking = True
            print("Medium attack!")
            self.last_attack_time_M = now

        if keys[tasto['heavy']] and not self.tasto_precedente[tasto['heavy']] and (now - self.last_attack_time_H > self.attack_cooldown_H):
            self.is_attacking = True
            print("Heavy attack!")
            self.last_attack_time_H = now
        
        self.tasto_precedente=keys
        self.is_attacking=False 
