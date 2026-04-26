# Lesson05 - Sprite 精灵系统与游戏实体管理

## 学习目标

1. 理解 Sprite 作为「2D 游戏引擎通用实体单元」的概念；
2. 掌握 Pygame 原生 `Sprite`、`Group` 的批量管理机制；
3. 理解「实体 – 批量更新 – 批量绘制」的工业范式。

## 重点理解

- 跨引擎本质：
  - Pygame `Sprite` ≈ Godot `Sprite2D/Node2D` ≈ Unity `SpriteRenderer \+ GameObject`
- 生命周期：`init` → `update\(delta\)` → `kill\(\)`
- Group 优势：一行代码 `group\.update\(delta\)` 和 `group\.draw\(surface\)` 实现批量操作
- 内置碰撞：`pygame\.sprite\.spritecollide` 等函数快速实现碰撞检测

## 动手练习题

1. 继承 `Sprite` 封装玩家类，包含位置、贴图、基于 delta 的移动逻辑。
2. 使用 `Group` 管理玩家、敌人、道具，批量 `update\(delta\)` 和 `draw`。
3. 碰撞实战：玩家碰敌人减少生命，碰道具拾取。

## 🔁 映射引擎原理

- 在 Godot 中创建多个 `CharacterBody2D` 放入同一父节点，对比 `\_process` 被自动遍历调用的方式。
- 思考：Godot 的场景树如何自动实现「批量更新」？你手写的 Group 与它有何异同？
