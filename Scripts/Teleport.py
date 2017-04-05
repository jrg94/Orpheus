from bge import logic
cont = logic.getCurrentController()
own = cont.owner

scene = logic.getCurrentScene()
obj = scene.objects[own['to']]

player = scene.objects['Character']
lava = scene.objects['LavaSave']
empty = scene.objects['Teleporters']
act = empty.actuators['Port']

# check Active and Collision, then teleport
if own['Active'] == 0 and cont.sensors['Collision'].positive:
    player.worldPosition = [obj.worldPosition[0],obj.worldPosition[1],obj.worldPosition[2]+1]
    obj['Active'] = 1
    
    # check for lava exception
    if own != lava:
         act.startSound()
    
# check Active, then activate    
if cont.sensors['Away'].positive:
    own['Active'] = 0