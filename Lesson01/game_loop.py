'''
学习游戏主循环, 不封装任何高级类。
写一个最小 Demo: 窗口 + 移动方块 + 按键控制 + 帧率显示
'''
import pygame

WINDOW_SIZE = (640, 480)    # 窗口大小
FRICTION = 0.95             # 摩擦力系数（0.95 = 每帧减少5%速度）
MIN_VELOCITY = 0.1          # 最小速度阈值  
CUBE_WIDTH = 50             # 方块宽度
CUBE_HEIGHT = 50            # 方块高度

def handle_input():
    global velocity
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity[0] -= 4
            elif event.key == pygame.K_RIGHT:
                velocity[0] += 4
            elif event.key == pygame.K_UP:
                velocity[1] -= 4
            elif event.key == pygame.K_DOWN:
                velocity[1] += 4    
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()


def update():
    global pos_x, pos_y
    pos_x += velocity[0]
    pos_y += velocity[1]
    # 边界检测
    if pos_x < 0:
        velocity[0] = -velocity[0]
        pos_x = 0
    elif pos_x > WINDOW_SIZE[0] - CUBE_WIDTH:
        velocity[0] = -velocity[0]
        pos_x = WINDOW_SIZE[0] - CUBE_WIDTH

    if pos_y < 0:
        velocity[1] = -velocity[1]
        pos_y = 0
    elif pos_y > WINDOW_SIZE[1] - CUBE_HEIGHT:
        velocity[1] = -velocity[1]
        pos_y = WINDOW_SIZE[1] - CUBE_HEIGHT

    # 摩擦力
    velocity[0] *= FRICTION
    velocity[1] *= FRICTION
    # 速度截断
    velocity[0] = velocity[0] if abs(velocity[0]) > MIN_VELOCITY else 0
    velocity[1] = velocity[1] if abs(velocity[1]) > MIN_VELOCITY else 0


def render():
    # 渲染场景
    screen.fill((153, 204, 255))
    # 绘制方块
    pygame.draw.rect(screen, (210, 128, 45), (pos_x, pos_y, CUBE_WIDTH, CUBE_HEIGHT))
    # 显示帧率
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {int(fps)}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))
    # 更新显示
    pygame.display.flip()

if __name__ == "__main__":  
    # 初始化参数
    pos_x = WINDOW_SIZE[0] // 2 - CUBE_WIDTH // 2
    pos_y = WINDOW_SIZE[1] // 2 - CUBE_HEIGHT // 2
    velocity = [0, 0]

    # 初始化 Pygame
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Lesson01 - Pygame Game Loop")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    # 游戏主循环
    while True:
        # 处理输入
        handle_input()
        # 更新场景状态
        update()
        # 渲染场景
        render()
        # 控制帧率
        clock.tick(60)
    
   