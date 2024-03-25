import pygame
import random

# 游戏窗口大小
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# 方格大小
CELL_SIZE = 20

# 方向
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 初始化 Pygame
pygame.init()

# 创建游戏窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("贪吃蛇")

# 创建时钟
clock = pygame.time.Clock()

# 加载字体
font = pygame.font.SysFont(None, 40)

# 初始化贪吃蛇
snake = [(5, 5), (4, 5), (3, 5)]
direction = RIGHT

# 初始化食物
food = (random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1), random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1))

# 循环标志位
running = True

while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            elif event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT

    # 移动贪吃蛇
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)

    # 判断是否吃到食物
    if head == food:
        food = (random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1), random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1))
    else:
        snake.pop()

    # 判断是否撞墙或撞自己
    if head[0] < 0 or head[0] >= WINDOW_WIDTH // CELL_SIZE or head[1] < 0 or head[1] >= WINDOW_HEIGHT // CELL_SIZE or head in snake[1:]:
        running = False

    # 绘制背景
    window.fill(BLACK)

    # 绘制食物
    pygame.draw.rect(window, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # 绘制贪吃蛇
    for cell in snake:
        pygame.draw.rect(window, GREEN, (cell[0] * CELL_SIZE, cell[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # 绘制分数
    score = len(snake) - 3
    text = font.render("Score: " + str(score), True, WHITE)
    window.blit(text, (WINDOW_WIDTH - text.get_width() - 10, 10))

    # 更新窗口
    pygame.display.update()

    # 控制蛇的运动速度
    clock.tick(10)