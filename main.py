import pygame, math

pygame.init()
CONSOLAS = pygame.font.SysFont("consolas", 24)
clock = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill("white")

colors = pygame.color.THECOLORS
rect_name_dict = []
LEN = len(colors)
SQUARES_ON_LINE = round(math.sqrt(LEN))
STEP_X = SCREEN_WIDTH / SQUARES_ON_LINE
STEP_Y = SCREEN_HEIGHT / SQUARES_ON_LINE

def RenderColors():
    global rect_name_dict
    rect_name_dict = []

    screen.fill("white")

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
        rect_name_dict.append((drawrect, name))

def ColorFromPoint(point):
    for item in rect_name_dict:
        if item[0].collidepoint(point):
            return item[1]
        

panic = 0
while panic < 3:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            panic += 1
            print(f"nah no quitting >:)")
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(current_color)
            

    RenderColors()
    mouse_pos = pygame.mouse.get_pos()
    current_color = ColorFromPoint(mouse_pos)
    txt_img = pygame.font.Font.render(CONSOLAS, current_color, True, "black")
    screen.blit(txt_img, mouse_pos)
    pygame.display.update()

print("okay then :(")
pygame.quit()