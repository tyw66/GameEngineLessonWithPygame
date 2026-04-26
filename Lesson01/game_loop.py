'''
学习游戏主循环
'''
import pygame
import sys

WINDOW_SIZE = (640, 480)    # 窗口大小

def handle_input():
    #取出事件队列中的事件并处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def update():
    # 更新场景状态
    pass

def render():
    # 清屏
    screen.fill((153, 204, 255))
    # 在后台缓冲区绘制矩形
    pygame.draw.rect(screen, (210, 128, 45), (50,50,100,100))   
    # 显示帧率文字
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {int(fps)}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))
    # 更新显示，即完整切换缓冲区到前台显示
    pygame.display.flip()

if __name__ == "__main__":  
    # 初始化 Pygame
    pygame.init()
    # 创建窗口，默认是双缓冲
    screen = pygame.display.set_mode(WINDOW_SIZE) 
    # 设置窗口标题
    pygame.display.set_caption("Lesson01 - Pygame Game Loop")
    # 创建时钟对象，用于控制帧率
    clock = pygame.time.Clock()
    # 加载字体
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
    
   