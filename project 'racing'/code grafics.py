##import modules
import time
import os
import pygame

pygame.init()

##interface

n_1st_p = input('Введите номер 1-ой машины(0-10): ')
n_2nd_p = input('Введите номер 2-ой машины(0-10): ')
p1_x=20
p1_y=720/2
p2_x=60
p2_y=720/2
p2_rect=pygame.Rect((1,1),(2,2))
p1_rect=pygame.Rect((4,3),(8,8))
correct_ans = True
m_sp2 = 5
m_sp1 = 5

##colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

##render and screen

width=1080
height=720
FPS=90
running = True
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Need for СПИД")
clock = pygame.time.Clock()
offset1 = (int(p1_x-width / 2), int(p1_y-height / 2))
offset2 = (int(p2_x-width / 2), int(p2_y-height / 2))


#classes

class Second_Player(pygame.sprite.Sprite):
    def __init__(self):
        global correct_ans, n_2nd_p, p2_rect
        pygame.sprite.Sprite.__init__(self)
        while correct_ans:
            try:
                self.car = pygame.image.load(os.path.join(img_folder, 'g_car'+n_2nd_p+'.png')).convert()
                if n_2nd_p == 'lessgo':
                    lessgo.play()
                    
                correct_ans = False
            except FileNotFoundError:
                n_2nd_p = input('Попробуйте другой номер для 2-ой машины ')
        correct_ans = True
        self.car = pygame.transform.scale(self.car, (self.car.get_width()//5, self.car.get_height()//5))
        self.image = self.car
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (60 , height / 2)
        p2_x=60
        p2_y=height / 2
        self.speedx = 0
        self.speedy = 0
        self.car_up = self.car
        self.car_down = pygame.transform.flip(self.car, 1, 1)
        self.car_left = pygame.transform.rotate(self.car, 90)
        self.car_right = pygame.transform.rotate(self.car, -90)
        self.car_up_right = pygame.transform.rotate(self.car, -45)
        self.car_down_right = pygame.transform.rotate(self.car, -135)
        self.car_up_left = pygame.transform.rotate(self.car, 45)
        self.car_down_left = pygame.transform.rotate(self.car, 135)
        p2_rect=self.rect

    def update(self):
        global p2_y, p2_x, p1_rect, p2_rect
        keystate = pygame.key.get_pressed()
        self.rect.x=p2_x
        self.rect.y=p2_y
        p2_rect=self.rect
        if keystate[pygame.K_LEFT]:
            if keystate[pygame.K_UP] and keystate[pygame.K_LEFT]:
                self.car = self.car_up_left
                self.speedy -= 0.6
                self.speedx -= 0.6
            elif keystate[pygame.K_LEFT] and keystate[pygame.K_DOWN]:
                self.car = self.car_down_left
                self.speedx -= 0.6
                self.speedy += 0.6
            elif keystate[pygame.K_LEFT]:
                self.car = self.car_left
                self.speedx-=0.6
        elif keystate[pygame.K_RIGHT]:
            if keystate[pygame.K_RIGHT] and keystate[pygame.K_DOWN]:
                self.car = self.car_down_right
                self.speedx += 0.6
                self.speedy += 0.6
            elif keystate[pygame.K_RIGHT] and keystate[pygame.K_UP]:
                self.speedy -= 0.6
                self.car = self.car_up_right
                self.speedx += 0.6
            elif keystate[pygame.K_RIGHT]:
                self.car = self.car_right
                self.speedx += 0.6
        elif keystate[pygame.K_UP]:
            self.car = self.car_up
            self.speedy -= 0.6
        elif keystate[pygame.K_DOWN]:
            self.car = self.car_down
            self.speedy += 0.6
        

        if self.rect.right > width:
            self.speedx*=(-0.75)
            p2_x-=5
        elif self.rect.left < 0:
            self.speedx*=(-0.75)
            p2_x+=5
        elif self.rect.bottom > height:
            self.speedy*=(-0.75)
            p2_y-=5
        elif self.rect.top < 0:
            self.speedy*=(-0.75)
            p2_y+=5
        if p2_rect.colliderect(p1_rect):
            if self.speedx > 0:
                self.speedx -= 3
                self.speedx*=(-0.75)
            elif self.speedx < 0:
                self.speedx*=(-0.75)
            if self.speedy > 0:
                self.speedy*=(-0.75)
            elif self.speedy < 0:
                self.speedy*=(-0.75)
        if self.speedx>m_sp2:
            self.speedx=m_sp2
        if self.speedx<-1*m_sp2:
            self.speedx=-1*m_sp2
        if self.speedy>m_sp2:
            self.speedy=m_sp2
        if self.speedy<-1*m_sp2:
            self.speedy=-1*m_sp2
        if self.speedx > 0:
            self.speedx-=0.1
        if self.speedy > 0:
            self.speedy-=0.1
        if self.speedx < 0:
            self.speedx+=0.2
        if self.speedy < 0:
            self.speedy+=0.1
        if self.speedx<0.3 and self.speedx>(-0.3):
            self.speedx=0
        if self.speedy<0.3 and self.speedy>(-0.3):
            self.speedy=0
        p2_y+=self.speedy
        p2_x+=self.speedx
        self.image = self.car


class Player(pygame.sprite.Sprite):
    def __init__(self):
        global correct_ans, n_1st_p, p1_rect, lessgo
        pygame.sprite.Sprite.__init__(self)
        while correct_ans:
            try:
                self.car = pygame.image.load(os.path.join(img_folder, 'g_car'+n_1st_p+'.png')).convert()
                if n_1st_p == 'lessgo':
                    lessgo.play()
                
                correct_ans = False
            except FileNotFoundError:
                n_1st_p = input('Попробуйте другой номер для 1-ой машины ')
        correct_ans = True
        car1_img = self.car
        self.car = pygame.transform.scale(self.car, (self.car.get_width()//5, self.car.get_height()//5))
        self.image = self.car
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (20, height / 2)
        self.speedx = 0
        self.speedy = 0
        self.car_up = self.car
        self.car_down = pygame.transform.flip(self.car, 1, 1)
        self.car_left = pygame.transform.rotate(self.car, 90)
        self.car_right = pygame.transform.rotate(self.car, -90)
        self.car_up_right = pygame.transform.rotate(self.car, -45)
        self.car_down_right = pygame.transform.rotate(self.car, -135)
        self.car_up_left = pygame.transform.rotate(self.car, 45)
        self.car_down_left = pygame.transform.rotate(self.car, 135)
        p1_rect=self.rect
        
        
    def update(self):
        global p1_x, p1_y, p1_rect, p2_rect
        keystate = pygame.key.get_pressed()
        self.rect.x=p1_x
        self.rect.y=p1_y
        p1_rect=self.rect
        if keystate[pygame.K_a]:
            if keystate[pygame.K_w] and keystate[pygame.K_a]:
                self.car = self.car_up_left
                self.speedy -= 0.6
                self.speedx -= 0.6
            elif keystate[pygame.K_a] and keystate[pygame.K_s]:
                self.car = self.car_down_left
                self.speedx -= 0.6
                self.speedy += 0.6
            elif keystate[pygame.K_a]:
                self.car = self.car_left
                self.speedx-=0.6
        elif keystate[pygame.K_d]:
            if keystate[pygame.K_d] and keystate[pygame.K_s]:
                self.car = self.car_down_right
                self.speedx += 0.6
                self.speedy += 0.6
            elif keystate[pygame.K_d] and keystate[pygame.K_w]:
                self.speedy -= 0.6
                self.car = self.car_up_right
                self.speedx += 0.6
            elif keystate[pygame.K_d]:
                self.car = self.car_right
                self.speedx += 0.6
        elif keystate[pygame.K_w]:
            self.car = self.car_up
            self.speedy -= 0.6
        elif keystate[pygame.K_s]:
            self.car = self.car_down
            self.speedy += 0.6
        
        if self.rect.right > width:
            self.speedx*=(-0.75)
            p1_x-=5
        elif self.rect.left < 0:
            self.speedx*=(-0.75)
            p1_x+=5
        elif self.rect.bottom > height:
            self.speedy*=(-0.75)
            p1_y-=5
        elif self.rect.top < 0:
            self.speedy*=(-0.75)
            p1_y+=5
        if p1_rect.colliderect(p2_rect):
            if self.speedx > 0:
                self.speedx -= 3
                self.speedx*=(-0.75)
            elif self.speedx < 0:
                self.speedx*=(-0.75)
            if self.speedy > 0:
                self.speedy*=(-0.75)
            elif self.speedy < 0:
                self.speedy*=(-0.75)
        if self.speedx>m_sp1:
            self.speedx=m_sp1
        if self.speedx<-1*m_sp1:
            self.speedx=-1*m_sp1
        if self.speedy>m_sp1:
            self.speedy=m_sp1
        if self.speedy<-1*m_sp1:
            self.speedy=-1*m_sp1
        if self.speedx > 0:
            self.speedx-=0.1
        if self.speedy > 0:
            self.speedy-=0.1
        if self.speedx < 0:
            self.speedx+=0.1
        if self.speedy < 0:
            self.speedy+=0.1
        if self.speedx<0.299 and self.speedx>(-0.299):
            self.speedx=0
        if self.speedy<0.299 and self.speedy>(-0.299):
            self.speedy=0
        p1_y+=self.speedy
        p1_x+=self.speedx
        self.image = self.car



class Race_Map(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = map_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_l]:
            pygame.mixer.music.play()
        self.speedx = 0
        self.speedy = 0
        
#body

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
sound_folder = os.path.join(game_folder, 'sound')
lessgo = pygame.mixer.Sound(os.path.join(sound_folder, 'lessgo.ogg'))
second_player = Second_Player()
player = Player()

tema = pygame.mixer.music.load(os.path.join(sound_folder, 'lessgo_tema.mp3'))

map_img = pygame.image.load(os.path.join(img_folder, 'trassa.png')).convert()
car1_img = pygame.image.load(os.path.join(img_folder, 'g_car'+n_1st_p+'.png')).convert()
car2_img = pygame.image.load(os.path.join(img_folder, 'g_car'+n_2nd_p+'.png')).convert()
map_img = pygame.transform.scale(map_img, (int(width), int(height)))
mask = pygame.mask.from_surface(map_img)
mask_p1 = pygame.mask.from_surface(car1_img)
mask_p2 = pygame.mask.from_surface(car2_img)

all_sprites = pygame.sprite.Group()

Map = Race_Map()
all_sprites.add(Map)
all_sprites.add(player)
all_sprites.add(second_player)

while running:
    all_sprites.update()
    offset1 = (int(p1_x-width / 2), int(p1_y-height / 2))
    offset2 = (int(p2_x-width / 2), int(p2_y-height / 2))
#    if mask.overlap_area(mask_p1, offset1) > 0:
#        m_sp1 = 5
#    else:
#        m_sp1 = 2
#    if mask.overlap_area(mask_p2, offset2) > 0:
#        m_sp2 = 5
#    else:
#        m_sp2 = 2
    clock.tick(FPS)
    screen.fill(GREEN)
    all_sprites.draw(screen)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
pygame.quit()
