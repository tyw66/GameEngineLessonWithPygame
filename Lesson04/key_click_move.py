'''
学习输入系统——物体的点击移动
靠输入事件处理，处理键盘/鼠标按下事件，使方块进行1次移动，并加入摩擦力
'''
import pygame

WINDOW_SIZE = (640, 480)    # 窗口大小
FRICTION = 0.95             # 摩擦力系数（0.95 = 每帧减少5%速度）
MIN_VELOCITY = 0.1          # 最小速度阈值  
CUBE_WIDTH = 50             # 方块宽度
CUBE_HEIGHT = 50            # 方块高度

def handle_input():
    global running,velocity, pos_x, pos_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            dir = pygame.math.Vector2(
                pygame.mouse.get_pos()[0] - pos_x,
                pygame.mouse.get_pos()[1] - pos_y,
            ).normalize()
            velocity[0]  += 4 * dir[0]
            velocity[1]  += 4 * dir[1]


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
    # 渲染标题
    txt = f"Click mouse button or keybord to move"
    title_text = font.render(txt, True, (255, 255, 255))
    screen.blit(title_text, (10, 20)) 
    # 绘制方块
    pygame.draw.rect(screen, (210, 128, 45), (pos_x, pos_y, CUBE_WIDTH, CUBE_HEIGHT))
    # 显示帧率
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {int(fps)}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 50))
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
    pygame.display.set_caption("Lesson04 - Click Move It!")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    # 游戏主循环
    running = True
    while running:
        # 处理输入
        handle_input()
        # 更新场景状态
        update()
        # 渲染场景
        render()
        # 控制帧率
        clock.tick(60)
    
   