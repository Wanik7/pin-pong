import pygame
pygame.init()
W, H = 700, 500
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Пин понг')
clock = pygame.time.Clock()
FPS = 60
run = True

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, img, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed


    def draw(self, win):
        win.blit(self.image, self.rect)

    def update_l(self):
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif Keys[pygame.K_DOWN] and self.rect.bottom < H:
            self.rect.y += self.speed

    def update_r(self):
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif Keys[pygame.K_s] and self.rect.bottom < H:
            self.rect.y += self.speed

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, img, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.speed_y = speed
        self.speed_x = speed
        self.score_l = 0
        self.score_r = 0

    def draw(self, win):
        win.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        is_catch = pygame.sprite.collide_rect(self, Player1)
        if is_catch:
            self.speed_x *= -1
        is_catch1 = pygame.sprite.collide_rect(self, Player2)
        if is_catch1:
            self.speed_x *= -1
        if self.rect.bottom >= H:
            self.speed_y *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1
        if self.rect.x <= 0:
            self.score_r += 1
            self.rect.center = (325, 225)
            self.speed_x *= -1
        if self.rect.right >= W:
            self.score_l += 1
            self.rect.center = (325, 225)
            self.speed_x *= -1

def game():
    Player1.draw(win)
    Player2.draw(win)
    iBall.draw(win)
    Player1.update_l()
    Player2.update_r()
    iBall.update()
    text = font.render(str(iBall.score_l)+':'+ str(iBall.score_r),1,(255,0,0))
    textRect = text.get_rect()
    textRect.center = (W//2, 40)
    win.blit(text, textRect)


Player1 = Player(100, 200, 20, 100, 'Player.png', 5)
Player2 = Player(600, 200, 20, 100, 'Player.png', 5)
iBall = Ball(325, 225, 50, 50, 'Ball.png', 5)

font = pygame.font.SysFont('serif', 100)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((33, 171, 181))
    if iBall.score_l == 15 or iBall.score_r == 15:

    else:

        game()

    pygame.display.update()
    clock.tick(FPS)