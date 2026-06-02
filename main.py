import pygame

# ініціалізація гри
pygame.init()
screen = pygame.display.set_mode((900, 359)) # flags=pygame.NOFRAME
pygame.display.set_caption("My Game")
icon = pygame.image.load("imgs/logo.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# налаштування основи
myfont = pygame.font.Font("fonts/pixel.ttf", 25)
bg = pygame.image.load("imgs/background.png")
bgX = 0
# player = pygame.image.load("imgs/hero/right-1.png")
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


# обєкти для відображення
text = myfont.render("Зіфірка", False, (255, 255, 255))
square = pygame.Surface((100, 100))
square.fill((255, 0, 0))


run = True
playerAnimCount = 3
while run:

    # відображення обєктів
    screen.blit(bg, (bgX, 0))
    screen.blit(bg, (bgX + 618, 0))
    screen.blit(text, (120, 10))
    screen.blit(walkRight[playerAnimCount], (300, 250))
    
    if playerAnimCount == 3:
        playerAnimCount = 0
    else:
        playerAnimCount += 1

    bgX -= 3
    if bgX == -900:
        bgX = 618

    
    # screen.blit(square, (50, 50))
    # pygame.draw.circle(screen, (0, 255, 0), (50, 100), 20)
    # player = pygame.image.load("imgs/logo.png")
    # screen.blit(player, (10, 10))

    pygame.display.update()

    # screen.fill(bg_color)
    # вихід з гри по хрестику обгортки
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w:
        #         bg_color = (0, 255, 0)
        #     elif event.key == pygame.K_s:
        #         bg_color = (0, 0, 255)
        #     elif event.key == pygame.K_a:
        #         bg_color = (255, 0, 0)
        #     elif event.key == pygame.K_d:
        #         bg_color = (255, 255, 0)


    clock.tick(10)