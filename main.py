import pygame

# ініціалізація гри та вікна
pygame.init()
screen = pygame.display.set_mode((618, 359), flags=pygame.NOFRAME) 
pygame.display.set_caption("My Game")
icon = pygame.image.load("imgs/logo.png")
pygame.display.set_icon(icon)
inGame = True

# музика
pygame.mixer.init()
pygame.mixer.music.load("sounds/lemonade.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # -1 = безкінечний повтор

# налаштування основи
clock = pygame.time.Clock()

bg = pygame.image.load("imgs/background.png")
bgX = 0

myfont = pygame.font.Font("fonts/pixel.ttf", 25)
text = myfont.render("Зіфірка", False, (255, 255, 255))

# анімація персонажа, координати, стан
walkRight = [
    pygame.image.load("imgs/hero/right-2.png"), 
    pygame.image.load("imgs/hero/right-3.png"), 
    pygame.image.load("imgs/hero/right-4.png"), 
    pygame.image.load("imgs/hero/right-1.png"), 
]
walkLeft = [
    pygame.image.load("imgs/hero/left-2.png"), 
    pygame.image.load("imgs/hero/left-3.png"), 
    pygame.image.load("imgs/hero/left-4.png"), 
    pygame.image.load("imgs/hero/left-1.png"), 
]
playerAnimCount = 3
walkDirection = walkRight

playerX = 130
playerY = 250

playerSpeed = 5
jumpHeight = 7

isJump  = False
isGo = True

# запуск гри
while inGame:
    clock.tick(10)

    # відображення обєктів
    screen.blit(bg, (bgX, 0))
    screen.blit(bg, (bgX + 618, 0))
    screen.blit(bg, (bgX - 618, 0))
    if bgX == -618 or bgX == 1236:
        bgX = 0

    screen.blit(text, (120, 10))

    screen.blit(walkDirection[playerAnimCount], (playerX, playerY))

    # анімація персонажа при русі та стрибку
    if isGo and not isJump:
        if playerAnimCount == 3:
            playerAnimCount = 0
        else:
            playerAnimCount += 1
    elif isGo and isJump:
        playerAnimCount = 0
    else:
        playerAnimCount = 3

    # Клавіші для руху персонажа
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        bgX += 3
        walkDirection = walkLeft
        isGo = True
    elif key[pygame.K_d]:
        bgX -= 3
        walkDirection = walkRight
        isGo = True
    else:
        isGo = False
        playerAnimCount = 3

    if key[pygame.K_a] and playerX > 80:
        playerX -= playerSpeed
    elif key[pygame.K_d] and playerX < 618 - 130:
        playerX += playerSpeed  

    if not isJump:
        if key[pygame.K_w]:
            isGo = False
            isJump = True
    else:
        if jumpHeight >= -7:
            if jumpHeight > 0:
                playerY -= (jumpHeight ** 2) / 2
            else:
                playerY += (jumpHeight ** 2) / 2

            jumpHeight -= 1
        else:
            isJump = False
            isGo = True
            jumpHeight = 7

    pygame.display.update()

    # вихід з гри
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inGame = False
                pygame.quit()
