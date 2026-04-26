extends Node2D

func _ready() -> void:
	print("就绪_ready")
	#物理帧率在”Project → Project Settings → Physics → Common → Physics Ticks Per Second”中修改
	#渲染帧率在”Project → Project Settings → Application → Run →  Max FPS“中修改（默认是 0，代表不限制）
	#渲染帧率也可在此修改
	#Engine.max_fps = 30
	

func _physics_process(delta: float) -> void:
	print("物理循环_physics_process" + str(delta))
	
	
func _process(delta: float) -> void:
	print("渲染循环_process" + str(delta))
