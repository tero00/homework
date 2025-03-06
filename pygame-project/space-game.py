import pygame
import math
import random
import time
import os

pygame.init()
coin = pygame.image.load(os.path.join(os.path.dirname(__file__), "coin.png"))
mob = pygame.image.load(os.path.join(os.path.dirname(__file__), "enemy.png"))
pygame.display.set_caption("Space Ghost's Coins")
pygame.display.set_icon(coin)
width = 1200
width_center = int(width/2)
height = 780
height_center = int(height/2)
i = 0
game_played = False
screen = pygame.display.set_mode((width, height))
kello = pygame.time.Clock()
deadzone = (range(width_center-50, width_center+50), range(height_center-50, height_center+50))
dir_sectors = [((math.pi*n)/20, (math.pi*n+1)/20) for n in range(0, 20)]
score_text = 0
mobs = []
coins = []
big_stars = []
small_stars = []
mini_stars = []
dim_stars = []
exhaust = []
    
#when clicking on X
def check_quit(event):
    if event.type == pygame.QUIT:
        return True
    
#when pressing space
def can_start(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            return True
    
def get_mouse_x():
    return pygame.mouse.get_pos()[0]
    
def get_mouse_y():
    return pygame.mouse.get_pos()[1]
    
#if touching a coin
def check_contact_coin():
    for c in coins:
        if get_mouse_x() in range(c[0], c[0]+33) and get_mouse_y() in range(c[1], c[1]+35):
            coins.remove(c)
            return True
    
#if touching a ghost
def check_contact_mob():
    for m in mobs:
        if get_mouse_x() in range(m[0]+20, m[0]+58) and get_mouse_y() in range(m[1]+5, m[1]+55):
            return True
    
#calculate mouses direction from center of screen
def calculate_v():
    dir = 0
    dirs = [(7, 0), (7, 1), (7, 2), (6, 3), (6, 4), (5, 5), (4, 6), (3, 6), (2, 7), (1, 7), (0, 7), (-1, 7), (-2, 7), (-3, 6), (-4, 6), (-5, 5), (-6, 4), (-6, 3), (-7, 2), (-7, 1), \
               (7, -1), (7, -2), (6, -3), (6, -4), (5, -5), (4, -6), (3, -6), (2, -7), (1, -7), (0, -7), (-1, -7), (-2, -7), (-3, -6), (-4, -6), (-5, -5), (-6, -4), (-6, -3), (-7, -2), (-7, -1), (-7, -0)]
    hyp = math.hypot(get_mouse_x()-width_center, get_mouse_y()-height_center)
    if hyp == 0:
        hyp += 1
    for sec in dir_sectors:
        if sec[1] < math.acos((get_mouse_x()-width_center)/hyp):
            dir = dir_sectors.index(sec)
    if get_mouse_y() > height_center:
        dir += 20
    for s in dirs:
        if dir == dirs.index(s):
            v = s
    return v
    
#generate coins and ghosts to protect them
def gen_coin():
    gen_location = [random.randrange(width+400)-200, random.randrange(height+400)-200]
    if gen_location[0] > width+100 or gen_location[0] < -100 or gen_location[1] < -100 or gen_location[1] > height+100:
        if all(gen_location[0] < c[0]-200 or gen_location[0] > c[0]+200 or gen_location[1] < c[1]-200 or gen_location[1] > c[1]+200 for c in coins):
            coins.append(gen_location)
            for i in range(random.randrange(1,3)):
                mobs.append([gen_location[0]+random.randrange(300)-150, gen_location[1]+random.randrange(300)-150])
def gen_exhaust():
    exhaust.append([get_mouse_x(), get_mouse_y(), 1])
    
#generate background stars

def generate(radius, lista):
    gen_location = [random.randrange(width+400)-200, random.randrange(height+400)-200]
    if gen_location[0] > width+100 or gen_location[0] < -100 or gen_location[1] < -100 or gen_location[1] > height+100:
        if all(gen_location[0] < s[0]-radius or gen_location[0] > s[0]+radius or gen_location[1] < s[1]-radius or gen_location[1] > s[1]+radius for s in lista):
            lista.append(gen_location)
    
#only used in the start
def gen_start_stars():
    gen_location = [random.randrange(width+400)-200, random.randrange(height+400)-200]
    if all(gen_location[0] < s[0]-40 or gen_location[0] > s[0]+40 or gen_location[1] < s[1]-40 or gen_location[1] > s[1]+40 for s in dim_stars):
        dim_stars.append(gen_location)
    elif all(gen_location[0] < s[0]-80 or gen_location[0] > s[0]+80 or gen_location[1] < s[1]-80 or gen_location[1] > s[1]+80 for s in mini_stars):
        mini_stars.append(gen_location)
    elif all(gen_location[0] < s[0]-200 or gen_location[0] > s[0]+200 or gen_location[1] < s[1]-200 or gen_location[1] > s[1]+200 for s in small_stars):
        small_stars.append(gen_location)
    elif all(gen_location[0] < s[0]-800 or gen_location[0] > s[0]+800 or gen_location[1] < s[1]-800 or gen_location[1] > s[1]+800 for s in big_stars):
        big_stars.append(gen_location)
    
#delete everything that's too far away
def delete_old():
    for c in coins:
        if c[0] > 2000 or c[0] < -2000 or c[1] > 2000 or c[0] < -2000:
            coins.remove(c)
    for m in mobs:
        if m[0] > 2000 or m[0] < -2000 or m[1] > 2000 or m[0] < -2000:
            mobs.remove(m)
    for s in big_stars:
        if s[0] > 2000 or s[0] < -2000 or s[1] > 2000 or s[0] < -2000:
            big_stars.remove(s)
    for s in small_stars:
        if s[0] > 2000 or s[0] < -2000 or s[1] > 2000 or s[0] < -2000:
            small_stars.remove(s)
    for s in mini_stars:
        if s[0] > 2000 or s[0] < -2000 or s[1] > 2000 or s[0] < -2000:
            mini_stars.remove(s)
    
#move everything
def move(v, slow):
    for m in mobs:
        m[0] -= v[0]
        m[1] += v[1]
    for c in coins:
        c[0] -= v[0]
        c[1] += v[1]
    for e in exhaust:
        e[0] -= int(v[0]*1.5)
        e[1] += int(v[1]*1.5)
    if slow%2 == 0:
        for s in big_stars:
            s[0] -= v[0]
            s[1] += v[1]
    if slow%5 == 0:
        for s in small_stars:
            s[0] -= int(v[0]*0.5)
            s[1] += int(v[1]*0.5)
    if slow%10 == 0:
        for s in mini_stars:
            s[0] -= int(v[0]*0.5)
            s[1] += int(v[1]*0.5)
    if slow == 0:
        for s in dim_stars:
            s[0] -= int(v[0]*0.5)
            s[1] += int(v[1]*0.5)
    
#when releasing mouse button
def decelerate(v, s):
    if s%2 == 0 and s > 20:
        move(v, s)
    else: 
        if s%4 == 0:
            move(v, s)
    
#add score text to screen
def display_score(score, italic, bold, text):
    if italic:
        text = pygame.font.SysFont("Courier New", 54, italic = True).render(f"score {score}", True, (255, 255, 0))
        screen.blit(text, (500, height-100))
    elif bold:
        text = pygame.font.SysFont("Courier New", 64, bold = True).render(f"score {score}", True, (255, 255, 0))
        screen.blit(text, (478, height-100))
    else: 
        text = pygame.font.SysFont("Courier New", 54, bold = True).render(f"score {score}", True, (255, 255, 0))
        screen.blit(text, (500, height-100))
    
def draw_big_stars():
    for s in big_stars:
        pygame.draw.circle(screen, (30, 30,50), (s[0], s[1]), 17)
        pygame.draw.line(screen, (30, 30, 50), (s[0]-25, s[1]), (s[0]+25, s[1]), 8)
        pygame.draw.line(screen, (30, 30, 50), (s[0], s[1]-25), (s[0], s[1]+25), 8)
        pygame.draw.line(screen, (30, 30, 50), (s[0]-61, s[1]), (s[0]+61, s[1]), 3)
        pygame.draw.line(screen, (30, 30, 50), (s[0], s[1]-61), (s[0], s[1]+61), 3)
        pygame.draw.circle(screen, (50, 50, 80), (s[0], s[1]), 11)
        pygame.draw.line(screen, (50, 50, 80), (s[0]-17, s[1]), (s[0]+17, s[1]), 5)
        pygame.draw.line(screen, (50, 50, 80), (s[0], s[1]-17), (s[0], s[1]+17), 5)
        pygame.draw.line(screen, (50, 50, 80), (s[0]-41, s[1]), (s[0]+41, s[1]), 2)
        pygame.draw.line(screen, (50, 50, 80), (s[0], s[1]-41), (s[0], s[1]+41), 2)
        pygame.draw.circle(screen, (255, 255, 255), (s[0], s[1]), 6)
        pygame.draw.line(screen, (255, 255, 255), (s[0]-10, s[1]), (s[0]+10, s[1]), 3)
        pygame.draw.line(screen, (255, 255, 255), (s[0], s[1]-10), (s[0], s[1]+10), 3)
        pygame.draw.line(screen, (255, 255, 255), (s[0]-25, s[1]), (s[0]+25, s[1]), 1)
        pygame.draw.line(screen, (255, 255, 255), (s[0], s[1]-25), (s[0], s[1]+25), 1)
    
def draw_small_stars():
    for s in small_stars:
        pygame.draw.circle(screen, (30, 30, 50), (s[0], s[1]), 7)
        pygame.draw.line(screen, (30, 30, 50), (s[0]-16, s[1]), (s[0]+16, s[1]), 3)
        pygame.draw.line(screen, (30, 30, 50), (s[0], s[1]-16), (s[0], s[1]+16), 3)
        pygame.draw.circle(screen, (255, 255, 255), (s[0], s[1]), 3)
        pygame.draw.line(screen, (255, 255, 255), (s[0]-7, s[1]), (s[0]+7, s[1]), 1)
        pygame.draw.line(screen, (255, 255, 255), (s[0], s[1]-7), (s[0], s[1]+7), 1)
    
def draw_mini_stars():
    for s in mini_stars:
        pygame.draw.circle(screen, (30, 30, 50), (s[0], s[1]), 4) 
        pygame.draw.line(screen, (30, 30, 50), (s[0]-9, s[1]), (s[0]+9, s[1]), 1)
        pygame.draw.line(screen, (30, 30, 50), (s[0], s[1]-9), (s[0], s[1]+9), 1)     
        pygame.draw.circle(screen, (255, 255, 255), (s[0], s[1]), 2)      
    
def draw_dim_stars():
    for s in dim_stars:
        pygame.draw.circle(screen, (30, 30, 50), (s[0], s[1]), 2) 
        pygame.draw.line(screen, (30, 30, 50), (s[0]-3, s[1]), (s[0]+3, s[1]), 1) 
        pygame.draw.line(screen, (30, 30, 50), (s[0], s[1]-3), (s[0], s[1]+3), 1)  
    
def game_start():
    mobs.clear()
    coins.clear()
    big_stars.clear()
    small_stars.clear()
    mini_stars.clear()
    game_on = True
    movement = False
    slow = 0
    slowing = 0
    score = 0
    stay_italic = 0
    stay_bold = 0
    start_time = time.perf_counter()
    
    #generate background when starting
    for i in range(0, 1000):
        gen_start_stars()
    
    while game_on:
        #clear screen
        screen.fill((15, 15, 20))
        #genenerate coins if moving
        if movement:
            gen_coin()
            generate(800, big_stars)
            generate(200, small_stars)
            generate(80, mini_stars)
            generate(40, dim_stars)
        #delete old things
        if movement:
            delete_old()
        #draw stars
        draw_dim_stars()
        draw_mini_stars()
        draw_small_stars()
        draw_big_stars()
        #draw coins
        for c in coins:
            screen.blit(coin, (c[0], c[1]))
        #draw mobs
        for m in mobs:
            screen.blit(mob, (m[0], m[1]))
        #draw exhaust
        for e in exhaust:
            pygame.draw.circle(screen, (245-e[2]*6, 245-e[2]*6, 255-e[2]*6), (e[0], e[1]), e[2])
            if random.randrange(2) == 1:
                e[2] += 3
            if e[2] > 39:
                exhaust.remove(e)
        #move
        if movement:
            v = calculate_v()
            move(v, slow)
            gen_exhaust()
        #move slowly if recently released button
        if movement is False and slowing > 0:
            decelerate(v, slow)
            slowing -= 1
    
        if slow <= 40:
            slow += 1
        else: slow = 0
            
        #check input
        for e in pygame.event.get():
            #exit
            if check_quit(e):
                exit()
            if can_start(e):
                game_start()
            #if pressing mouse button 1
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    movement = True
            #if releasing mouse button 1
            if e.type == pygame.MOUSEBUTTONUP:
                if e.button == 1:
                    v = calculate_v()
                    slowing = 25
                    movement = False
    
        #if cursor touching anything
        if check_contact_coin():
            score += 1
            stay_bold = 20
        if check_contact_mob():
            score = 0
            stay_italic = 20
    
        #display score
        if stay_italic > 0:
            display_score(score, True, False, score_text)
            stay_italic -= 1
        elif stay_bold > 0:
            display_score(score, False, True, score_text)
            stay_bold -= 1
        else: 
            display_score(score, False, False, score_text)
    
        pygame.display.flip()
        kello.tick(120)
        if score >= 20:
            game_on = False
    return time.perf_counter() - start_time
    
def menu(i, g):
    while True:
        for e in pygame.event.get():
            if check_quit(e):
                exit()    
            #game on
            if can_start(e):
                g = True
                end_time = int(game_start())
                print(end_time)
                screen.fill((15, 15, 18))
                screen.blit(pygame.font.SysFont("Courier New", 80).render(f"game finished in", True, (255, 255, 0)), (10, height_center))
                screen.blit(pygame.font.SysFont("Courier New", 80).render(f"{end_time} seconds", True, (255, 255, 0)), (10, height_center+80))
                
        if not g:
            #start screen
            screen.fill((15, 15, 18))
            font_size = 70 - int(math.sin(i)*5)
            screen.blit(pygame.font.SysFont("Courier New", 40).render(f"Collect 20 coins as fast as you can", True, (255, 255, 0)), (10, 20))
            screen.blit(pygame.font.SysFont("Courier New", 40).render(f"But watch out for the ghosts as ", True, (255, 255, 0)), (10, 60))
            screen.blit(pygame.font.SysFont("Courier New", 40).render(f"they want their coins back", True, (255, 255, 0)), (10, 100))
            screen.blit(pygame.font.SysFont("Courier New", 40).render(f"[collect coins by hovering over them]", True, (255, 255, 0)), (10, 140))
            screen.blit(pygame.font.SysFont("Courier New", 40).render(f"[left-click to fly]", True, (255, 255, 0)), (10, 180))
            screen.blit(pygame.font.SysFont("Courier New", font_size).render(f"press space to start", True, (255, 255, 255)), (width_center-300-3*font_size, height_center-int(font_size/2)))
            screen.blit(pygame.font.SysFont("Courier New", font_size).render(f"or to restart", True, (255, 255, 255)), (width_center-100-font_size, height_center+80-int(font_size/2)))
            i += 0.3
        pygame.display.flip()
        kello.tick(60)
    
screen.fill((15, 15, 15))
menu(i, game_played)