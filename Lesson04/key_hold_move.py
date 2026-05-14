'''
学习输入系统——物体的持续移动
靠轮询检测输入，检测是否持续按下键盘/鼠标，使方块持续移动
'''
import pygame

WINDOW_SIZE = (640, 480)    # 窗口大小
CUBE_WIDTH = 50             # 方块宽度
CUBE_HEIGHT = 50            # 方块高度

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def update():
    global pos_x,pos_y
    #轮询输入状态
    speed = 5
    if useMouse:
        mouseL,mouseM,mousR = pygame.mouse.get_pressed()
        if mouseL:
            dir = pygame.math.Vector2(
                pygame.mouse.get_pos()[0] - pos_x,
                pygame.mouse.get_pos()[1] - pos_y,
            ).normalize()
            pos_x += speed * dir[0]
            pos_y += speed * dir[1]
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pos_x -= speed
        if keys[pygame.K_RIGHT]:
            pos_x += speed
        if keys[pygame.K_UP]:
            pos_y -= speed
        if keys[pygame.K_DOWN]:
            pos_y += speed
    


def render():
    # 渲染场景
    screen.fill((112,146,190))
    # 绘制方块
    pygame.draw.rect(screen, (255, 182, 105), (pos_x - CUBE_WIDTH/2, pos_y - CUBE_HEIGHT/2, CUBE_WIDTH, CUBE_HEIGHT))
    # 渲染标题
    txt = f"Press mouse to move" if useMouse else f"Press keybord to move"
    title_text = font.render(txt, True, (255, 255, 255))
    screen.blit(title_text, (10, 20)) 
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
    useMouse = True

    # 初始化 Pygame
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Lesson04 - Move It!")
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
    
   