import pygame, math

pygame.init()
CONSOLAS_SMALL = pygame.font.SysFont("consolas", 23)
clock = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Color Picker")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
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
        rect_name_dict.append((drawrect, name, rgba))

def ColorFromPoint(point):
    for item in rect_name_dict: #(rect, name, rgba)
        if item[0].collidepoint(point):
            if item[1] != None:
                return item[1], item[2]
    else: return "", pygame.color.Color(255, 255, 255, 255)
            
        


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(current_color)
            

    RenderColors()
    mouse_pos = pygame.mouse.get_pos()
    current_color, current_rgba = ColorFromPoint(mouse_pos)
    render_text = pygame.font.Font.render(CONSOLAS_SMALL, current_color, True, pygame.color.Color(255 - current_rgba[0], 255 - current_rgba[1], 255 - current_rgba[2], 510 - current_rgba[3]))
    screen.blit(render_text, (mouse_pos[0] + 10, mouse_pos[1] - 10))
    pygame.display.update()