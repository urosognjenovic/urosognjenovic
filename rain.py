import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rain")

fontPath = "./PixelifySans-Regular.ttf"
fontSize = 36
font = pygame.font.Font(fontPath, fontSize)

class Raindrop:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.speed = random.randint(15, 45)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-HEIGHT, 0)
            self.x = random.randint(0, WIDTH)

    def draw(self):
        pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x, self.y + 5), 2)

raindrops = [Raindrop() for _ in range(200)]

clock = pygame.time.Clock()

while True:
    screen.fill(BLACK)

    textSurface = font.render("Ougi", True, WHITE)
    textRect = textSurface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(textSurface, textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for drop in raindrops:
        drop.fall()
        drop.draw()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()