import pygame
pygame.init()

WIDTH = 600
HEIGHT = 600
BLACK = 0,0,0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("white")
pygame.display.set_caption("Matching Game")
pygame.display.update()

candy_crush = pygame.image.load("./images/candycrush.jpeg")
ludo = pygame.image.load("./images/ludo.png")
subway_surfers = pygame.image.load("./images/subwaysurfers.png")
temple_run = pygame.image.load("./images/templerun.png")

screen.blit(candy_crush, (50,100))
screen.blit(ludo, (50,200))
screen.blit(subway_surfers, (50,300))
screen.blit(temple_run, (50,400))

font = pygame.font.SysFont("futura", 45)

text1 = font.render("Subway Surfers", False, BLACK)
text2 = font.render("Candy Crush", False, BLACK)
text3 = font.render("Temple Run", True, BLACK)
text4 = font.render("Ludo", True, BLACK)

screen.blit(text1, (250, 100))
screen.blit(text2, (250, 200))
screen.blit(text3, (250, 300))
screen.blit(text4, (250, 400))
pygame.display.update()

while 1:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, BLACK, (pos), 10, 0)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen, BLACK, (pos), (pos2), 2)
        pygame.draw.circle(screen, BLACK, (pos2), 10, 0)
        pygame.display.update()