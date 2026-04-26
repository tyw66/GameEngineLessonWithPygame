# Lesson06 - 场景图与节点变换（Node \&amp; Transform）

## 学习目标

1. 理解场景树 (SceneTree) 和局部/全局坐标变换原理；
2. 实现简单的父子节点层级、相对位置计算；
3. 理解摄像机跟随的本质是变换矩阵。

## 重点理解

- 节点树：每个节点有 `parent` 和 `children`，最终世界坐标 = 父节点世界坐标 + 局部坐标。
- 变换递归：`update\_transform\(\)` 递归计算子节点坐标。
- 引擎对应：Godot 中 `Node2D\.position`（局部）与 `global\_position` 的区别。
- 摄像机：本质上是一个节点，将其变换矩阵取逆，作用于所有世界坐标。

## 动手练习题

1. 实现一个 `TransformNode` 类（不重名 Pygame 类），包含 `local\_pos`、`global\_pos`、`parent`、`children`，提供 `add\_child`、`update\_global\_transform`。
2. 创建一个玩家节点，一个武器子节点，移动玩家时武器自动跟随。
3. 实现简单摄像机节点：世界坐标减去摄像机坐标后再绘制。
4. 扩展：支持旋转和缩放（可选）。

## 🔁 映射引擎原理

- 在 Godot 中创建 `Node2D` A 和子节点 `Sprite2D` B，移动 A，观察 B 的相对移动。
- 思考：如果没有引擎自动的全局坐标计算，你需要手动做什么？
