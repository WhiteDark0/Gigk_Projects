
import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

def shear_surface(surface, shear_factor):
    width, height = surface.get_size()
    
    new_width = width + abs(int(height * shear_factor))
    new_surface = pygame.Surface((new_width, height), pygame.SRCALPHA)

    for y in range(height):
        offset = int(y * shear_factor)
        row = surface.subsurface((0, y, width, 1))
        new_surface.blit(row, (offset, y))

    return new_surface

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
BIALY = (255,255,255)
CZARNY = (0,0,0)

def Object():
    surf = pygame.Surface((540,540), pygame.SRCALPHA)
    pygame.draw.circle(surf, ZOLTY, (270,270),170, 0)
    pygame.draw.circle(surf, SZARY, (170,170), 170, 0)
    pygame.draw.circle(surf, BIALY, (350,250), 10, 0)
    pygame.draw.circle(surf, BIALY, (410,290), 10, 0)
    pygame.draw.circle(surf, CZARNY, (350,250), 5, 0)
    pygame.draw.circle(surf, CZARNY, (410,290), 5, 0)
    pygame.draw.circle(surf, BIALY, (348,248), 1, 0)
    pygame.draw.circle(surf, BIALY, (408,288), 1, 0)
    pygame.draw.circle(surf, CZARNY, (340,345), 45, 0)
    pygame.draw.rect(surf, ZOLTY, (285, 300, 100, 55)) 
    pygame.draw.rect(surf, CZARNY, (296, 345, 3, 10)) 
    pygame.draw.rect(surf, CZARNY, (381, 345, 3, 10)) 
    pygame.draw.rect(surf, CZARNY, (287, 355, 10, 3))
    pygame.draw.rect(surf, CZARNY, (383, 355, 10, 3))
    pygame.draw.rect(surf, BIALY, (343, 355, 10, 10))
    pygame.draw.rect(surf, BIALY, (332, 355, 10, 10))
    return surf

def Object1():
    surf = pygame.Surface((540, 540), pygame.SRCALPHA)  
    pygame.draw.rect(surf, CZERWONY, (50, 50, 425, 20))   
    middle_surf = pygame.Surface((600, 25), pygame.SRCALPHA)
    pygame.draw.rect(middle_surf, CZERWONY, (0, 0, 590, 20))
    rotated_middle = pygame.transform.rotate(middle_surf, 45)   
    middle_rect = rotated_middle.get_rect()
    middle_rect.center = (270, 270)
    surf.blit(rotated_middle, middle_rect.topleft)  
    pygame.draw.rect(surf, CZERWONY, (55, 470, 440, 20))  
    return surf

run = True
current = Object()
x = 30
y = 20

while run:
    background_rect = pygame.Rect(30,20,540,540)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

            # rysowanie kwadratów
        #pygame.draw.rect(win, CZERWONY , (10, 30, 100, 100))
        #pygame.draw.rect(win, ZOLTY, (160, 30, 100, 100))
        #pygame.draw.rect(win, ZIELONY, (310, 30, 100, 100))
        # rysowanie kół
        #pygame.draw.circle(win, FIOLETOWY, (60, 200), 50, 0)
        #pygame.draw.circle(win, JASNY_NIEBIESKI, (210, 200), 50, 25)
        #pygame.draw.circle(win, POMARANCZOWY, (360, 200), 50, 5)
        # linia pozioma
        #pygame.draw.line(win, NIEBIESKI, (10, 325), (110, 325), 15)
        # linia pionowa
        #pygame.draw.line(win, SZARY, (210, 275), (210, 375), 5)
        # rysowanie plusa
        #pygame.draw.line(win, NIEBIESKI, (310, 325), (410, 325), 10)
        #pygame.draw.line(win, SZARY, (360, 275), (360, 375), 10)
        # wypisywanie tekstu
        #font = pygame.font.SysFont('comicsans', 30)
        #label = font.render('Tekst do wyświetlania ', 1, (255, 255, 255))
        #win.blit(label, (100, 425))


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_0:
                current = Object()
                x = 30
                y = 20

            if event.key == pygame.K_1:
                current = pygame.transform.scale(Object(), (200,200))
                x = 200
                y = 200

            if event.key == pygame.K_2:
                current = pygame.transform.rotate(Object(), -45)
                x = -65
                y = -50

            if event.key == pygame.K_3:
                temp = pygame.transform.scale(Object(), (200,350))
                current = pygame.transform.rotate(temp, 180)
                x = 190
                y = 80

            if event.key == pygame.K_4:
                current = shear_surface(Object(), 0.5)
                x = -35
                y = 50

            if event.key == pygame.K_5:
                current = pygame.transform.scale(Object(), (250,50))
                x = 200
                y = 20

            if event.key == pygame.K_6:
                temp = shear_surface(Object(), 0.5)
                current = pygame.transform.rotate(temp, 90)
                x = 40
                y = -185

            if event.key == pygame.K_7:
                temp = pygame.transform.scale(Object(), (200,350))
                temp = pygame.transform.rotate(temp, 180)
                current = pygame.transform.flip(temp, True, False)
                x = 200
                y = 80

            if event.key == pygame.K_8:
                temp = pygame.transform.scale(Object(), (250,50))
                current = pygame.transform.rotate(temp, -30)
                x = 100
                y = 400

            if event.key == pygame.K_9:
                temp = shear_surface(Object(), 0.5)
                current = pygame.transform.rotate(temp, 180)
                x = -176
                y = 0

            if event.key == pygame.K_p: #Object for second task
                current = Object1()
                x = 30
                y = 25


    win.fill(BIALY)

    pygame.draw.rect(win, SZARY, background_rect)
    win.blit(current, (x,y))

    pygame.display.update()
