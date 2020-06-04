import pygame, sys, random, time

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.mixer.pre_init(44100, 16, 2, 4096)

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((800, 600))

titleFont = pygame.font.SysFont(None, 60)
titleFont2 = pygame.font.SysFont(None, 100)
winFont = pygame.font.SysFont(None,150)
buttonFont = pygame.font.SysFont(None, 40)

icon = pygame.image.load('cube.jpg')
pygame.display.set_icon(icon)

# # # # # Level Variables # # # # #
attemptNumLevel1 = 1
attemptNumLevel2 = 1
attemptNumLevel3 = 1
attemptNumLevel4 = 1

level1Win = False
level2Win = False
level3Win = False
level4Win = False


def load_map(path):
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map


game_map = load_map('map1')

game_map2 = load_map('map2')

game_map3 = load_map('map3')

game_map4 = load_map('map4')


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (int(x), int(y))
    surface.blit(textobj, textrect)


def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True

    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        rect.bottom = tile.top
        collision_types['bottom'] = True
    return rect, collision_types


def main_menu(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win):
    # # # # # Window Icon and caption # # # # #
    pygame.mixer.music.load("[FREE] The Weeknd x Synthwave 80s Type Beat - SPEEDWAY.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    playerImg = pygame.image.load('cube.jpg')
    squareImg = pygame.image.load('square.png')
    triangleImg = pygame.image.load('triangle.png')
    playerImg.set_colorkey((0, 0, 0))
    pygame.display.set_caption("The Impossible Game")
    background = pygame.image.load('background_menu.jpg')
    click = False
    angle = 0
    while True:
        screen.fill((200, 100, 0))
        screen.blit(background, (0, 0))  # if we want to put a background image
        draw_text('The Impossible Game', titleFont2, (255, 255, 255), screen, 20, 20)
        pygame.draw.line(screen, (255, 255, 255), (0, 95), (800, 95), 5)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 130, 200, 50)
        button_2 = pygame.Rect(50, 230, 200, 50)
        button_3 = pygame.Rect(50, 330, 200, 50)
        button_4 = pygame.Rect(50, 430, 200, 50)

        pygame.draw.rect(screen, (50, 0, 0), button_1)
        pygame.draw.rect(screen, (50, 0, 0), button_2)
        pygame.draw.rect(screen, (50, 0, 0), button_3)
        pygame.draw.rect(screen, (50, 0, 0), button_4)

        screen.blit(playerImg, (350, 300))
        screen.blit(triangleImg, (566, 330))
        screen.blit(squareImg, (310, 394))
        screen.blit(squareImg, (374, 394))
        screen.blit(squareImg, (438, 394))
        screen.blit(squareImg, (502, 394))
        screen.blit(squareImg, (566, 394))
        screen.blit(squareImg, (630, 394))

        draw_text('Play', buttonFont, (255, 255, 255), screen, 150 / 2, 140)
        draw_text('Manual', buttonFont, (255, 255, 255), screen, 150 / 2, 240)
        draw_text('Credits', buttonFont, (255, 255, 255), screen, 150 / 2, 340)
        draw_text('Exit', buttonFont, (255, 255, 255), screen, 150 / 2, 440)

        if button_1.collidepoint((mx, my)):
            if click:
                levelPage(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if button_2.collidepoint((mx, my)):
            if click:
                manual(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if button_3.collidepoint((mx, my)):
            if click:
                credits(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if button_4.collidepoint((mx, my)):
            if click:
                exit()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def levelPage(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win):
    playerImg = pygame.image.load('cube.jpg')
    squareImg = pygame.image.load('square.png')
    triangleImg = pygame.image.load('triangle.png')
    background = pygame.image.load('background_menu.jpg')
    levelPassImg = pygame.image.load('crown.png')
    click = False
    while True:
        screen.fill((200, 100, 0))
        screen.blit(background, (0, 0))  # if we want to put a background image

        draw_text('Levels', titleFont2, (255, 255, 255), screen, 310, 15)
        pygame.draw.line(screen, (255, 255, 255), (0, 78), (800, 78), 5)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)
        button_4 = pygame.Rect(50, 400, 200, 50)
        button_5 = pygame.Rect(50, 500, 200, 50)

        pygame.draw.rect(screen, (50, 0, 0), button_1)
        pygame.draw.rect(screen, (50, 0, 0), button_2)
        pygame.draw.rect(screen, (50, 0, 0), button_3)
        pygame.draw.rect(screen, (50, 0, 0), button_4)
        pygame.draw.rect(screen, (50, 0, 0), button_5)

        draw_text('Level 1', buttonFont, (255, 255, 255), screen, 150 / 2, 110)
        draw_text('Level 2', buttonFont, (255, 255, 255), screen, 150 / 2, 210)
        draw_text('Level 3', buttonFont, (255, 255, 255), screen, 150 / 2, 310)
        draw_text('Level 4', buttonFont, (255, 255, 255), screen, 150 / 2, 410)
        draw_text('Back', buttonFont, (255, 255, 255), screen, 150 / 2, 510)

        screen.blit(playerImg, (350, 300))
        screen.blit(triangleImg, (502, 330))
        screen.blit(triangleImg, (566, 330))
        screen.blit(squareImg, (310, 394))
        screen.blit(squareImg, (374, 394))
        screen.blit(squareImg, (438, 394))
        screen.blit(squareImg, (502, 394))
        screen.blit(squareImg, (566, 394))
        screen.blit(squareImg, (630, 394))
        screen.blit(squareImg, (566, 250))
        screen.blit(squareImg, (630, 250))
        screen.blit(squareImg, (694, 250))
        screen.blit(triangleImg, (694, 186))

        if button_1.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.play(-1)
                level1(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.play(-1)
                level2(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if button_3.collidepoint((mx, my)):
            if click:
                level3(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if button_4.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.play(-1)
                level4(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if button_5.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.play(-1)
                main_menu(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)

        if level1Win == True:
            screen.blit(levelPassImg, (170, 90))
        if level2Win == True:
            screen.blit(levelPassImg, (170, 190))
        if level3Win == True:
            screen.blit(levelPassImg, (170, 290))
        if level4Win == True:
            screen.blit(levelPassImg, (170, 390))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def level1(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win):
    # # # # # Background # # # # # #
    display = pygame.Surface((400, 300))
    background = pygame.image.load('background1.jpg')
    pygame.mixer.music.load("[Free] Vintage Retro 80s Synthwave Vaporwave Synthpop Type Beat.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # # # # # Player # # # # #
    playerImg = pygame.image.load('cube.jpg')
    playerImg.set_colorkey((0, 0, 0))
    rotated_image = pygame.image.load('cube.jpg')
    jumping = False
    jump_count = 12
    fallcount = 0
    angle = 0
    resetflag = 0

    # # # # # Obstacles # # # # # #
    squareImg = pygame.image.load('square.png')
    triangleImg = pygame.image.load('triangle.png')
    winningImg = pygame.image.load('goal.jpg')

    true_scroll = [0, 0]  # x, y scroll starts at (0,0)

    player_rect = pygame.Rect(0, 481, 64, 64)  # left, top, width, height of images

    # # # # # Game Loop # # # # #
    click = False
    running = True
    win = False
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill((20, 20, 20))
        screen.blit(background, (0, 0))  # if we want to put a background image
        if win == True:
            draw_text('Level 1 Clear', winFont, (255, 215, 0), screen, 80, 120)
        draw_text('Attempt ' + str(attemptNumLevel1), titleFont, (255, 255, 255), screen, 300, 20)
        if win == False:
            draw_text('Tap Space Bar or Up-key to Jump', titleFont, (255, 255, 255), screen, 100, 120)

        button_1 = pygame.Rect(20, 20, 200, 50)
        pygame.draw.rect(screen, (50, 0, 0), button_1)
        draw_text('Back', buttonFont, (255, 255, 255), screen, 150 / 2, 30)

        if button_1.collidepoint((mx, my)):
            if click:
                levelPage(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)

        # # # # # Scrolling # # # # #
        true_scroll[0] += (player_rect.x - true_scroll[0] - 400) / 2
        true_scroll[1] += (player_rect.y - true_scroll[1] - 240) / 2
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        tile_rects = []

        pygame.draw.rect(display, (7, 80, 75), pygame.Rect(0, 120, 300, 80))
        pygame.draw.line(screen, (255, 255, 255), (0, 545 - scroll[1]), (800, 545 - scroll[1]), 5)

        tile_rects.append(pygame.Rect(0, 545, 1000000, 1000))

        # # # # # Bliting Obstacles # # # # #

        tile_trig = []
        tile_win = []
        y = 0
        for layer in game_map2:
            x = 0
            for tile in layer:
                if tile == '1':  # square obstacle
                    screen.blit(squareImg, (x * 64 - scroll[0], y * 64 - scroll[1]))
                    tile_rects.append(pygame.Rect(x * 64, y * 64, 64, 64))
                if tile == '2':  # triangle obstacle
                    screen.blit(triangleImg, (x * 64 - scroll[0], y * 64 - scroll[1]))
                    tile_trig.append(pygame.Rect(x * 64, y * 64, 64, 64))
                if tile == '3':  # win obstacle
                    screen.blit(winningImg, (x * 64 - scroll[0], y * 64 - scroll[1]))
                    tile_win.append(pygame.Rect(x * 64, y * 64, 64, 64))
                x += 1
            y += 1

        player_movement = [0, 0]
        player_movement[0] += 12

        # # # # # jumping logic # # # # #
        key = pygame.key.get_pressed()
        if not jumping:
            if (key[pygame.K_UP] or key[pygame.K_SPACE]) and resetflag == 1:
                jumping = True
            player_movement[1] += (fallcount ** 2) // 2
            fallcount += 1
        else:
            resetflag = 0
            if jump_count >= -12:
                neg = 1
                if jump_count < 0:
                    neg = -1
                # player_rect.y -= (jump_count ** 2) // 2 * neg
                player_movement[1] -= (jump_count ** 2) // 2 * neg
                jump_count -= 1
                angle -= 8
                rotated_image = pygame.transform.rotate(playerImg, angle)
            else:
                jumping = False
                jump_count = 12
                angle = 0
                fallcount = 13
                rotated_image = pygame.transform.rotate(playerImg, angle)

        player_rect, collisions = move(player_rect, player_movement, tile_rects)
        player_rect.x -= player_movement[0]
        player_rect.y -= player_movement[1]
        player_rect, collisionstrig = move(player_rect, player_movement, tile_trig)
        player_rect.x -= player_movement[0]
        player_rect.y -= player_movement[1]
        player_rect, collisionsWin = move(player_rect, player_movement, tile_win)

        print(collisions)
        print(collisionstrig)
        print(collisionsWin)

        # # # # # collisions # # # # #

        if collisions['bottom'] == True and jumping == True:
            jumping = False
            jump_count = 12
            angle = 0
            rotated_image = pygame.transform.rotate(playerImg, angle)
            fallcount = 0
            resetflag = 1
        elif collisions['bottom'] == True:
            fallcount = 0
            resetflag = 1

        if collisions['right'] == True:
            attemptNumLevel1 += 1
            pygame.mixer.music.play(-1)
            level1(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        elif collisions['left'] == True:
            attemptNumLevel1 += 1
            pygame.mixer.music.play(-1)
            level1(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)

        if collisionstrig['bottom'] == True:
            attemptNumLevel1 += 1
            pygame.mixer.music.play(-1)
            level1(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if collisionstrig['right'] == True:
            attemptNumLevel1 += 1
            pygame.mixer.music.play(-1)
            level1(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if collisionstrig['left'] == True:
            attemptNumLevel1 += 1
            pygame.mixer.music.play(-1)
            level1(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)

        if collisionsWin['bottom'] == True:
            #attemptNumLevel1 += 1
            #pygame.mixer.music.play(-1)
            #exit()
            #level1(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
            win = True
            level1Win = True
        if collisionsWin['right'] == True:
            #attemptNumLevel1 += 1
            #pygame.mixer.music.play(-1)
            #exit()
            #level1(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
            win = True
            level1Win = True    
        if collisionsWin['left'] == True:
            #attemptNumLevel1 += 1
            #pygame.mixer.music.play(-1)
            #exit()
            #level1(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
            win = True
            level1Win = True
        # # # # # quit - escape # # # # #
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # # # # # update # # # # #
        screen.blit(rotated_image, (player_rect.x - scroll[0], player_rect.y - scroll[1]))

        print(player_rect.y)

        # screen.blit(pygame.transform.scale(display, (800,600)), (0, 0))

        pygame.display.update()
        mainClock.tick(60)

def level2(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win):
    # # # # # Background # # # # # #
    display = pygame.Surface((400, 300))
    background = pygame.image.load('background1.jpg')
    pygame.mixer.music.load("80's Synthwave Electronic Type Beat Levitating Emotional 80s Instrumental Prod. By IAVI.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)


    # # # # # Player # # # # #
    playerImg = pygame.image.load('cube.jpg')
    playerImg.set_colorkey((0, 0, 0))
    rotated_image = pygame.image.load('cube.jpg')
    jumping = False
    jump_count = 12
    fallcount = 0
    angle = 0
    resetflag = 0

    # # # # # Obstacles # # # # # #
    squareImg = pygame.image.load('square.png')
    triangleImg = pygame.image.load('triangle.png')
    winningImg = pygame.image.load('goal.jpg')

    true_scroll = [0, 0]  # x, y scroll starts at (0,0)

    player_rect = pygame.Rect(0, 481, 64, 64)  # left, top, width, height of images

    # # # # # Game Loop # # # # #
    click = False
    running = True
    win = False
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill((20, 20, 20))
        screen.blit(background, (0, 0))  # if we want to put a background image
        draw_text('Attempt ' + str(attemptNumLevel2), titleFont, (255, 255, 255), screen, 300, 20)
        if win == True:
            draw_text('Level 2 Clear', winFont, (255, 215, 0), screen, 80, 120)

        button_1 = pygame.Rect(20, 20, 200, 50)
        pygame.draw.rect(screen, (50, 0, 0), button_1)
        draw_text('Back', buttonFont, (255, 255, 255), screen, 150 / 2, 30)

        if button_1.collidepoint((mx, my)):
            if click:
                levelPage(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)

        # # # # # Scrolling # # # # #
        true_scroll[0] += (player_rect.x - true_scroll[0] - 400) / 2
        true_scroll[1] += (player_rect.y - true_scroll[1] - 240) / 2
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        tile_rects = []

        pygame.draw.rect(display, (7, 80, 75), pygame.Rect(0, 120, 300, 80))
        pygame.draw.line(screen, (255, 255, 255), (0, 545 - scroll[1]), (800, 545 - scroll[1]), 5)

        tile_rects.append(pygame.Rect(0, 545, 1000000, 1000))

        # # # # # Bliting Obstacles # # # # #

        tile_trig = []
        tile_win = []
        y = 0
        for layer in game_map:
            x = 0
            for tile in layer:
                if tile == '1':  # square obstacle
                    screen.blit(squareImg, (x * 64 - scroll[0], y * 64 - scroll[1]))
                    tile_rects.append(pygame.Rect(x * 64, y * 64, 64, 64))
                if tile == '2':  # triangle obstacle
                    screen.blit(triangleImg, (x * 64 - scroll[0], y * 64 - scroll[1]))
                    tile_trig.append(pygame.Rect(x * 64, y * 64, 64, 64))
                if tile == '3':  # triangle obstacle
                    screen.blit(winningImg, (x * 64 - scroll[0], y * 64 - scroll[1]))
                    tile_win.append(pygame.Rect(x * 64, y * 64, 64, 64))
                x += 1
            y += 1

        player_movement = [0, 0]
        player_movement[0] += 12

        # # # # # jumping logic # # # # #
        key = pygame.key.get_pressed()
        if not jumping:
            if (key[pygame.K_UP] or key[pygame.K_SPACE]) and resetflag == 1:
                jumping = True
            player_movement[1] += (fallcount ** 2) // 2
            fallcount += 1
        else:
            resetflag = 0
            if jump_count >= -12:
                neg = 1
                if jump_count < 0:
                    neg = -1
                # player_rect.y -= (jump_count ** 2) // 2 * neg
                player_movement[1] -= (jump_count ** 2) // 2 * neg
                jump_count -= 1
                angle -= 8
                rotated_image = pygame.transform.rotate(playerImg, angle)
            else:
                jumping = False
                jump_count = 12
                angle = 0
                fallcount = 13
                rotated_image = pygame.transform.rotate(playerImg, angle)

        player_rect, collisions = move(player_rect, player_movement, tile_rects)
        player_rect.x -= player_movement[0]
        player_rect.y -= player_movement[1]
        player_rect, collisionstrig = move(player_rect, player_movement, tile_trig)
        player_rect.x -= player_movement[0]
        player_rect.y -= player_movement[1]
        player_rect, collisionsWin = move(player_rect, player_movement, tile_win)

        print(collisions)
        print(collisionstrig)
        print(collisionsWin)

        # # # # # collisions # # # # #

        if collisions['bottom'] == True and jumping == True:
            jumping = False
            jump_count = 12
            angle = 0
            rotated_image = pygame.transform.rotate(playerImg, angle)
            fallcount = 0
            resetflag = 1
        elif collisions['bottom'] == True:
            fallcount = 0
            resetflag = 1

        if collisions['right'] == True:
            attemptNumLevel2 += 1
            pygame.mixer.music.play(-1)
            level2(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        elif collisions['left'] == True:
            attemptNumLevel2 += 1
            pygame.mixer.music.play(-1)
            level2(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)

        if collisionstrig['bottom'] == True:
            attemptNumLevel2 += 1
            pygame.mixer.music.play(-1)
            level2(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if collisionstrig['right'] == True:
            attemptNumLevel2 += 1
            pygame.mixer.music.play(-1)
            level2(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if collisionstrig['left'] == True:
            attemptNumLevel2 += 1
            pygame.mixer.music.play(-1)
            level2(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)

        if collisionsWin['bottom'] == True:
            win = True
            level2Win = True
            #attemptNumLevel1 += 1
            #pygame.mixer.music.play(-1)
            #exit()
            #level2(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if collisionsWin['right'] == True:
            win = True
            level2Win = True
            #attemptNumLevel1 += 1
            #pygame.mixer.music.play(-1)
            #exit()
            #level2(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)

        if collisionsWin['left'] == True:
            win = True
            level2Win = True
            #attemptNumLevel1 += 1
            #pygame.mixer.music.play(-1)
            #exit()
            #level2(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)

        # # # # # quit - escape # # # # #
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # # # # # update # # # # #
        screen.blit(rotated_image, (player_rect.x - scroll[0], player_rect.y - scroll[1]))

        print(player_rect.y)

        # screen.blit(pygame.transform.scale(display, (800,600)), (0, 0))

        pygame.display.update()
        mainClock.tick(60)

def level3(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win):
    # # # # # Background # # # # # #
    display = pygame.Surface((400, 300))
    background = pygame.image.load('background1.jpg')
    pygame.mixer.music.load("[FREE] The Weeknd X 80s Type Beat - Demons In The Night Blinding Lights Type Beat.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # # # # # Player # # # # #
    playerImg = pygame.image.load('cube.jpg')
    playerImg.set_colorkey((0, 0, 0))
    rotated_image = pygame.image.load('cube.jpg')
    jumping = False
    jump_count = 12
    fallcount = 0
    angle = 0
    resetflag = 0

    # # # # # Obstacles # # # # # #
    squareImg = pygame.image.load('square.png')
    triangleImg = pygame.image.load('triangle.png')
    winningImg = pygame.image.load('goal.jpg')

    true_scroll = [0, 0]  # x, y scroll starts at (0,0)

    player_rect = pygame.Rect(0, 481, 64, 64)  # left, top, width, height of images

    # # # # # Game Loop # # # # #
    click = False
    running = True
    win = False
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill((20, 20, 20))
        screen.blit(background, (0, 0))  # if we want to put a background image
        draw_text('Attempt ' + str(attemptNumLevel3), titleFont, (255, 255, 255), screen, 300, 20)
        if win == True:
            draw_text('Level 3 Clear', winFont, (255, 215, 0), screen, 80, 120)

        button_1 = pygame.Rect(20, 20, 200, 50)
        pygame.draw.rect(screen, (50, 0, 0), button_1)
        draw_text('Back', buttonFont, (255, 255, 255), screen, 150 / 2, 30)

        if button_1.collidepoint((mx, my)):
            if click:
                levelPage(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)

        # # # # # Scrolling # # # # #
        true_scroll[0] += (player_rect.x - true_scroll[0] - 400) / 2
        true_scroll[1] += (player_rect.y - true_scroll[1] - 240) / 2
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        tile_rects = []

        pygame.draw.rect(display, (7, 80, 75), pygame.Rect(0, 120, 300, 80))
        pygame.draw.line(screen, (255, 255, 255), (0, 545 - scroll[1]), (800, 545 - scroll[1]), 5)

        tile_rects.append(pygame.Rect(0, 545, 1000000, 1000))

        # # # # # Bliting Obstacles # # # # #

        tile_trig = []
        tile_win = []
        y = 0
        for layer in game_map3:
            x = 0
            for tile in layer:
                if tile == '1':  # square obstacle
                    screen.blit(squareImg, (x * 64 - scroll[0], y * 64 - scroll[1]))
                    tile_rects.append(pygame.Rect(x * 64, y * 64, 64, 64))
                if tile == '2':  # triangle obstacle
                    screen.blit(triangleImg, (x * 64 - scroll[0], y * 64 - scroll[1]))
                    tile_trig.append(pygame.Rect(x * 64, y * 64, 64, 64))
                if tile == '3':  # triangle obstacle
                    screen.blit(winningImg, (x * 64 - scroll[0], y * 64 - scroll[1]))
                    tile_win.append(pygame.Rect(x * 64, y * 64, 64, 64))
                x += 1
            y += 1

        player_movement = [0, 0]
        player_movement[0] += 12

        # # # # # jumping logic # # # # #
        key = pygame.key.get_pressed()
        if not jumping:
            if (key[pygame.K_UP] or key[pygame.K_SPACE]) and resetflag == 1:
                jumping = True
            player_movement[1] += (fallcount ** 2) // 2
            fallcount += 1
        else:
            resetflag = 0
            if jump_count >= -12:
                neg = 1
                if jump_count < 0:
                    neg = -1
                # player_rect.y -= (jump_count ** 2) // 2 * neg
                player_movement[1] -= (jump_count ** 2) // 2 * neg
                jump_count -= 1
                angle -= 8
                rotated_image = pygame.transform.rotate(playerImg, angle)
            else:
                jumping = False
                jump_count = 12
                angle = 0
                fallcount = 13
                rotated_image = pygame.transform.rotate(playerImg, angle)

        player_rect, collisions = move(player_rect, player_movement, tile_rects)
        player_rect.x -= player_movement[0]
        player_rect.y -= player_movement[1]
        player_rect, collisionstrig = move(player_rect, player_movement, tile_trig)
        player_rect.x -= player_movement[0]
        player_rect.y -= player_movement[1]
        player_rect, collisionsWin = move(player_rect, player_movement, tile_win)

        print(collisions)
        print(collisionstrig)
        print(collisionsWin)

        # # # # # collisions # # # # #

        if collisions['bottom'] == True and jumping == True:
            jumping = False
            jump_count = 12
            angle = 0
            rotated_image = pygame.transform.rotate(playerImg, angle)
            fallcount = 0
            resetflag = 1
        elif collisions['bottom'] == True:
            fallcount = 0
            resetflag = 1

        if collisions['right'] == True:
            attemptNumLevel3 += 1
            pygame.mixer.music.play(-1)
            level3(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        elif collisions['left'] == True:
            attemptNumLevel3 += 1
            pygame.mixer.music.play(-1)
            level3(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)

        if collisionstrig['bottom'] == True:
            attemptNumLevel3 += 1
            pygame.mixer.music.play(-1)
            level3(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if collisionstrig['right'] == True:
            attemptNumLevel3 += 1
            pygame.mixer.music.play(-1)
            level3(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if collisionstrig['left'] == True:
            attemptNumLevel3 += 1
            pygame.mixer.music.play(-1)
            level3(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)

        if collisionsWin['bottom'] == True:
            #attemptNumLevel1 += 1
            #pygame.mixer.music.play(-1)
            #exit()
            #level3(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
            win = True
            level3Win = True
        if collisionsWin['right'] == True:
            #attemptNumLevel1 += 1
            #pygame.mixer.music.play(-1)
            #exit()
            #level3(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
            win = True
            level3Win = True
        if collisionsWin['left'] == True:
            #attemptNumLevel1 += 1
            #pygame.mixer.music.play(-1)
            #exit()
            #level3(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
            win = True
            level3Win = True
        # # # # # quit - escape # # # # #
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # # # # # update # # # # #
        screen.blit(rotated_image, (player_rect.x - scroll[0], player_rect.y - scroll[1]))

        print(player_rect.y)

        # screen.blit(pygame.transform.scale(display, (800,600)), (0, 0))

        pygame.display.update()
        mainClock.tick(60)

def level4(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win):
    # # # # # Background # # # # # #
    display = pygame.Surface((400, 300))
    background = pygame.image.load('background1.jpg')
    pygame.mixer.music.load("[FREE] The Weeknd x Synthwave Type Beat - INCEPTION Retrowave 80s Synth Pop Instrumental.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # # # # # Player # # # # #
    playerImg = pygame.image.load('cube.jpg')
    playerImg.set_colorkey((0, 0, 0))
    rotated_image = pygame.image.load('cube.jpg')
    jumping = False
    jump_count = 12
    fallcount = 0
    angle = 0
    resetflag = 0

    # # # # # Obstacles # # # # # #
    squareImg = pygame.image.load('square.png')
    triangleImg = pygame.image.load('triangle.png')
    winningImg = pygame.image.load('goal.jpg')

    true_scroll = [0, 0]  # x, y scroll starts at (0,0)

    player_rect = pygame.Rect(0, 481, 64, 64)  # left, top, width, height of images

    # # # # # Game Loop # # # # #
    click = False
    running = True
    win = False
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill((20, 20, 20))
        screen.blit(background, (0, 0))  # if we want to put a background image
        draw_text('Attempt ' + str(attemptNumLevel4), titleFont, (255, 255, 255), screen, 300, 20)
        if win == True:
            draw_text('You Win!', winFont, (255, 215, 0), screen, 80, 120)

        button_1 = pygame.Rect(20, 20, 200, 50)
        pygame.draw.rect(screen, (50, 0, 0), button_1)
        draw_text('Back', buttonFont, (255, 255, 255), screen, 150 / 2, 30)

        if button_1.collidepoint((mx, my)):
            if click:
                levelPage(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)

        # # # # # Scrolling # # # # #
        true_scroll[0] += (player_rect.x - true_scroll[0] - 400) / 2
        true_scroll[1] += (player_rect.y - true_scroll[1] - 240) / 2
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        tile_rects = []

        pygame.draw.rect(display, (7, 80, 75), pygame.Rect(0, 120, 300, 80))
        pygame.draw.line(screen, (255, 255, 255), (0, 545 - scroll[1]), (800, 545 - scroll[1]), 5)

        tile_rects.append(pygame.Rect(0, 545, 1000000, 1000))

        # # # # # Bliting Obstacles # # # # #

        tile_trig = []
        tile_win = []
        y = 0
        for layer in game_map4:
            x = 0
            for tile in layer:
                if tile == '1':  # square obstacle
                    screen.blit(squareImg, (x * 64 - scroll[0], y * 64 - scroll[1]))
                    tile_rects.append(pygame.Rect(x * 64, y * 64, 64, 64))
                if tile == '2':  # triangle obstacle
                    screen.blit(triangleImg, (x * 64 - scroll[0], y * 64 - scroll[1]))
                    tile_trig.append(pygame.Rect(x * 64, y * 64, 64, 64))
                if tile == '3':  # triangle obstacle
                    screen.blit(winningImg, (x * 64 - scroll[0], y * 64 - scroll[1]))
                    tile_win.append(pygame.Rect(x * 64, y * 64, 64, 64))
                x += 1
            y += 1

        player_movement = [0, 0]
        player_movement[0] += 12

        # # # # # jumping logic # # # # #
        key = pygame.key.get_pressed()
        if not jumping:
            if (key[pygame.K_UP] or key[pygame.K_SPACE]) and resetflag == 1:
                jumping = True
            player_movement[1] += (fallcount ** 2) // 2
            fallcount += 1
        else:
            resetflag = 0
            if jump_count >= -12:
                neg = 1
                if jump_count < 0:
                    neg = -1
                # player_rect.y -= (jump_count ** 2) // 2 * neg
                player_movement[1] -= (jump_count ** 2) // 2 * neg
                jump_count -= 1
                angle -= 8
                rotated_image = pygame.transform.rotate(playerImg, angle)
            else:
                jumping = False
                jump_count = 12
                angle = 0
                fallcount = 13
                rotated_image = pygame.transform.rotate(playerImg, angle)

        player_rect, collisions = move(player_rect, player_movement, tile_rects)
        player_rect.x -= player_movement[0]
        player_rect.y -= player_movement[1]
        player_rect, collisionstrig = move(player_rect, player_movement, tile_trig)
        player_rect.x -= player_movement[0]
        player_rect.y -= player_movement[1]
        player_rect, collisionsWin = move(player_rect, player_movement, tile_win)

        print(collisions)
        print(collisionstrig)
        print(collisionsWin)

        # # # # # collisions # # # # #

        if collisions['bottom'] == True and jumping == True:
            jumping = False
            jump_count = 12
            angle = 0
            rotated_image = pygame.transform.rotate(playerImg, angle)
            fallcount = 0
            resetflag = 1
        elif collisions['bottom'] == True:
            fallcount = 0
            resetflag = 1

        if collisions['right'] == True:
            attemptNumLevel4 += 1
            pygame.mixer.music.play(-1)
            level4(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        elif collisions['left'] == True:
            attemptNumLevel4 += 1
            pygame.mixer.music.play(-1)
            level4(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)

        if collisionstrig['bottom'] == True:
            attemptNumLevel4 += 1
            pygame.mixer.music.play(-1)
            level4(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if collisionstrig['right'] == True:
            attemptNumLevel4 += 1
            pygame.mixer.music.play(-1)
            level4(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        if collisionstrig['left'] == True:
            attemptNumLevel4 += 1
            pygame.mixer.music.play(-1)
            level4(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)

        if collisionsWin['bottom'] == True:
            #attemptNumLevel3 += 1
            #pygame.mixer.music.play(-1)
            #exit()
            #level4(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
            win = True
            level4Win = True
        if collisionsWin['right'] == True:
            #attemptNumLevel3 += 1
            #pygame.mixer.music.play(-1)
            #exit()
            #level4(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
            win = True
            level4Win = True
        if collisionsWin['left'] == True:
            #attemptNumLevel3 += 1
            #pygame.mixer.music.play(-1)
            #exit()
            #level4(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
            win = True
            level4Win = True
        # # # # # quit - escape # # # # #
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # # # # # update # # # # #
        screen.blit(rotated_image, (player_rect.x - scroll[0], player_rect.y - scroll[1]))

        print(player_rect.y)

        # screen.blit(pygame.transform.scale(display, (800,600)), (0, 0))

        pygame.display.update()
        mainClock.tick(60)


def manual(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win):
    # # # # # images # # # # #
    playerImg = pygame.image.load('cube.jpg')
    squareImg = pygame.image.load('square.png')
    triangleImg = pygame.image.load('triangle.png')
    background = pygame.image.load('background_menu.jpg')
    click = False
    while True:
        screen.fill((200, 100, 0))
        screen.blit(background, (0, 0))  # if we want to put a background image

        draw_text('Manual', titleFont, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(20, 20, 200, 50)
        pygame.draw.rect(screen, (50, 0, 0), button_1)
        draw_text('Back', buttonFont, (255, 255, 255), screen, 150 / 2, 30)

        if button_1.collidepoint((mx, my)):
            if click:
                main_menu(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        # # # # # Text box # # # # #
        # box = pygame.Rect(60, 90, 700, 400)
        # pygame.draw.rect(screen, (200, 150, 50), box)
        # # # # # text # # # # #
        draw_text('Keys', titleFont2, (255, 255, 255), screen, 300, 80)
        pygame.draw.line(screen, (255, 255, 255), (0, 160), (800, 160), 5)
        draw_text('Tap space bar or up-key to jump', titleFont, (255, 255, 255), screen, 100, 200)

        screen.blit(playerImg, (260, 264))
        screen.blit(triangleImg, (400, 264))
        screen.blit(triangleImg, (464, 264))
        screen.blit(squareImg, (260, 330))
        screen.blit(squareImg, (324, 330))
        screen.blit(squareImg, (378, 330))
        screen.blit(squareImg, (442, 330))
        screen.blit(squareImg, (496, 330))
        screen.blit(squareImg, (260, 394))
        screen.blit(squareImg, (324, 394))
        screen.blit(squareImg, (378, 394))
        screen.blit(squareImg, (442, 394))
        screen.blit(squareImg, (496, 394))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def credits(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win):
    background = pygame.image.load('background_menu.jpg')

    click = False
    while True:
        screen.fill((200, 100, 0))
        screen.blit(background, (0, 0))  # if we want to put a background image
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(20, 20, 200, 50)
        pygame.draw.rect(screen, (50, 0, 0), button_1)
        draw_text('Back', buttonFont, (255, 255, 255), screen, 150 / 2, 30)

        if button_1.collidepoint((mx, my)):
            if click:
                main_menu(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
        # # # # # Text box # # # # #
        # box = pygame.Rect(60, 90, 700, 400)
        # pygame.draw.rect(screen, (200, 150, 50), box)

        # # # # # text # # # # #
        draw_text('Credits', titleFont2, (255, 255, 255), screen, 300, 80)
        pygame.draw.line(screen, (255, 255, 255), (0, 160), (800, 160), 5)

        draw_text('Ryan Hail', titleFont, (255, 255, 255), screen, 300, 200)
        draw_text('James Plasko', titleFont, (255, 255, 255), screen, 300, 260)
        draw_text('Taka Ohashi', titleFont, (255, 255, 255), screen, 300, 320)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def closeGame():
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main_menu(attemptNumLevel1, attemptNumLevel2, attemptNumLevel3, attemptNumLevel4, level1Win, level2Win, level3Win, level4Win)
