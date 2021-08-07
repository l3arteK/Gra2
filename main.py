import pygame
from random import randint

pygame.init()

WIDTH = 1200
HEIGHT = 720
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))


class Player:
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
        self.speed = 5
        self.image = pygame.image.load("gracz.png")
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.image.get_width(), self.image.get_height())

    def tick(self, keys):
        if keys[pygame.K_w] and self.y_cord > 0:
            self.y_cord -= self.speed
        if keys[pygame.K_s] and self.y_cord < HEIGHT - self.image.get_height():
            self.y_cord += self.speed
        if keys[pygame.K_a] and self.x_cord > 0:
            self.x_cord -= self.speed
        if keys[pygame.K_d] and self.x_cord < WIDTH - self.image.get_width():
            self.x_cord += self.speed
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.image.get_width(), self.image.get_height())

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


class Cash:

    def __init__(self):
        self.x_cord = randint(0, 1200)
        self.y_cord = randint(0, 670)
        self.image = pygame.image.load("dollar.png")
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, 50, 25)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, 50, 25)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


def main():
    run = True
    player = Player()
    clock = 0
    score = 0
    banknoty = []
    while run:
        clock += pygame.time.Clock().tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if clock >= 3:
            clock = 0
            banknoty.append(Cash())

        player.tick(keys)
        text_img = pygame.font.Font.render(pygame.font.SysFont("arial", 48), "Wynik: " + str(score), True, (0, 0, 0))
        for banknot in banknoty:
            banknot.tick()

        for banknot in banknoty:
            if player.hitbox.colliderect(banknot.hitbox):
                banknoty.remove(banknot)
                score += 1
        window.fill((24, 166, 240))
        player.draw()
        window.blit(text_img, (0, 0))
        for banknot in banknoty:
            banknot.draw()
        pygame.display.update()


if __name__ == "__main__":
    main()
