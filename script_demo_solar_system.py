# 
from gaia.cu9.ari.gaiaorbit.script import EventScriptingInterface
gs = EventScriptingInterface.instance()

def showAnObject( obj, msg ):
    i=0
    gs.setHeadlineMessage(obj)
    gs.setSubheadMessage(msg)
    gs.setCameraFocus(obj)
    gs.goToObject(obj, 20.0, 4.5)
    
    for i in range(90):
        gs.setCameraPositionAndFocus(obj, "Sol", i, 30)
        gs.sleep(0.03)
    
    return;

def zoomOut():
    gs.setCameraFocus("Earth")
    gs.goToObject("Earth",0.00000000005,5)
    return;

# Disable input
gs.disableInput()
gs.cameraStop()
gs.minimizeInterfaceWindow()

# Welcome
gs.setCinematicCamera(True)
gs.setHeadlineMessage("A long time ago in a galaxy far, far away....")
gs.sleep(2)

# Sun
gs.setHeadlineMessage("Sun")
gs.setSubheadMessage("This is our star, the Sun")
gs.setCameraFocus("Sol")
gs.goToObject("Sol", 20.0, 4.5)
gs.sleep(1)

#Mercury
showAnObject( obj="Mercury", msg="This is Mercury")

#Venus
showAnObject( obj="Venus", msg="This is Venus")

# Earth
showAnObject( obj="Earth", msg="This is our planet, the Earth")

#Mars
showAnObject( obj="Mars", msg="This is Mars")

#Jupiter
showAnObject( obj="Jupiter", msg="This is Jupiter")

#Saturn
showAnObject( obj="Saturn", msg="This is Saturn")

#Uranus
showAnObject( obj="Uranus", msg="This is Uranus")

#Neptune
showAnObject( obj="Neptune", msg="This is Neptune")

#Pluto
showAnObject( obj="Pluto", msg="This is Pluto ... and it is not a planet anymore :( ")

zoomOut()

# Maximize interface and enable input
gs.clearAllMessages()
gs.maximizeInterfaceWindow()
gs.enableInput()

'''
gs.enableInput()
'''
