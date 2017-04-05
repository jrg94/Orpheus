import GameLogic

# get controller
controller = GameLogic.getCurrentController()

# get current scene and sensors
scene = GameLogic.getCurrentScene()
random = controller.sensors['Random']
property = controller.sensors['CheckSwitch']

# check sensors
if property.positive and random.positive:

    # store all outcomes
    blue = "BossPlateB"
    red = "BossPlateR"
    green = "BossPlateG"
    teal = "BossPlateT"
    yellow = "BossPlateY"
    purple = "BossPlateP"
    
    # generate a random number between 1 and 6
    index = 6
    seed = GameLogic.getRandomFloat()
    find = int(seed * index) + 1
    
    # match number with color
    if find == 1:
        obj = red
    elif find == 2:
        obj = blue
    elif find == 3:
        obj = green
    elif find == 4:
        obj = teal
    elif find == 5:
        obj = yellow
    elif find == 6:
        obj = purple
    
    # Add object at Gun's position
    scene.addObject(obj, "Gun", 500)
     
    
    