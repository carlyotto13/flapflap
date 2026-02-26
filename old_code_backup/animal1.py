class Animal:
    def __init__(self):
        self.IMGS = []
        self.x = 0
        self.y = 0
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = None

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2
        if d >= 16:
            d = 16
        if d < 0:
            d -= 2
        self.y += d

    def draw(self, win):
        self.img_count += 1
        self.img = self.IMGS[self.img_count // 5 % len(self.IMGS)]
        win.blit(self.img, (self.x, self.y))
