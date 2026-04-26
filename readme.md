# 基于 Pygame 的游戏引擎底层原理学习路线

作者：@一尾66

本文档为「游戏原理教具学习路线」，核心目标是：**利用Pygame库手写实现现代 2D 游戏引擎核心模块，反向理解 Godot/Unity 等引擎的基本原理**。

## 课程说明

✅ 全程采用 **「学习目标｜重点理解｜动手练习题 | 映射引擎原理」** 固定结构，阶段从易到难、边界清晰，知识点归属精准。

✅ 每阶段末尾设**综合案例**，用一个稍大 Demo 整合本阶段全部知识点，实现单点学习到综合落地的闭环。

✅ 知识基础：Python 基础语法、面向对象编程、基础数学计算（坐标、向量、三角函数）。

✅ 运行环境：Python + Pygame 最新稳定版，配置代码格式化、调试工具。

## 课程内容

### 第一阶段｜引擎运行基础骨架

阶段目标：彻底搞懂游戏程序最底层运行逻辑，掌握主循环、时间系统、静态渲染、输入交互四大基础能力，建立「循环驱动画面、时间驱动逻辑、输入控制交互」的核心认知。

- [Lesson01 - 最小游戏主循环实现（一切的起点）](./Lesson01/readme.md)
- [Lesson02 - 时间系统与 delta time + 固定时间步长](./Lesson02/readme.md)
- [Lesson03 - 静态渲染与 画布基础](./Lesson03/readme.md)
- [Lesson04 - 输入系统与交互判定底层](./Lesson04/readme.md)
- [Milestone 01 - 综合案例：极简桌面交互画板](./Milestone01/readme.md)

### 第二阶段｜引擎核心功能系统

阶段目标：手写实现现代 2D 引擎内置的几大核心系统，覆盖 Godot 日常高频功能。

- [Lesson05 - 精灵系统与游戏实体管理](./Lesson05/readme.md)
- [Lesson06 - 场景图与节点变换](./Lesson06/readme.md)
- [Lesson07 - 有限状态机 FSM](./Lesson07/readme.md) 
- [Lesson08 - 资源管理与静态配置系统](./Lesson08/readme.md)
- [Lesson09 - 存档系统与数据持久化](./Lesson09/readme.md)
- [Lesson10 - 碰撞检测与简易物理系统](./Lesson10/readme.md)
- [Lesson11 - 动画系统与时间驱动逻辑](./Lesson11/readme.md)
- [Lesson12 - 粒子系统与批量特效底层原理](./Lesson12/readme.md)
- [Lesson13 - 音频系统基础](./Lesson13/readme.md)
- [Milestone 02 - 综合案例：极简横版闯关小游戏](./Milestone02/readme.md)

### 第三阶段｜游戏工程化与高级架构

阶段目标：从“能运行的 Demo”升级为“可维护、可扩展的工业级架构”。

- [Lesson14 - 事件系统与模块解耦通信](./Lesson14/readme.md)
- [Lesson15 - 分层架构与模块设计规范](./Lesson15/readme.md)
- [Lesson16 - 性能优化基础](./Lesson16/readme.md)
- [Milestone 03 - 综合案例：分层架构版模拟经营 Demo](./Milestone03/readme.md)


## 学习建议

- 聚焦核心闭环：每课结束完成「手写底层原理 + Godot 对应功能验证」
- 严控项目边界：单点轻量化，案例适度扩展；
