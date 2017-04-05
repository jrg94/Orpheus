import bge
from bge import render
g=bge.logic
scene = g.getCurrentScene()



co = bge.logic.getCurrentController()
o= co.owner

#sensor
mouse = co.sensors["mousesensor"]

#objects
camera = scene.objects["CameraB"]
character = scene.objects["Character - Level 2"]

#####mouse movement

movSpeed = 0.3
rotSpeed = (0.005, 0.005)

# mouse look
x = (render.getWindowWidth() / 2 - mouse.position[0])
y = (render.getWindowHeight() / 2 - mouse.position[1])

character.applyRotation((0 , 0, int(x) * rotSpeed[0]), False)
camera.applyRotation((int(y) * rotSpeed[1], 0, 0), True)
render.setMousePosition(int(render.getWindowWidth() / 2), int(render.getWindowHeight() / 2))