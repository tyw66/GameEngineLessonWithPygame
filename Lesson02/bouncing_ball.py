'''
学习时间系统——弹跳球示例
由于pygame自身不支持物理更新帧率与渲染帧率分开，所以没有用pygame的tick方法，转而自己实现
通过按tab键切换固定时间/可变时间，按上下键修改渲染帧率大小，来观察弹跳行为的不同，理解物理帧率与渲染帧率。
'''
import sys
import time
import pygame

def handle_input():
    global is_fixed_time, fps_render, delta_time_render
    for event in pygame.event.get():
        # 退出
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
        # 切换固定时间/可变时间
            if event.key == pygame.K_TAB:
                is_fixed_time = not is_fixed_time
            elif event.key == pygame.K_UP:
                fps_render += 10
                if fps_render > 120:
                    fps_render = 120
                delta_time_render = 1.0 / fps_render
            elif event.key == pygame.K_DOWN:
                fps_render -= 10
                if fps_render < 10:
                    fps_render = 10
                delta_time_render = 1.0 / fps_render         


def simulation(delta_time):
    '''更新弹跳球的运动参数，仅模拟竖直重力加速度，不考虑空气阻力'''
    global ball_position, ball_velocity
    ball_velocity[1] += 980 * delta_time
    ball_position[1] += ball_velocity[1] * delta_time
    if ball_position[1] + 50 > WINDOW_SIZE[1]:
        ball_position[1] = WINDOW_SIZE[1] - 50   
        ball_velocity[1] = -ball_velocity[1] 


def update(delta_time):
    '''物理更新：固定(高)频率'''  
    if is_fixed_time:
        simulation(delta_time)

def render(delta_time):
    '''渲染：可变(低)频率'''  
    if not is_fixed_time:
        # 错误的实现：在渲染循环中更新物理参数，这会导致物理更新频率等于渲染帧率，运动不稳定
        simulation(delta_time)

    screen.fill((116, 161, 195))
    screen.blit(title_text, (10, 10))
    fixed_time_text = font.render(f"Fixed Time: {is_fixed_time}", True, (255, 255, 255))
    screen.blit(fixed_time_text, (10, 50))    
    fps_text = font.render(f"Physics: {PHYSICS_FPS}FPS, Render: {fps_render}FPS", True, (255, 255, 255))
    screen.blit(fps_text, (10, 80))
    pygame.draw.circle(screen, OBJECT_COLOR, (ball_position[0], ball_position[1]), 50)
    pygame.display.flip()


if __name__ == "__main__":  
    # 初始化游戏参数    
    WINDOW_SIZE = (800, 600)                # 窗口大小  
    OBJECT_COLOR = (255, 255, 255)          # 对象颜色    
    PHYSICS_FPS = 60                        # 物理更新频率
    PHYSICS_DELTA = 1.0 / PHYSICS_FPS       # 物理时间步长（秒）
    MAX_PHYSICS_FRAMES = 5                  # 最大物理帧累积（防止螺旋死亡）
    
    fps_render = 20                         # 渲染更新频率      <---- 按上下键修改
    delta_time_render = 1.0 / fps_render    # 渲染时间步长（秒）    
    is_fixed_time = True                    # 是否采用固定时间步长更新物理参数 <---- 按TAB键切换，观察弹跳高度变化
    lag_physical = 0.0                      # 差值（物理时间 真实时间）
    lag_render = 0.0                        # 差值（渲染时间 真实时间）
    
    ball_position = [400, 200]              # 球体初始位置
    ball_velocity = [0, 0]                  # 球体初始速度  

    # 初始化 Pygame
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Lesson02 - Time System")
    font = pygame.font.Font(None, 30)
    title_text = font.render("Press \"Tab\" to toggle fixed/delta time.  Press \"Up\"/\"Down\" to change render FPS.", True, (255, 255, 255))
    # 初始化时间（秒）
    last_time = time.time()

    # 游戏主循环
    while True:
        # 计算当前时间（秒）
        current_time = time.time()
        elapsed_time = current_time - last_time
        last_time = current_time

        # 累积物理时间
        lag_physical += elapsed_time
        # 累积渲染时间
        lag_render += elapsed_time
        # 处理输入
        handle_input()        

        # 执行固定时间步长的物理更新，让物理时间“追上”真实时间
        physics_steps = 0
        while lag_physical >= PHYSICS_DELTA and physics_steps < MAX_PHYSICS_FRAMES:
            update(PHYSICS_DELTA)
            lag_physical -= PHYSICS_DELTA
            physics_steps += 1
        
        # 如果累积了太多物理帧，直接清空累积器（防止螺旋死亡）
        if physics_steps >= MAX_PHYSICS_FRAMES:
            lag_physical = 0
        
        # 渲染更新，让渲染时间“追上”真实时间
        while lag_render >= delta_time_render:
            lag_render -= delta_time_render
            render(delta_time_render)
        
        # 让出时间给系统其他进程
        time.sleep(0.01)
