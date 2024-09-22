import pygame
import random

# 初始化 Pygame
pygame.init()

# 設定螢幕大小
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("2D 射擊遊戲")

# 設定顏色
WHITE = (255, 255, 255)

# 載入圖片

font = pygame.font.Font(None, 30)  # 使用 Pygame 的預設字體，字型大小為 30

# 定義 Bullet 類別
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10  # 子彈速度快一些，適應更大的畫面
        self.active = True  # 子彈是否存在

    def move(self):
        self.x += self.speed
        if self.x > 1280:  # 超出螢幕就不再顯示
            self.active = False

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 20, 10))  # 調整子彈大小適應新螢幕

# 定義 Target 類別
class Target:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def reset_position(self):
        self.y = random.randint(10, 620)  # 隨機化 y 座標，適應新的畫面高度

# 創建多個 Target 物件
num_targets = 5  # 增加標靶數量以適應較大畫面
targets = [Target(1180, random.randint(10, 620), target_image) for _ in range(num_targets)]

# 記錄所有的子彈
bullets = []

# 遊戲循環
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if __name__ == __main__:
        

    # 更新螢幕
    pygame.display.flip()
    clock.tick(60)  # 每秒 60 幀

# 結束 Pygame
pygame.quit()
