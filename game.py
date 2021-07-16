import sys, pygame, math

pygame.init()

size = width, height = 1280, 720
bg_color = 255, 255, 255

screen = pygame.display.set_mode(size)

arrow = pygame.image.load("Assets/arrow.png")
arrow_rect = arrow.get_rect(center = screen.get_rect().center)

def calc_angle(x, y, mX, mY):
    return math.atan2(y-mY, mX-x) * 180 / math.pi

def rotate(image, rect, angle):
    rotate_image = pygame.transform.rotate(image, angle)
    rect = rotate_image.get_rect(center = rect.center)

    return rotate_image, rect


angle = 0

while 1:
    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(bg_color)

    if x == 0: x = 1

    image, rect = rotate(arrow, arrow_rect, angle)
    angle = calc_angle(rect.x, rect.y, x, y)
    
    screen.blit(image, rect)
    pygame.display.flip()


