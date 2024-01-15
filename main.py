from pygame import*
class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed, width=65, height=65):
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed # швидкість переміщення спрайту
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x # координата x спрайту
        self.rect.y = player_y # координата y спрайту

    # метод для відображення спрайту у точці з координатами (x, y)
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

        # клас-спадкоємець для спрайту-гравця (керується стрілками)
class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back = (200, 255, 255)  # колір фону (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
game = True
finish = False
clock = time.Clock()
FPS = 60
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tennis_ball.png', 200, 200, 4, 50, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(back)

        racket1.update_left()
        racket2.update_right()

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)