import pygame, math, time

pygame.init()
CONSOLAS = pygame.font.SysFont("consolas", 24)
clock = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill("white")

colors = pygame.color.THECOLORS
LEN = len(colors)
SQUARES_ON_LINE = round(math.sqrt(LEN))
STEP_X = SCREEN_WIDTH / SQUARES_ON_LINE
STEP_Y = SCREEN_HEIGHT / SQUARES_ON_LINE
for col in colors:
    name = col
    rgba = colors.get(col)
    index = list(colors).index(col)
    y = math.ceil(index / SQUARES_ON_LINE)
    x = index - (y * SQUARES_ON_LINE) + SQUARES_ON_LINE

    drawrect = pygame.Rect(x * STEP_X - STEP_X,
                           y * STEP_Y - STEP_Y,
                           SCREEN_WIDTH / SQUARES_ON_LINE,
                           SCREEN_HEIGHT / SQUARES_ON_LINE)
    pygame.draw.rect(screen, pygame.color.Color(rgba), drawrect)
    pygame.display.update()
    

    #print(f'color: {col}, RBGA: {colors.get(col)}, len: {len(colors)}, index: {list(colors).index(col)}, y: {y}, x: {x}') #len = 665

elapsed = 0
while elapsed < 5000:
    elapsed += clock.tick(60)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x, mouse_y)
    txt_img = pygame.font.Font.render(CONSOLAS, "this", True, "black")
    screen.blit(txt_img, (250, 250))
    pygame.display.update()

pygame.quit()